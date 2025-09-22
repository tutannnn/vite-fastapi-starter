FROM ghcr.io/astral-sh/uv:alpine

WORKDIR /app

COPY . .

RUN uv venv --python 3.13

RUN uv pip install --no-cache-dir --upgrade -r pyproject.toml

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
