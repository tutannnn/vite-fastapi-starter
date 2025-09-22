/**
 * @note
 * This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
 * It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
 */

export const buildHeaders = (userId?: String): Record<string, string> => {
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
  };

  if (userId) {
    headers.Authorization = `Bearer ${userId}`;
  }

  return headers;
};
