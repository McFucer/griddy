import uuid as uuid
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Boolean
from sqlalchemy.orm import relationship

from db import Base

from datetime import datetime
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String)
    password = Column(Integer)
    comments = relationship("Comment", back_populates="user")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="comments")


class Comment_Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String, unique=True)
    file_path = Column(String)
    comment_id = Column(Integer, ForeignKey("comments.id"))
    comment = relationship("Comment", back_populates="image_comments")

from datetime import datetime



class AdminModel(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    born = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=func.utcnow())
    phone_number = Column(String, nullable=False)
    gmail = Column(String, nullable=False)
    password = Column(String, nullable=False)
    country = Column(String, default="UZB")
    region = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)



