from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from api.database import Base
from datetime import datetime
from typing import List
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

class Book(Base):
    __tablename__ = "book"

    id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)

user_role = Table(
    "user_role",
    Base.metadata,
    Column("user_id", UUID(as_uuid=True), ForeignKey("user.id"), primary_key=True),
    Column("role_id", UUID(as_uuid=True), ForeignKey("role.id"), primary_key=True)
)

class Role(Base):
    __tablename__ = "role"

    id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    
class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(35), nullable=False)
    attempt = Column(Integer, default=0)
    active = Column(Boolean, default=True)
    secret = Column(String(150))
    start_datetime = Column(DateTime, default=datetime.utcnow)

    roles = relationship("Role", secondary=user_role, back_populates="users")