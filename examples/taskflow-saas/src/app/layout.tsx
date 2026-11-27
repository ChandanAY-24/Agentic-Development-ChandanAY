import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'TaskFlow SaaS — SDD-Vibe Reference App',
  description: 'Modern Next.js + TypeScript + Tailwind + SQLite + Vitest reference app built with SDD-Vibe.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark">
      <body className="min-h-screen bg-zinc-950 text-zinc-100 antialiased">{children}</body>
    </html>
  );
}
