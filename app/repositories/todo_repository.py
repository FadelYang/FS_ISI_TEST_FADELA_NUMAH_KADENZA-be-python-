import logging
from typing import Optional
from fastapi import HTTPException
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session
from app.models.todo_model import Todo
from app.schemas.todo_schema import TodoCreate, TodoUpdate

logger = logging.getLogger(__name__)

def get_all(db: Session, is_completed: Optional[bool] = None):
    try:
        query = db.query(Todo)

        if is_completed is True:
            query = query.filter(Todo.is_completed == True).order_by(asc(Todo.created_at))
            logger.info("Fetching all completed todos")
        elif is_completed is False:
            query = query.filter(Todo.is_completed == False).order_by(desc(Todo.created_at))
            logger.info("Fetching all not completed todos")
        else:
            logger.info("Fetching all todos")

        todos = query.all()
        return todos
    except Exception as e:
        logger.error(f"Failed to get todos: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get todos")

def update(db: Session, todo_id: int, data: TodoUpdate):
  try:
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    print(data)

    if not todo:
      raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")

    if data.title is not None:
        todo.title = data.title
    if data.is_completed is not None:
        todo.is_completed = data.is_completed

    db.commit()
    db.refresh(todo)
    logger.info(f"Sucess updated todo with id {todo.id}")
    return todo
  except Exception as e:
    logger.error(f"Error updating todo: {str(e)}")
    raise HTTPException(status_code=500, detail=f"Failed to update a todo: {str(e)}")

def delete(db: Session, todo_id: int):
  try:
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
      raise HTTPException(status_code=404, detail=f"Todo with id {todo_id} not found")

    db.delete(todo)
    db.commit()
    logger.info(f"Success deleted todo with id {todo.id}")
    return todo
  except Exception as e:
    logger.error(f"Error deleting todo: {str(e)}")
    raise HTTPException(status_code=500, detail="Failed to delete a todo")

def create(db: Session, todo_data: TodoCreate):
  try:
    todo = Todo(**todo_data.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    logger.info(f"Success create new todo with id {todo.id}")
    return todo
  except Exception as e:
    logger.error(f"Error creating todo: {str(e)}")
    raise HTTPException(status_code=500, detail="Failed to create todo")