/**
 * Reusable Button component.
 */

import { Spinner } from "./Spinner";

/**
 * Properties for the Button component.
 *
 * @property children - Child components of the button.
 * @property onClick - Optional click event handler.
 * @property disabled - Disables the button if true.
 * @property loading - If true, disables the button and shows a spinner.
 */
interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  loading?: boolean;
}

/**
 * Renders a styled button with optional loading and disabled states.
 *
 * @param props - See {@link ButtonProps}.
 * @returns A React button element with conditional rendering.
 */
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
      className={`
        w-full py-2 px-4 bg-indigo-600 text-white font-semibold rounded-md shadow hover:bg-indigo-700
        disabled:bg-gray-400
      `}
    >
      {loading ? <Spinner /> : children}
    </button>
  );
};
