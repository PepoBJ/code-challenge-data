from sqlalchemy import Column, String
from models.base_model import BaseModel

class Department(BaseModel):
    __tablename__ = 'departments'

    department = Column(String(255))
