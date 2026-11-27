import { NextRequest, NextResponse } from 'next/server';
import { z } from 'zod';
import {
  createSessionToken,
  getServerSession,
  SESSION_COOKIE_NAME,
} from '@/lib/auth';

const LoginSchema = z.object({
  userId: z.string().trim().min(1).max(40),
  role: z.enum(['lead', 'developer']).default('developer'),
});

export async function GET(): Promise<NextResponse> {
  const session = await getServerSession();
  return NextResponse.json({ authenticated: Boolean(session), session });
}

export async function POST(req: NextRequest): Promise<NextResponse> {
  const body = await req.json().catch(() => null);
  const parsed = LoginSchema.safeParse(body);
  if (!parsed.success) {
    return NextResponse.json({ error: 'Invalid login payload', issues: parsed.error.flatten() }, { status: 400 });
  }

  const token = createSessionToken(parsed.data.userId, parsed.data.role);
  const res = NextResponse.json({
    authenticated: true,
    session: { userId: parsed.data.userId, role: parsed.data.role },
  });
  res.cookies.set(SESSION_COOKIE_NAME, token, {
    httpOnly: true,
    sameSite: 'lax',
    path: '/',
    maxAge: 3600,
  });
  return res;
}

export async function DELETE(): Promise<NextResponse> {
  const res = NextResponse.json({ authenticated: false });
  res.cookies.delete(SESSION_COOKIE_NAME);
  return res;
}
