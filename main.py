from fastapi import FastAPI
from app.controllers import todo_controller
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router( todo_controller.router, prefix="/api/v1")

origins = ["*"]
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)

@app.get("/")
def read_root():
	return {"message": "Hello from FastAPI in Docker"}
