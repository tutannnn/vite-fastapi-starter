"use client";

/**
 * NOTE: This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
 * It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
 */

import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { login, signup, getMe } from "../api/auth";
import {
  getStoredUserId,
  storeUserId,
  clearStoredUserId,
} from "../utils/localStorage";

const QUERY_KEY = ["auth", "me"];

export function useAuth() {
  const queryClient = useQueryClient();
  const userId = getStoredUserId();

  const {
    data: user,
    error,
    isLoading: loading,
  } = useQuery({
    queryKey: QUERY_KEY,
    queryFn: () => getMe(userId!),
    enabled: !!userId,
    staleTime: Infinity,
    retry: false,
  });

  const signupMutation = useMutation({
    mutationFn: signup,
    onSuccess: (res) => {
      if (res) {
        storeUserId(res.id);
        queryClient.setQueryData(QUERY_KEY, res);
      }
    },
  });

  const loginMutation = useMutation({
    mutationFn: login,
    onSuccess: (res) => {
      if (res) {
        storeUserId(res.id);
        queryClient.setQueryData(QUERY_KEY, res);
      }
    },
  });

  const logout = () => {
    clearStoredUserId();
    queryClient.removeQueries({ queryKey: QUERY_KEY });
  };

  return {
    user,
    loading,
    error: error instanceof Error ? error.message : null,
    signup: signupMutation,
    login: loginMutation,
    logout,
  };
}
