from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Greet(Base):
    __tablename__ = 'greet'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

