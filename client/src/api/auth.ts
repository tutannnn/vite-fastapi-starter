/**
 * NOTE: This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
 * It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
 */

import type { User, SignupInput, LoginInput } from "../types/auth";
import { API_BASE } from "../config/api";
import { fetchJson } from "../utils/http";

const defaultHeaders = {
  "Content-Type": "application/json",
};

export async function signup(signupInput: SignupInput): Promise<User> {
  return fetchJson<User>(`${API_BASE}/auth/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(signupInput),
  });
}

export async function login(loginInput: LoginInput): Promise<User> {
  return fetchJson<User>(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: defaultHeaders,
    body: JSON.stringify(loginInput),
  });
}

export async function getMe(userId: string): Promise<User> {
  return fetchJson<User>(`${API_BASE}/auth/me`, {
    method: "GET",
    headers: {
      ...defaultHeaders,
      Authorization: `Bearer ${userId}`,
    },
  });
}
