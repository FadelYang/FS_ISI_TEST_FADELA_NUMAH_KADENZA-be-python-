from typing import Optional
from sqlalchemy.orm import Session
from app.repositories import todo_repository
from app.schemas.todo_schema import TodoCreate, TodoUpdate, TodoRead
from fastapi import HTTPException

def get_all_todos(db: Session, is_completed: Optional[bool] = None):
  return todo_repository.get_all(db, is_completed)

def create_todo(db: Session, data: TodoCreate):
  return todo_repository.create(db, data)

def update_todo(db: Session, todo_id, data: TodoUpdate):
  return todo_repository.update(db, todo_id, data)

def delete_todo(db: Session, todo_id: int):
  return todo_repository.delete(db, todo_id)
