#!/usr/bin/env node
/**
 * Unified test runner for SDD-Vibe Framework.
 * Usage:
 *   node scripts/run-tests.js                  (run all tests)
 *   node scripts/run-tests.js --filter parser  (run only parser tests)
 */
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const TESTS_DIR = path.join(__dirname, '..', 'tests');
const filter = process.argv.find((a, i) => process.argv[i - 1] === '--filter') || '';

const files = fs
  .readdirSync(TESTS_DIR)
  .filter((f) => f.startsWith('test_') && f.endsWith('.js'))
  .filter((f) => !filter || f.includes(filter))
  .sort();

console.log('═══════════════════════════════════════════════════════════════');
console.log('   🧪 SDD-VIBE FRAMEWORK TEST RUNNER');
console.log('═══════════════════════════════════════════════════════════════');
console.log(`  Suites found: ${files.length}${filter ? ` (filter: "${filter}")` : ''}`);
console.log(`  Timestamp:    ${new Date().toISOString()}\n`);

let passed = 0;
let failed = 0;
const failures = [];

for (const file of files) {
  const filePath = path.join(TESTS_DIR, file);
  process.stdout.write(`  ▶ ${file} ... `);
  try {
    execSync(`node "${filePath}"`, { stdio: 'pipe', timeout: 30000 });
    console.log('✅ PASS');
    passed++;
  } catch (err) {
    console.log('❌ FAIL');
    failed++;
    failures.push({
      file,
      output: (err.stderr || err.stdout || err.message || '').toString().slice(-800),
    });
  }
}

console.log('\n═══════════════════════════════════════════════════════════════');
console.log(`  Results: ${passed} passed, ${failed} failed, ${files.length} total`);
if (failures.length > 0) {
  console.log('\n  ❌ FAILURES:');
  for (const f of failures) {
    console.log(`\n  --- ${f.file} ---`);
    console.log(
      f.output
        .split('\n')
        .map((l) => '    ' + l)
        .join('\n')
    );
  }
}
console.log('═══════════════════════════════════════════════════════════════');
process.exit(failed > 0 ? 1 : 0);
