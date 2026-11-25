const assert = require('assert');
const path = require('path');
const DashboardParser = require('../Project-Manager-Dashboard/parser');

const root = path.resolve(__dirname, '..');
const parser = new DashboardParser(root);

// 1. Verify 4-Group, 14-Team Agentic Ecosystem structure
const eco = parser.getAgentEcosystem();
assert.strictEqual(eco.enabledByDefault, true);
assert.strictEqual(eco.optionalDeveloperChoice, true);
assert.strictEqual(eco.groups.length, 4, 'Expected 4 ecosystem groups');

const totalTeams = eco.groups.reduce((sum, g) => sum + g.teams.length, 0);
assert.strictEqual(totalTeams, 14, 'Expected 14 specialized teams');

const group4 = eco.groups.find(g => g.id === 'Group 4');
const team12 = group4 && group4.teams.find(t => t.id === 'Team 12');
assert.ok(team12, 'Expected Team 12 in Group 4');
assert.ok(
  Array.isArray(team12.subAgents) && team12.subAgents.some(a => /Finance Management Agent/i.test(a)),
  'Expected Team 12 to define Finance Management Agent'
);

const requiredDomains = [
  'SaaS',
  'E-commerce',
  'Brand / Product / Service',
  'Software Development',
  'App Development',
  'ML / Deep Learning / Data Science',
  'Computer Vision',
  'Operating System Development'
];
for (const d of requiredDomains) {
  assert.ok(eco.domainTracks.includes(d), `Missing domain track: ${d}`);
}

// 2. Verify Google Sheet Kanban CSV export
const csv = parser.exportKanbanCsv([
  {
    id: 'TASK-001',
    group: 'Group 2',
    team: 'Team 4',
    title: 'Implement auth, RBAC & "API" gateway',
    status: 'IN_PROGRESS',
    startDate: '25-11-2026',
    stopDate: '',
    specRef: 'FEAT-001'
  }
]);
const lines = csv.trim().split('\n');
assert.strictEqual(lines[0], 'task_id,group,team,title,status,start_date,stop_date,sign_off,spec_ref');
assert.ok(lines[1].includes('"Implement auth, RBAC & ""API"" gateway"'), 'CSV escaping failed');

console.log('test_agent_ecosystem.js PASSED');
