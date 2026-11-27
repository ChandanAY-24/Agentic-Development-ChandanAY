import { describe, expect, it } from 'vitest';
import { CreateTaskSchema } from '@/lib/contracts';
import { TaskStore } from '@/db';

describe('FEAT-001: Sprint Task Board & Persistence', () => {
  it('TEST-FEAT001-01 / AC-FEAT001-01: creates and persists a valid task in SQLite', () => {
    const store = new TaskStore(':memory:');
    try {
      const created = store.createTask({
        title: 'Implement OAuth callback',
        priority: 'P1',
        owner: 'chandan',
      });
      expect(created.id).toMatch(/^TASK-[A-F0-9]+$/);
      expect(created.status).toBe('BACKLOG');
      expect(created.priority).toBe('P1');

      const all = store.listTasks();
      expect(all.some((t) => t.id === created.id && t.title === 'Implement OAuth callback')).toBe(true);
    } finally {
      store.close();
    }
  });

  it('TEST-FEAT001-02 / AC-FEAT001-02: rejects empty or whitespace-only task payloads', () => {
    const empty = CreateTaskSchema.safeParse({ title: '   ', priority: 'P1' });
    expect(empty.success).toBe(false);

    const badPriority = CreateTaskSchema.safeParse({ title: 'Valid task', priority: 'P9' });
    expect(badPriority.success).toBe(false);
  });
});
