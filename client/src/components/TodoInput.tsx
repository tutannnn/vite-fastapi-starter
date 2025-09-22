import { useState } from "react";

interface TodoInputProps {
  onAdd: (text: string) => void;
  loading?: boolean;
}

export const TodoInput = ({ onAdd, loading = false }: TodoInputProps) => {
  const [text, setText] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!text.trim()) return;
    onAdd(text.trim());
    setText("");
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="fixed bottom-0 left-0 right-0 bg-gray-900 p-4 border-t border-gray-700 flex justify-center"
    >
      <div className="flex w-full max-w-2xl gap-2">
        <input
          type="text"
          className="flex-1 px-4 py-2 rounded-md border border-gray-600 bg-gray-800 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="Add a new todo..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          maxLength={30}
        />
        <button
          type="submit"
          disabled={!text.trim() || loading}
          className="px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 disabled:bg-gray-500 disabled:cursor-not-allowed"
        >
          {loading ? "..." : "Send"}
        </button>
      </div>
    </form>
  );
};
