import type { Todo } from "../types/todo";

interface TodoItemProps {
  todo: Todo;
  onDelete: (todo: Todo) => void;
  loading?: boolean;
}

export const TodoItem = ({
  todo,
  onDelete,
  loading = false,
}: TodoItemProps) => {
  return (
    <div className="flex items-center justify-between p-4 bg-gray-800 rounded-md shadow mb-2">
      <p className="text-white flex-1 truncate">{todo.text}</p>
      <button
        onClick={() => onDelete(todo)}
        disabled={loading}
        className="ml-4 px-3 py-1 bg-red-600 text-white rounded-md hover:bg-red-700 disabled:bg-gray-500 disabled:cursor-not-allowed"
      >
        {loading ? "..." : "X"}
      </button>
    </div>
  );
};
