#!/bin/sh

set -e

echo "Running migrations..."
cd /app/src/todo
uv run python -m alembic upgrade head

echo "Starting server..."
cd /app
exec uv run fastapi run src/todo/main.py --host 0.0.0.0 --port 8000
