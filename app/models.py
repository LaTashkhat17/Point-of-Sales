from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)  # length specified
    hashed_password = Column(String(255))  # length specified
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
