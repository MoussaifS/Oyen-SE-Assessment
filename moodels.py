from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id= Column(Integer,primary_key = True , index = True)
    name = Column(String, unique=True , index = True)
    password = Column(String)
    animal_type = Column(String,index = True)

    