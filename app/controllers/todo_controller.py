from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.todo_schema import TodoRead, TodoCreate, TodoUpdate
from app.services import todo_service

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=list[TodoRead])
def get_all(db: Session = Depends(get_db), is_completed: Optional[bool] = None):
  return todo_service.get_all_todos(db, is_completed)

@router.post("/", response_model=TodoRead)
def create_todo(todo_data: TodoCreate, db: Session = Depends(get_db)):
    return todo_service.create_todo(db, todo_data)

@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo_data: TodoUpdate, db: Session = Depends(get_db)):
    updated = todo_service.update_todo(db, todo_id, todo_data)
    if updated is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    deleted = todo_service.delete_todo(db, todo_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": f"Todo with ID {todo_id} has been deleted."}