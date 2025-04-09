from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database import Base
from datetime import datetime, timezone

class Todo(Base):
  __tablename__ = "todos"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  is_completed = Column(Boolean, default=False)
  created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))