import type { Todo, TodoInput } from "../types/todo";
import { API_BASE } from "../config/api";
import { fetchJson } from "../utils/http";
import { buildHeaders } from "../utils/headers";

const TODO_ENDPOINT = `${API_BASE}/todo`;

export const getTodos = async (userId: string): Promise<Todo[]> => {
  return fetchJson<Todo[]>(TODO_ENDPOINT, {
    headers: buildHeaders(userId),
  });
};

export const createTodo = async (todoInput: TodoInput): Promise<Todo> => {
  return fetchJson<Todo>(TODO_ENDPOINT, {
    method: "POST",
    headers: buildHeaders(todoInput.userId),
    body: JSON.stringify(todoInput),
  });
};

export const deleteTodo = async (todo: Todo): Promise<null> => {
  return fetchJson<null>(`${TODO_ENDPOINT}/${todo.id}`, {
    method: "DELETE",
    headers: buildHeaders(todo.user_id),
  });
};
