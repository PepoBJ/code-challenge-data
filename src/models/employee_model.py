from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel

from .department_model import Department
from .job_model import Job

class Employee(BaseModel):
    __tablename__ = 'hired_employees'

    name = Column(String(255))
    hire_datetime = Column(DateTime)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=True)
    job_id = Column(Integer, ForeignKey('jobs.id'), nullable=True)

    department = relationship(Department)
    job = relationship(Job)
