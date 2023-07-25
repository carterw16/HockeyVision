

export const usePlaceholder = ({
  loading,
  error,
  ...rest
}) => {
  const placeholder = !!loading
    ? "Loading..." 
    : !!error
    ? "error"
    : undefined;
  return {placeholder, loading, error, ...rest}
}