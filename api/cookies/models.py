from uuid import uuid4

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime

from main.models import Base


def generate_uuid():
   return str(uuid4())


class Fortune(Base):
    """
    Holds the message (fortune) inside the fortune cookie.
    """
    __tablename__ = 'Fortune'
    
    id = Column(Integer, primary_key=True)
    uuid = Column(String, unique=True, default=generate_uuid)
    message = Column(String)
    pub_date = Column(DateTime(timezone=True), default=func.now())
