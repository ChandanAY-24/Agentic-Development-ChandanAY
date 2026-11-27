'use client';

import { useEffect, useState } from 'react';
import type { TaskPriority, TaskRecord, TaskStatus } from '@/lib/contracts';

const COLUMNS: { status: TaskStatus; label: string; accent: string }[] = [
  { status: 'BACKLOG', label: 'Backlog', accent: 'border-zinc-700' },
  { status: 'IN_PROGRESS', label: 'In Progress', accent: 'border-sky-500/50' },
  { status: 'DONE', label: 'Done', accent: 'border-emerald-500/50' },
];

const PRIORITY_BADGE: Record<TaskPriority, string> = {
  P0: 'bg-rose-500/15 text-rose-300 border-rose-500/30',
  P1: 'bg-amber-500/15 text-amber-300 border-amber-500/30',
  P2: 'bg-sky-500/15 text-sky-300 border-sky-500/30',
  P3: 'bg-zinc-500/15 text-zinc-300 border-zinc-500/30',
};

export default function HomePage() {
  const [tasks, setTasks] = useState<TaskRecord[]>([]);
  const [session, setSession] = useState<{ userId: string; role: string } | null>(null);
  const [title, setTitle] = useState('');
  const [priority, setPriority] = useState<TaskPriority>('P1');
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  async function refresh() {
    const [tRes, aRes] = await Promise.all([fetch('/api/tasks'), fetch('/api/auth')]);
    const tData = (await tRes.json()) as { tasks: TaskRecord[] };
    const aData = (await aRes.json()) as { authenticated: boolean; session: { userId: string; role: string } | null };
    setTasks(tData.tasks);
    setSession(aData.session);
    setLoading(false);
  }

  useEffect(() => {
    void refresh();
  }, []);

  async function handleSignIn() {
    setError(null);
    await fetch('/api/auth', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ userId: 'chandan', role: 'lead' }),
    });
    await refresh();
  }

  async function handleSignOut() {
    await fetch('/api/auth', { method: 'DELETE' });
    await refresh();
  }

  async function handleCreate(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    const res = await fetch('/api/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, priority, owner: session?.userId || 'developer' }),
    });
    if (!res.ok) {
      const data = (await res.json()) as { error?: string };
      setError(data.error || 'Failed to create task');
      return;
    }
    setTitle('');
    await refresh();
  }

  async function moveTask(id: string, status: TaskStatus) {
    setError(null);
    const res = await fetch('/api/tasks', {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, status }),
    });
    if (!res.ok) {
      const data = (await res.json()) as { error?: string };
      setError(data.error || 'Failed to update task');
      return;
    }
    await refresh();
  }

  return (
    <main className="mx-auto max-w-6xl px-6 py-10">
      <header className="mb-8 flex flex-wrap items-center justify-between gap-4 border-b border-zinc-800 pb-6">
        <div>
          <span className="inline-flex items-center rounded-full border border-indigo-500/30 bg-indigo-500/10 px-3 py-1 text-xs font-medium text-indigo-300">
            SDD-Vibe 1-in-2 Reference App
          </span>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight text-white">TaskFlow SaaS</h1>
          <p className="mt-1 text-sm text-zinc-400">
            Next.js App Router · TypeScript · Tailwind CSS · Zod · SQLite · HMAC Auth
          </p>
        </div>

        <div className="flex items-center gap-3">
          {session ? (
            <>
              <span className="rounded-lg border border-emerald-500/30 bg-emerald-500/10 px-3 py-1.5 text-xs text-emerald-300">
                Signed in as <strong>{session.userId}</strong> ({session.role})
              </span>
              <button
                onClick={handleSignOut}
                className="rounded-lg border border-zinc-700 bg-zinc-900 px-3 py-1.5 text-xs font-medium text-zinc-200 hover:bg-zinc-800"
              >
                Sign out
              </button>
            </>
          ) : (
            <button
              onClick={handleSignIn}
              className="rounded-lg bg-indigo-600 px-4 py-2 text-xs font-semibold text-white hover:bg-indigo-500"
            >
              Demo Sign In (Lead)
            </button>
          )}
        </div>
      </header>

      <section className="mb-8 rounded-xl border border-zinc-800 bg-zinc-900/60 p-4">
        <form onSubmit={handleCreate} className="flex flex-wrap items-center gap-3">
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Add a sprint task (requires sign-in)..."
            className="min-w-64 flex-1 rounded-lg border border-zinc-700 bg-zinc-950 px-3 py-2 text-sm text-zinc-100 placeholder-zinc-500 focus:border-indigo-500 focus:outline-none"
          />
          <select
            value={priority}
            onChange={(e) => setPriority(e.target.value as TaskPriority)}
            className="rounded-lg border border-zinc-700 bg-zinc-950 px-3 py-2 text-sm text-zinc-100"
          >
            <option value="P0">P0 · Critical</option>
            <option value="P1">P1 · High</option>
            <option value="P2">P2 · Medium</option>
            <option value="P3">P3 · Low</option>
          </select>
          <button
            type="submit"
            className="rounded-lg bg-zinc-100 px-4 py-2 text-sm font-semibold text-zinc-950 hover:bg-white"
          >
            Create Task
          </button>
        </form>
        {error && <p className="mt-2 text-xs text-rose-400">{error}</p>}
      </section>

      {loading ? (
        <p className="text-sm text-zinc-400">Loading sprint board...</p>
      ) : (
        <section className="grid gap-6 md:grid-cols-3">
          {COLUMNS.map((col) => {
            const colTasks = tasks.filter((t) => t.status === col.status);
            return (
              <div key={col.status} className={`rounded-xl border ${col.accent} bg-zinc-900/40 p-4`}>
                <div className="mb-4 flex items-center justify-between">
                  <h2 className="text-sm font-semibold text-zinc-200">{col.label}</h2>
                  <span className="rounded-full bg-zinc-800 px-2 py-0.5 text-xs text-zinc-400">{colTasks.length}</span>
                </div>
                <div className="space-y-3">
                  {colTasks.map((t) => (
                    <article key={t.id} className="rounded-lg border border-zinc-800 bg-zinc-950 p-3">
                      <div className="mb-2 flex items-center justify-between gap-2">
                        <span className="font-mono text-xs text-zinc-500">{t.id}</span>
                        <span className={`rounded border px-1.5 py-0.5 text-[11px] font-medium ${PRIORITY_BADGE[t.priority]}`}>
                          {t.priority}
                        </span>
                      </div>
                      <p className="text-sm font-medium text-zinc-100">{t.title}</p>
                      <div className="mt-3 flex flex-wrap gap-1.5">
                        {COLUMNS.filter((c) => c.status !== t.status).map((target) => (
                          <button
                            key={target.status}
                            onClick={() => void moveTask(t.id, target.status)}
                            className="rounded border border-zinc-800 bg-zinc-900 px-2 py-1 text-[11px] text-zinc-300 hover:border-zinc-700 hover:text-white"
                          >
                            → {target.label}
                          </button>
                        ))}
                      </div>
                    </article>
                  ))}
                </div>
              </div>
            );
          })}
        </section>
      )}
    </main>
  );
}
