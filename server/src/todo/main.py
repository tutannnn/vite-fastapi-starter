"""Todo application entrypoint."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from todo.api.v1.routes.todo import router as todo_router


def _configure_cors(app: FastAPI) -> None:
    """Adds CORS middleware to the app.

    Args:
        app (FastAPI): App instance.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # TODO: Allow all origins in dev.
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def _register_routes(app: FastAPI) -> None:
    """Registers API routers with the app.

    Args:
        app (FastAPI): App instance.
    """
    app.include_router(todo_router, prefix="/api/v1/todo", tags=["todo"])


def create_app() -> FastAPI:
    """Returns a configured app instance.

    Returns:
        FastAPI: Configured app instance.
    """
    app = FastAPI()
    _configure_cors(app)
    _register_routes(app)
    return app


app = create_app()
