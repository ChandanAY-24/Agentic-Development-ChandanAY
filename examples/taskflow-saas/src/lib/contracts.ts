import { z } from 'zod';

export const TaskStatusSchema = z.enum(['BACKLOG', 'IN_PROGRESS', 'DONE']);
export const TaskPrioritySchema = z.enum(['P0', 'P1', 'P2', 'P3']);

export const CreateTaskSchema = z.object({
  title: z.string().trim().min(1, 'Task title is required').max(120, 'Title must be 120 characters or fewer'),
  priority: TaskPrioritySchema.default('P2'),
  owner: z.string().trim().min(1).max(60).default('developer'),
});

export const UpdateTaskStatusSchema = z.object({
  id: z.string().trim().min(1, 'Task ID is required'),
  status: TaskStatusSchema,
});

export type TaskStatus = z.infer<typeof TaskStatusSchema>;
export type TaskPriority = z.infer<typeof TaskPrioritySchema>;
export type CreateTaskInput = z.infer<typeof CreateTaskSchema>;

export interface TaskRecord {
  id: string;
  title: string;
  status: TaskStatus;
  priority: TaskPriority;
  owner: string;
  createdAt: string;
}
