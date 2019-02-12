# app/models/example.py

from .base import Base
from ..database import db

class Example(Base):

    __tablename__ = 'examples'

    description = db.Column(db.String(255), nullable=True, unique=False)
