from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    question_text = Column(Text)
    answer_text = Column(Text)
    created_at = Column(DateTime)
