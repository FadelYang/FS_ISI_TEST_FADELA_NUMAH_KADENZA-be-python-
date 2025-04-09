from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class TodoCreate(BaseModel):
  title: str
  is_completed: bool = False

class TodoRead(BaseModel):
  id: int
  title: str
  is_completed: bool
  created_at: datetime

  class Config:
    orm_mode = True

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    is_completed: Optional[bool] = None

    class Config:
      orm_mode = True
    
