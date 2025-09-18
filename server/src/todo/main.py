from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from todo.api.v1 import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router.router, prefix="/api/v1/todos", tags=["todos"])
