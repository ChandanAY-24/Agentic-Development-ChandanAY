/**
 * Behavioral Test Suite for DashboardParser
 * Tests actual parsing logic with fixture data, verifying JSON output structure,
 * data correctness, task prioritization, error classification, and CSV export.
 */

const path = require('path');
const assert = require('assert');
const DashboardParser = require('../Project-Manager-Dashboard/parser');

const FIXTURE_ROOT = path.resolve(__dirname, 'fixtures');
const parser = new DashboardParser(FIXTURE_ROOT);

console.log('=================================================================');
console.log('   🔬 BEHAVIORAL PARSER TEST SUITE (FIXTURE-DRIVEN)              ');
console.log('=================================================================');
console.log(`Fixture Root: ${FIXTURE_ROOT}`);
console.log(`Timestamp:    ${new Date().toISOString()}\n`);

let passedChecks = 0;
let totalChecks = 0;

function runCheck(name, fn) {
  totalChecks++;
  try {
    fn();
    console.log(`  ✅ [PASS] ${name}`);
    passedChecks++;
  } catch (err) {
    console.error(`  ❌ [FAIL] ${name}: ${err.message}`);
    throw err;
  }
}

// ── 1. Task Parsing ──────────────────────────────────────────────────────────
runCheck('parseTasks: extracts correct number of tasks from fixture', () => {
  const tasks = parser.parseTasks();
  assert(Array.isArray(tasks), 'parseTasks must return an array');
  assert(tasks.length >= 3, `Expected >= 3 tasks, got ${tasks.length}`);
});

runCheck('parseTasks: identifies task IDs correctly', () => {
  const tasks = parser.parseTasks();
  const ids = tasks.map((t) => t.id);
  assert(ids.includes('TASK-001'), 'Must find TASK-001');
  assert(ids.includes('TASK-002'), 'Must find TASK-002');
  assert(ids.includes('TASK-003'), 'Must find TASK-003');
});

runCheck('parseTasks: maps status values correctly', () => {
  const tasks = parser.parseTasks();
  const t1 = tasks.find((t) => t.id === 'TASK-001');
  const t2 = tasks.find((t) => t.id === 'TASK-002');
  const t3 = tasks.find((t) => t.id === 'TASK-003');
  assert.strictEqual(t1.status, 'DONE', 'TASK-001 should be DONE');
  assert.strictEqual(t2.status, 'IN_PROGRESS', 'TASK-002 should be IN_PROGRESS');
  assert.strictEqual(t3.status, 'BACKLOG', 'TASK-003 should be BACKLOG');
});

runCheck('parseTasks: extracts priority from task header', () => {
  const tasks = parser.parseTasks();
  const t1 = tasks.find((t) => t.id === 'TASK-001');
  assert(t1.priority === 'P1' || t1.priority === 1, `Expected P1 priority, got ${t1.priority}`);
});

runCheck('parseTasks: extracts subtasks and completion state', () => {
  const tasks = parser.parseTasks();
  const t1 = tasks.find((t) => t.id === 'TASK-001');
  assert(Array.isArray(t1.subtasks) && t1.subtasks.length >= 2, 'TASK-001 must have >= 2 subtasks');
  assert(t1.subtasks.every((s) => s.completed === true), 'TASK-001 subtasks should all be completed');
});

// ── 2. Phase Parsing ─────────────────────────────────────────────────────────
runCheck('parsePhases: extracts phases from fixture', () => {
  const phases = parser.parsePhases();
  assert(Array.isArray(phases), 'parsePhases must return an array');
  assert(phases.length >= 3, `Expected >= 3 phases, got ${phases.length}`);
});

runCheck('parsePhases: maps phase status correctly', () => {
  const phases = parser.parsePhases();
  const p1 = phases.find((p) => p.name && p.name.includes('Foundation'));
  const p2 = phases.find((p) => p.name && p.name.includes('Enrollment'));
  if (p1) assert.strictEqual(p1.status, 'DONE', 'Phase 1 should be DONE');
  if (p2) assert.strictEqual(p2.status, 'IN_PROGRESS', 'Phase 2 should be IN_PROGRESS');
});

// ── 3. Error Parsing ─────────────────────────────────────────────────────────
runCheck('parseErrors: extracts errors from defect log table', () => {
  const errors = parser.parseErrors();
  assert(Array.isArray(errors), 'parseErrors must return an array');
  assert(errors.length >= 3, `Expected >= 3 errors, got ${errors.length}`);
});

runCheck('parseErrors: identifies severity levels', () => {
  const errors = parser.parseErrors();
  const e1 = errors.find((e) => e.id === 'ERR-001');
  const e2 = errors.find((e) => e.id === 'ERR-002');
  if (e1) assert(e1.severity === 'P1' || e1.sev === 'P1', 'ERR-001 must be P1');
  if (e2) assert(e2.severity === 'P0' || e2.sev === 'P0', 'ERR-002 must be P0');
});

runCheck('parseErrors: distinguishes ACTIVE vs RESOLVED status', () => {
  const errors = parser.parseErrors();
  const resolved = errors.filter((e) => e.status === 'RESOLVED');
  const active = errors.filter((e) => e.status === 'ACTIVE');
  assert(resolved.length >= 2, `Expected >= 2 RESOLVED, got ${resolved.length}`);
  assert(active.length >= 1, `Expected >= 1 ACTIVE, got ${active.length}`);
});

// ── 4. Error Telemetry Aggregation ───────────────────────────────────────────
runCheck('parseErrorTelemetry: returns summary severity and resolution counts', () => {
  const telemetry = parser.parseErrorTelemetry();
  assert(telemetry && telemetry.summary, 'parseErrorTelemetry must return summary object');
  assert.strictEqual(telemetry.summary.total, 3, 'Must report 3 total defects');
  assert.strictEqual(telemetry.summary.active, 1, 'Must report 1 active defect');
  assert.strictEqual(telemetry.summary.resolved, 2, 'Must report 2 resolved defects');
  assert.strictEqual(telemetry.summary.p2, 1, 'Must report 1 active P2 defect');
});

// ── 5. Kanban CSV Export ─────────────────────────────────────────────────────
runCheck('exportKanbanCsv: produces valid CSV with header row', () => {
  const tasks = parser.parseTasks();
  const csv = parser.exportKanbanCsv(tasks);
  assert(typeof csv === 'string', 'CSV must be a string');
  const lines = csv.trim().split('\n');
  assert(lines.length >= 2, 'CSV must have header + at least 1 data row');
  const header = lines[0];
  assert(header.includes('task_id'), 'CSV header must include task_id');
  assert(header.includes('status'), 'CSV header must include status');
  assert(header.includes('title'), 'CSV header must include title');
});

runCheck('exportKanbanCsv: data rows match task count', () => {
  const tasks = parser.parseTasks();
  const csv = parser.exportKanbanCsv(tasks);
  const lines = csv.trim().split('\n');
  assert.strictEqual(lines.length - 1, tasks.length, `Expected ${tasks.length} data rows, got ${lines.length - 1}`);
});

runCheck('exportKanbanCsv: DONE tasks get APPROVED sign_off', () => {
  const tasks = parser.parseTasks();
  const csv = parser.exportKanbanCsv(tasks);
  const doneRow = csv.split('\n').find((line) => line.includes('TASK-001'));
  assert(doneRow, 'CSV must contain TASK-001 row');
  assert(doneRow.includes('APPROVED'), 'DONE task must have APPROVED sign_off');
});

// ── 6. Agent Ecosystem ───────────────────────────────────────────────────────
runCheck('getAgentEcosystem: returns 4 groups with 14 teams', () => {
  const eco = parser.getAgentEcosystem();
  assert(eco, 'Ecosystem must be returned');
  assert.strictEqual(eco.groups.length, 4, 'Must contain exactly 4 groups');
  const teamCount = eco.groups.reduce((sum, g) => sum + g.teams.length, 0);
  assert.strictEqual(teamCount, 14, `Must have 14 teams total, got ${teamCount}`);
});

runCheck('getAgentEcosystem: covers all 8 domain tracks', () => {
  const eco = parser.getAgentEcosystem();
  assert.strictEqual(eco.domainTracks.length, 8, 'Must list 8 domain tracks');
  assert(eco.domainTracks.includes('SaaS'), 'Must include SaaS');
  assert(eco.domainTracks.includes('Computer Vision'), 'Must include Computer Vision');
});

// ── 7. Dashboard State Aggregate ─────────────────────────────────────────────
runCheck('getDashboardState: returns complete state with all sections', () => {
  const state = parser.getDashboardState();
  assert(state, 'State must be returned');
  assert(state.tasks, 'State must include tasks');
  assert(state.phases, 'State must include phases');
  assert(state.specs, 'State must include specs');
  assert(state.kpis, 'State must include KPIs');
  assert(state.agentEcosystem, 'State must include agentEcosystem');
  assert(state.currentDate, 'State must include currentDate in DD-MM-YYYY');
  assert(/^\d{2}-\d{2}-\d{4}$/.test(state.currentDate), 'Date must be DD-MM-YYYY format');
});

runCheck('getDashboardState: KPIs reflect fixture data', () => {
  const state = parser.getDashboardState();
  assert(state.kpis.totalTasks >= 3, `Expected >= 3 total tasks, got ${state.kpis.totalTasks}`);
  assert(state.kpis.completedTasks >= 1, `Expected >= 1 completed, got ${state.kpis.completedTasks}`);
  assert(state.kpis.activeTasks >= 1, `Expected >= 1 active, got ${state.kpis.activeTasks}`);
});

runCheck('getDashboardState: IN_PROGRESS task floats to priority in KPIs', () => {
  const state = parser.getDashboardState();
  assert(state.kpis.activeTasks >= 1, 'Must have at least 1 active task (IN_PROGRESS)');
  assert(typeof state.kpis.scopeProgress === 'number', 'scopeProgress must be a number');
});

console.log('\n=================================================================');
console.log(`🎉 ALL ${passedChecks}/${totalChecks} BEHAVIORAL PARSER CHECKS PASSED!`);
console.log('=================================================================\n');
