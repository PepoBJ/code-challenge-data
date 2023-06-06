from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from base_model import BaseModel

from department import Department
from job import Job

class Employee(BaseModel):
    __tablename__ = 'hired_employees'

    name = Column(String(255))
    hire_datetime = Column(DateTime)
    department_id = Column(Integer, ForeignKey('departments.id'))
    job_id = Column(Integer, ForeignKey('jobs.id'))

    department = relationship(Department)
    job = relationship(Job)
