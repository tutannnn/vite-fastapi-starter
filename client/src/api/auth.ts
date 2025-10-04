/**
 *  Authentication API module.
 * 
 * @note
 * This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
 * It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
 */

import type { User, SignupInput, LoginInput } from "../types/auth";
import { API_BASE } from "../config/api";
import { fetchJson } from "../utils/http";
import { buildHeaders } from "../utils/headers";

const AUTH_ENDPOINT = `${API_BASE}/auth`;

/**
 * Registers a new user.
 *
 * @param signupInput - User registration details (e.g., username).
 * @returns A `User` object representing the newly created user.
 */
export const signup = async (signupInput: SignupInput): Promise<User> => {
  return fetchJson<User>(`${AUTH_ENDPOINT}/signup`, {
    method: "POST",
    headers: buildHeaders(),
    body: JSON.stringify(signupInput),
  });
};

/**
 * Logs in an existing user.
 *
 * @param loginInput - User login credentials (e.g., username).
 * @returns A `User` object if the user exists in the database.
 */
export const login = async (loginInput: LoginInput): Promise<User> => {
  return fetchJson<User>(`${AUTH_ENDPOINT}/login`, {
    method: "POST",
    headers: buildHeaders(),
    body: JSON.stringify(loginInput),
  });
};

/**
 * Returns the currently authenticated user.
 *
 * @param userId The ID of the user to authenticate.
 * @returns A `User` object representing the authenticated user.
 */
export const getMe = async (userId: string): Promise<User> => {
  return fetchJson<User>(`${AUTH_ENDPOINT}/me`, {
    method: "GET",
    headers: buildHeaders(userId),
  });
};
