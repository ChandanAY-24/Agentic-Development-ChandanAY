import crypto from 'node:crypto';
import { cookies } from 'next/headers';

export type UserRole = 'lead' | 'developer';

export interface SessionPayload {
  userId: string;
  role: UserRole;
  exp: number;
}

export const SESSION_COOKIE_NAME = 'taskflow_session';

function getSecret(): string {
  return process.env.TASKFLOW_SESSION_SECRET || 'sdd-vibe-dev-secret-change-in-prod';
}

export function createSessionToken(userId: string, role: UserRole, ttlSeconds = 3600): string {
  const payload: SessionPayload = {
    userId,
    role,
    exp: Math.floor(Date.now() / 1000) + ttlSeconds,
  };
  const encoded = Buffer.from(JSON.stringify(payload), 'utf8').toString('base64url');
  const sig = crypto.createHmac('sha256', getSecret()).update(encoded).digest('base64url');
  return `${encoded}.${sig}`;
}

export function verifySessionToken(token: string | undefined | null): SessionPayload | null {
  if (!token || !token.includes('.')) return null;
  const [encoded, sig] = token.split('.', 2);
  if (!encoded || !sig) return null;

  const expectedSig = crypto.createHmac('sha256', getSecret()).update(encoded).digest('base64url');
  const sigBuf = Buffer.from(sig);
  const expBuf = Buffer.from(expectedSig);
  if (sigBuf.length !== expBuf.length || !crypto.timingSafeEqual(sigBuf, expBuf)) {
    return null;
  }

  try {
    const parsed = JSON.parse(Buffer.from(encoded, 'base64url').toString('utf8')) as SessionPayload;
    if (!parsed.userId || !parsed.role || typeof parsed.exp !== 'number') return null;
    if (parsed.exp < Math.floor(Date.now() / 1000)) return null;
    return parsed;
  } catch {
    return null;
  }
}

export async function getServerSession(): Promise<SessionPayload | null> {
  const store = await cookies();
  return verifySessionToken(store.get(SESSION_COOKIE_NAME)?.value);
}
