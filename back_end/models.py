import enum
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Enum, ForeignKey, TIMESTAMP, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Company(Base):
  __tablename__ = 'company'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  address = Column(String)

class PotentialCustomer(Base):
  __tablename__ = 'potential_customer'
  id = Column(Integer, primary_key=True, index=True)
  score = Column(Integer)
  address = Column(String)
  customer_name = Column(String)
  created_date = Column(TIMESTAMP)
  potential_income = Column(Float)
  house_value = Column(Float)
  company_id = Column(Integer, ForeignKey("company.id"))

  company = relationship('Company', foreign_keys=[company_id])

class Schedule(Base):
  __tablename__ = 'schedule'
  id = Column(Integer, primary_key=True, index=True)
  customer_location = Column(String)
  date_created = Column(TIMESTAMP)
  schedule_date = Column(DateTime)
  potential_customer_id = Column(Integer, ForeignKey('potential_customer.id'))
  company_employee_id = Column(Integer, ForeignKey('company_employee.id'))

  potential_customer = relationship('PotentialCustomer', foreign_keys=[potential_customer_id])
  company_employee = relationship('CompanyEmployee', foreign_keys=[company_employee_id])

class RolesEnum(enum.Enum):
  admin = "Admin"
  user = "User"

class CompanyEmployee(Base):
  __tablename__ = 'company_employee'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  address = Column(String),
  roles = Column(Enum(RolesEnum))
  company_id = Column(Integer, ForeignKey('company.id'))
  schedule_id = Column(Integer, ForeignKey('schedule.id'))


  company = relationship('Company', foreign_keys=[company_id])
  schedule = relationship('Schedule', foreign_keys=[schedule_id])


