import { useAuth } from "../hooks/useAuth";
import { useTodos } from "../hooks/useTodos";
import { TodoItem } from "../components/TodoItem";
import { TodoInput } from "../components/TodoInput";
import { Spinner } from "../components/Spinner";
import { Link, useNavigate } from "react-router";

const TodoPage = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const { todos, isLoading, error, addTodo, removeTodo } = useTodos(user!.id);

  const handleLogout = () => {
    logout();
    navigate("/");
  };

  return (
    <div className="flex flex-col h-screen bg-gray-900">
      <header className="fixed top-0 left-0 right-0 flex justify-between items-center text-white bg-gray-900 z-30 px-4 h-16 border-b border-gray-700">
        <span className="font-bold text-2xl">
          Welcome {user!.username}! Here are your todos:
        </span>
        <Link
          to="/"
          className="hover:underline font-semibold"
          onClick={handleLogout}
        >
          Log out
        </Link>
      </header>
      <div className="h-16" />
      <div className="flex-1 overflow-y-auto px-4 flex flex-col-reverse items-center h-16">
        <div className="w-full max-w-2xl flex flex-col gap-2 py-4 pb-20">
          {isLoading && <Spinner />}
          {error && <p className="text-red-500">Error loading todos</p>}
          {todos?.map((todo) => (
            <TodoItem key={todo.id} todo={todo} onDelete={removeTodo.mutate} />
          ))}
        </div>
      </div>
      <footer className="border-t border-gray-700 bg-gray-900 z-20">
        <TodoInput onAdd={addTodo.mutate} />
      </footer>
    </div>
  );
};

export default TodoPage;
