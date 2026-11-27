import { NextRequest, NextResponse } from 'next/server';
import { getServerSession } from '@/lib/auth';
import { CreateTaskSchema, UpdateTaskStatusSchema } from '@/lib/contracts';
import { getTaskStore } from '@/db';

export async function GET(): Promise<NextResponse> {
  const tasks = getTaskStore().listTasks();
  return NextResponse.json({ tasks });
}

export async function POST(req: NextRequest): Promise<NextResponse> {
  const session = await getServerSession();
  if (!session) {
    return NextResponse.json({ error: 'Unauthorized: sign in required' }, { status: 401 });
  }

  const body = await req.json().catch(() => null);
  const parsed = CreateTaskSchema.safeParse(body);
  if (!parsed.success) {
    return NextResponse.json({ error: 'Validation failed', issues: parsed.error.flatten() }, { status: 400 });
  }

  const task = getTaskStore().createTask({
    ...parsed.data,
    owner: parsed.data.owner || session.userId,
  });
  return NextResponse.json({ task }, { status: 201 });
}

export async function PATCH(req: NextRequest): Promise<NextResponse> {
  const session = await getServerSession();
  if (!session) {
    return NextResponse.json({ error: 'Unauthorized: sign in required' }, { status: 401 });
  }

  const body = await req.json().catch(() => null);
  const parsed = UpdateTaskStatusSchema.safeParse(body);
  if (!parsed.success) {
    return NextResponse.json({ error: 'Validation failed', issues: parsed.error.flatten() }, { status: 400 });
  }

  const updated = getTaskStore().updateTaskStatus(parsed.data.id, parsed.data.status);
  if (!updated) {
    return NextResponse.json({ error: 'Task not found' }, { status: 404 });
  }
  return NextResponse.json({ task: updated });
}
