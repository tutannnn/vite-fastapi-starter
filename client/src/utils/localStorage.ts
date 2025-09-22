/**
 * @note
 * This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
 * It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
 */

const USER_ID_KEY = "user_id";

export const storeUserId = (userId: string): void => {
  localStorage.setItem(USER_ID_KEY, userId);
};

export const getStoredUserId = (): string | null => {
  return localStorage.getItem(USER_ID_KEY);
};

export const clearStoredUserId = (): void => {
  localStorage.removeItem(USER_ID_KEY);
};
