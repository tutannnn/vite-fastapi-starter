# vite-fastapi-starter

Full-stack too app to use as a template for projects using Python, FastAPI, SQLAlchemy, Typescript, React, Vite,
Tailwind, and a PostgreSQL database!

---

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running via Docker](#running-via-docker)
  - [Running in Development](#running-in-development)
- [Linting and Testing](#linting-and-testing)
- [License](#license)

---

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) for containerization
- [PostgreSQL](https://www.postgresql.org/) (running locally or via Docker)
- [uv](https://docs.astral.sh/uv/) for managing virtual environments, dependencies, and server builds
- [Python 3.13](https://www.python.org/downloads/) for development
- [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html) for running database migrations

---

### Running via Docker

1. Clone the repo

```bash
git clone git@github.com:pfischer1687/vite-fastapi-starter.git
cd vite-fastapi-starter
```

2. Start the Docker containers (DB, server, and client)

```bash
docker compose up
```

3. Enter `localhost:3000` in your browser

---

### Running in Development

1. Compose the Postgres DB

```bash
docker compose up db
```

2. Set up Python virtual environment

```bash
cd server
uv venv --python 3.13
source .venv/bin/activate
pip install -r pyproject.toml --all-extras
```

3. Run the database migration via Alembic

```bash
cd server/src/todo
uv run alembic upgrade head
```

If you want to generate your own migrations after updating the DB models:

```bash
alembic revision --autogenerate -m "<COMMIT_MSG>"
```

4. Start the server

```bash
uv run fastapi dev src/todo/main.py
```

5. Set up the client

```bash
cd client
npm install
npm run dev
```

6. Open `localhost:3000` in a browser

---

## Linting and Testing

You can lint the client with:

```bash
npx prettier . --write
```

and you can lint, format, and type check the server with:

```bash
uv run pre-commit run --all-files
```

and you can run the server's suite of unit tests with:

```bash
uv run pytest -s -vvv
```

---

## License

MIT License
