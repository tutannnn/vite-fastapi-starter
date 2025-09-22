"use client";

/**
 * NOTE: This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
 * It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
 */

import { useState } from "react";
import { Link, useNavigate } from "react-router";
import { InputField } from "../components/InputField";
import { Button } from "../components/Button";
import { useAuth } from "../hooks/useAuth";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [formError, setFormError] = useState<string | null>(null);
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setFormError(null);

    if (!username.trim()) {
      setFormError("Username is required.");
      return;
    }

    try {
      await login.mutateAsync({ username });
      navigate("/");
    } catch (error: any) {
      const message = error?.message || "Login failed. Please try again.";
      setFormError(message);
    }
  };

  return (
    <div className="min-h-screen flex flex-col justify-center px-6 py-12 bg-gray-900">
      <div className="sm:mx-auto sm:w-full sm:max-w-md text-center">
        <h2 className="text-3xl font-extrabold text-white">
          Sign in to your account
        </h2>
      </div>

      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md bg-gray-800 p-8 rounded-lg shadow-lg">
        <form onSubmit={handleLogin} className="space-y-6" noValidate>
          <InputField
            label="Username"
            value={username}
            onChange={setUsername}
            placeholder="Enter your username"
            error={formError ?? undefined}
          />

          <Button loading={login.isPending} disabled={login.isPending}>
            Sign In
          </Button>

          <p className="mt-6 text-center text-gray-400">
            Not a member?{" "}
            <Link
              to="/signup"
              className="font-semibold text-indigo-400 hover:text-indigo-300"
            >
              Create an account
            </Link>
          </p>
        </form>
      </div>
    </div>
  );
}
