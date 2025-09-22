import * as z from "zod";

const Env = z.object({
  VITE_API_BASE: z.string().url().default("http://localhost:8000/api/v1"),
});

const env = Env.parse(import.meta.env);

export const API_BASE = env.VITE_API_BASE;
