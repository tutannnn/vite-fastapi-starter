/**
 * Todo API module.
 */

import type { Todo, TodoInput } from "../types/todo";
import { API_BASE } from "../config/api";
import { fetchJson } from "../utils/http";
import { buildHeaders } from "../utils/headers";

const TODO_ENDPOINT = `${API_BASE}/todo`;

/**
 * Fetches all todos for a given user.
 *
 * @param userId - The ID of the user whose todos should be fetched.
 * @returns A list of `Todo` objects for the specified user.
 */
export const getTodos = async (userId: string): Promise<Todo[]> => {
  return fetchJson<Todo[]>(TODO_ENDPOINT, {
    headers: buildHeaders(userId),
  });
};

/**
 * Creates a new todo for a user.
 * 
 * @param todoInput - The new todo data, including the user ID and content.
 * @returns The created `Todo` object.
 */
export const createTodo = async (todoInput: TodoInput): Promise<Todo> => {
  return fetchJson<Todo>(TODO_ENDPOINT, {
    method: "POST",
    headers: buildHeaders(todoInput.userId),
    body: JSON.stringify(todoInput),
  });
};

/**
 * Deletes an existing todo.
 *
 * @param todo - The todo object to be deleted.
 */
export const deleteTodo = async (todo: Todo): Promise<null> => {
  return fetchJson<null>(`${TODO_ENDPOINT}/${todo.id}`, {
    method: "DELETE",
    headers: buildHeaders(todo.user_id),
  });
};
