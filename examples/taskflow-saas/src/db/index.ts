import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { DatabaseSync } from 'node:sqlite';
import type { CreateTaskInput, TaskRecord, TaskStatus } from '@/lib/contracts';

const DEFAULT_DB_PATH = path.resolve(process.cwd(), 'data', 'taskflow.db');

export class TaskStore {
  private db: DatabaseSync;

  constructor(dbPath: string = process.env.TASKFLOW_DB_PATH || DEFAULT_DB_PATH) {
    if (dbPath !== ':memory:') {
      fs.mkdirSync(path.dirname(dbPath), { recursive: true });
    }
    this.db = new DatabaseSync(dbPath);
    this.db.exec(`
      CREATE TABLE IF NOT EXISTS tasks (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'BACKLOG',
        priority TEXT NOT NULL DEFAULT 'P2',
        owner TEXT NOT NULL DEFAULT 'developer',
        created_at TEXT NOT NULL
      );
    `);
    this.seedIfEmpty();
  }

  private seedIfEmpty(): void {
    const row = this.db.prepare('SELECT COUNT(*) as count FROM tasks').get() as { count: number };
    if (row.count === 0) {
      const insert = this.db.prepare(
        'INSERT INTO tasks (id, title, status, priority, owner, created_at) VALUES (?, ?, ?, ?, ?, ?)'
      );
      const now = new Date().toISOString();
      insert.run('TASK-001', 'Phase 2: Verify Sprint Board Sensory Demo (:3000)', 'DONE', 'P1', 'lead', now);
      insert.run('TASK-002', 'Phase 3: Lock FEAT-001 Zod & SQLite Contracts', 'IN_PROGRESS', 'P0', 'developer', now);
      insert.run('TASK-003', 'Phase 4: Run Vitest TDD & Security Audit Gate', 'BACKLOG', 'P2', 'developer', now);
    }
  }

  listTasks(): TaskRecord[] {
    const rows = this.db
      .prepare('SELECT id, title, status, priority, owner, created_at as createdAt FROM tasks ORDER BY created_at DESC')
      .all() as unknown as TaskRecord[];
    return rows;
  }

  createTask(input: CreateTaskInput): TaskRecord {
    const id = `TASK-${crypto.randomBytes(3).toString('hex').toUpperCase()}`;
    const createdAt = new Date().toISOString();
    this.db
      .prepare('INSERT INTO tasks (id, title, status, priority, owner, created_at) VALUES (?, ?, ?, ?, ?, ?)')
      .run(id, input.title, 'BACKLOG', input.priority, input.owner, createdAt);
    return {
      id,
      title: input.title,
      status: 'BACKLOG',
      priority: input.priority,
      owner: input.owner,
      createdAt,
    };
  }

  updateTaskStatus(id: string, status: TaskStatus): TaskRecord | null {
    const result = this.db.prepare('UPDATE tasks SET status = ? WHERE id = ?').run(status, id);
    if (result.changes === 0) return null;
    const updated = this.db
      .prepare('SELECT id, title, status, priority, owner, created_at as createdAt FROM tasks WHERE id = ?')
      .get(id) as unknown as TaskRecord | undefined;
    return updated ?? null;
  }

  close(): void {
    this.db.close();
  }
}

let sharedStore: TaskStore | null = null;

export function getTaskStore(): TaskStore {
  if (!sharedStore) {
    sharedStore = new TaskStore();
  }
  return sharedStore;
}
