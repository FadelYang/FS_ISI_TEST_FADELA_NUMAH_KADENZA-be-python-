from fastapi import FastAPI
from app.controllers import todo_controller

app = FastAPI()

app.include_router( todo_controller.router, prefix="/api/v1")

@app.get("/")
def read_root():
	return {"message": "Hello from FastAPI in Docker"}
