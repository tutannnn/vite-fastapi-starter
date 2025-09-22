/**
 * @note
 * This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
 * It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
 */

export interface User {
  id: string;
  username: string;
}

export interface SignupInput {
  username: string;
}

export interface LoginInput {
  username: string;
}
