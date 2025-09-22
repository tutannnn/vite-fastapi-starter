import { Spinner } from "./Spinner";

interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  loading?: boolean;
}

export const Button = ({
  children,
  onClick,
  disabled = false,
  loading = false,
}: ButtonProps) => {
  return (
    <button
      onClick={onClick}
      disabled={disabled || loading}
      className={`w-full py-2 px-4 bg-indigo-600 text-white font-semibold rounded-md shadow hover:bg-indigo-700 disabled:bg-gray-400`}
    >
      {loading ? <Spinner /> : children}
    </button>
  );
};
