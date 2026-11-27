import { describe, expect, it } from 'vitest';
import { createSessionToken, verifySessionToken } from '@/lib/auth';
import { TaskStore } from '@/db';

describe('FEAT-001 & FEAT-002: Auth Session & Task Status Transitions', () => {
  it('TEST-FEAT001-03 / AC-FEAT001-03: transitions task status across BACKLOG -> IN_PROGRESS -> DONE', () => {
    const store = new TaskStore(':memory:');
    try {
      const created = store.createTask({ title: 'Ship v1.0', priority: 'P0', owner: 'lead' });
      const inProgress = store.updateTaskStatus(created.id, 'IN_PROGRESS');
      expect(inProgress?.status).toBe('IN_PROGRESS');

      const done = store.updateTaskStatus(created.id, 'DONE');
      expect(done?.status).toBe('DONE');
    } finally {
      store.close();
    }
  });

  it('TEST-FEAT002-01 / AC-FEAT002-01: signs and verifies valid HMAC session tokens', () => {
    const token = createSessionToken('chandan', 'lead', 600);
    const verified = verifySessionToken(token);
    expect(verified).not.toBeNull();
    expect(verified?.userId).toBe('chandan');
    expect(verified?.role).toBe('lead');
  });

  it('TEST-FEAT002-02 / AC-FEAT002-02: rejects missing or tampered session tokens', () => {
    expect(verifySessionToken(null)).toBeNull();
    expect(verifySessionToken('invalid.token')).toBeNull();

    const token = createSessionToken('chandan', 'developer', 600);
    const tampered = `${token.slice(0, -4)}AAAA`;
    expect(verifySessionToken(tampered)).toBeNull();
  });
});
