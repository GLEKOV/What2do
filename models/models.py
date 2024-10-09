from datetime import datetime
from db import Base
from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, Table, Column, JSON



class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, unique=True, index=True,  nullable=False, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    body = Column(String)
    
    
    
class Roles(Base):
    __tablename__ = "roles",
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)



class Users(Base):
    __tablename__ =  "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    registrated_at = Column(TIMESTAMP, default=datetime.now)
    roleid = Column(Integer, ForeignKey("roles.id"))


