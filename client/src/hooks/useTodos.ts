import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { getTodos, createTodo, deleteTodo } from "../api/todo";
import type { Todo } from "../types/todo";

export const useTodos = (userId: string) => {
  const queryClient = useQueryClient();

  const {
    data: todos,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["todo", userId],
    queryFn: () => getTodos(userId),
    enabled: !!userId,
  });

  const addTodo = useMutation({
    mutationFn: (text: string) => createTodo({ userId, text }),
    onSuccess: () =>
      queryClient.invalidateQueries({ queryKey: ["todo", userId] }),
  });

  const removeTodo = useMutation({
    mutationFn: (todo: Todo) => deleteTodo(todo),
    onSettled: () =>
      queryClient.invalidateQueries({
        queryKey: ["todo", userId],
        refetchType: "active",
      }),
  });

  return { todos, isLoading, error, addTodo, removeTodo };
};
