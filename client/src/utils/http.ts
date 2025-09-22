const handleResponse = async <T>(resp: Response): Promise<T> => {
  const json = await resp.json();

  if (!resp.ok) {
    const message = json?.detail || "Request failed";
    throw new Error(message);
  }

  return json;
};

export const fetchJson = async <T>(
  url: string,
  options?: RequestInit,
): Promise<T> => {
  const resp = await fetch(url, options);
  return handleResponse<T>(resp);
};
