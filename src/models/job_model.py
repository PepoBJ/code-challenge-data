from sqlalchemy import Column, String
from base_model import BaseModel

class Job(BaseModel):
    __tablename__ = 'jobs'

    job = Column(String(255))
