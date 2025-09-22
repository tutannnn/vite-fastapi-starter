"use client";

/**
 * @note
 * This dev-only implementation uses header-based "Bearer <user_id>" auth and minimal identity checks.
 * It is intentionally designed to be replaced with production-ready authentication (e.g., Auth0, OAuth2, JWT).
 */

import { useState } from "react";
import { Link, useNavigate } from "react-router";

import { InputField } from "../components/InputField";
import { Button } from "../components/Button";
import { useAuth } from "../hooks/useAuth";

const SignupPage = () => {
  const { signup } = useAuth();

  const [username, setUsername] = useState("");
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const handleSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    try {
      await signup.mutateAsync({ username: username });
      navigate("/todo");
    } catch (err: any) {
      setError(err?.message || "Signup failed.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col justify-center px-6 py-12 bg-gray-900">
      <div className="sm:mx-auto sm:w-full sm:max-w-md text-center">
        <h2 className="text-3xl font-extrabold text-white">
          Create your account
        </h2>
      </div>

      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md bg-gray-800 p-8 rounded-lg shadow-lg">
        <form onSubmit={handleSignup} className="space-y-6">
          <InputField
            label="Username"
            value={username}
            onChange={setUsername}
          />

          {error && <p className="text-sm text-red-500 text-center">{error}</p>}

          <Button loading={signup.isPending} disabled={signup.isPending}>
            Create account
          </Button>
        </form>

        <p className="mt-6 text-center text-gray-400">
          Already have an account?{" "}
          <Link
            to="/login"
            className="font-semibold text-indigo-400 hover:text-indigo-300"
          >
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
};

export default SignupPage;
