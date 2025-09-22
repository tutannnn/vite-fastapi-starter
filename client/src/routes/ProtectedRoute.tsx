import { Navigate } from "react-router";
import { useAuth } from "../hooks/useAuth";
import { Spinner } from "../components/Spinner";
import type { JSX } from "react";

interface ProtectedRouteProps {
  children: JSX.Element;
}

export const ProtectedRoute = ({ children }: ProtectedRouteProps) => {
  const { user, loading } = useAuth();

  if (loading) return <Spinner />;

  if (!user) {
    return <Navigate to="/" replace />;
  }

  return children;
};
