from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


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
    file_name = Column(String,unique=True,uuid=True)
    file_path = Column(String)
    comment_id = 
