/**
 * SSE Stream & Rapid Reconnection Regression Test (ERR-004 / AC-FEAT001-01)
 * Verifies /api/stream delivers valid SSE frames and handles abrupt client
 * disconnects / rapid reconnections without crashing the dashboard server.
 * Zero external dependencies — uses pure Node.js standard library.
 */

const assert = require('assert');
const http = require('http');
const net = require('net');
const path = require('path');
const { spawn } = require('child_process');

const SERVER_PATH = path.resolve(__dirname, '../Project-Manager-Dashboard/server.js');
const PROJECT_ROOT = path.resolve(__dirname, '..');

function getFreePort() {
  return new Promise((resolve, reject) => {
    const srv = net.createServer();
    srv.listen(0, '127.0.0.1', () => {
      const { port } = srv.address();
      srv.close(() => resolve(port));
    });
    srv.on('error', reject);
  });
}

function startDashboardServer(port) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [SERVER_PATH, `--port=${port}`, `--project=${PROJECT_ROOT}`], {
      stdio: ['ignore', 'pipe', 'pipe']
    });
    let stderr = '';
    const timer = setTimeout(() => reject(new Error('Server startup timed out')), 8000);

    child.stdout.on('data', (chunk) => {
      if (chunk.toString().includes('Live in-IDE daemon active')) {
        clearTimeout(timer);
        resolve({ child, getStderr: () => stderr });
      }
    });
    child.stderr.on('data', (chunk) => {
      stderr += chunk.toString();
    });
    child.on('exit', (code) => {
      clearTimeout(timer);
      if (code !== null && code !== 0) {
        reject(new Error(`Server exited early with code ${code}: ${stderr}`));
      }
    });
  });
}

function connectSse(port, { abortImmediately = false } = {}) {
  return new Promise((resolve, reject) => {
    const req = http.get({
      hostname: '127.0.0.1',
      port,
      path: '/api/stream',
      headers: { Accept: 'text/event-stream' }
    }, (res) => {
      if (abortImmediately) {
        req.destroy();
        resolve({ statusCode: res.statusCode, aborted: true });
        return;
      }
      let buffer = '';
      res.on('data', (chunk) => {
        buffer += chunk.toString();
        if (buffer.includes('\n\n')) {
          req.destroy();
          resolve({ statusCode: res.statusCode, headers: res.headers, frame: buffer });
        }
      });
      res.on('error', () => resolve({ statusCode: res.statusCode, aborted: true }));
    });
    req.on('error', (err) => {
      if (abortImmediately && (err.code === 'ECONNRESET' || err.message.includes('aborted'))) {
        resolve({ aborted: true });
      } else {
        reject(err);
      }
    });
    if (abortImmediately) {
      setImmediate(() => req.destroy());
    }
  });
}

async function run() {
  console.log('=================================================================');
  console.log('       📡 SSE STREAM & RECONNECTION REGRESSION TEST SUITE        ');
  console.log('=================================================================\n');

  const port = await getFreePort();
  const { child, getStderr } = await startDashboardServer(port);

  try {
    // 1. Verify initial SSE handshake and JSON payload
    const first = await connectSse(port);
    assert.strictEqual(first.statusCode, 200, 'SSE endpoint should return HTTP 200');
    assert.ok(
      (first.headers['content-type'] || '').includes('text/event-stream'),
      'Content-Type must be text/event-stream'
    );
    assert.ok(first.frame.startsWith('data: '), 'SSE frame must start with "data: "');
    const parsed = JSON.parse(first.frame.replace(/^data:\s*/, '').trim());
    assert.ok(parsed && typeof parsed === 'object', 'SSE frame payload must be valid JSON');
    console.log('  ✅ [PASS] Handshake: /api/stream emits valid text/event-stream JSON frame');

    // 2. Rapidly open and immediately destroy 10 SSE connections
    await Promise.all(
      Array.from({ length: 10 }, () => connectSse(port, { abortImmediately: true }))
    );
    console.log('  ✅ [PASS] Rapid Disconnect: 10 immediate client aborts handled cleanly');

    // 3. Verify server remains healthy and serves subsequent SSE + HTTP requests
    const followUp = await connectSse(port);
    assert.strictEqual(followUp.statusCode, 200, 'Server must remain healthy after rapid aborts');
    assert.ok(followUp.frame.startsWith('data: '), 'Subsequent SSE client receives valid frame');
    assert.strictEqual(child.exitCode, null, 'Server process must still be running');
    assert.strictEqual(getStderr().trim(), '', 'Server stderr must remain empty');
    console.log('  ✅ [PASS] Recovery: Subsequent SSE reconnection succeeds with zero server errors');

    console.log('\n=================================================================');
    console.log('  🎉 ALL 3/3 SSE STREAM REGRESSION CHECKS PASSED SUCCESSFULLY!');
    console.log('=================================================================');
  } finally {
    child.kill();
  }
}

run().catch((err) => {
  console.error('❌ SSE stream test failed:', err);
  process.exit(1);
});
