from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Company(Base):
  __tablename__ = 'company'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  address = Column(String)

class Schedule(Base):
  __tablename__ = 'schedule'
  id = Column(Integer, primary_key=True, index=True)
  location = Column(String)
  date_created = Column(TIMESTAMP)
  schedule_date = Column(DateTime)
  potential_customer = Column(Integer, ForeignKey('potential_customer.id'))

class CompanyEmployee(Base):
  __tablename__ = 'company_employee'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  address = Column(String),
  company_id = Column(Integer, ForeignKey('company.id'))
  schedule_id = Column(Integer, ForeignKey('schedule.id'))

  company = relationship('Company')
  schedule = relationship('Schedule')


