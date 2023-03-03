from enum import Enum
from pydantic import BaseModel
import datetime

class Company(BaseModel):
  name: str
  address: str

  class Config:
    orm_mode = True

class PotentialCustomer(BaseModel):
  score: int
  address: str
  customer_name: str
  created_date: datetime
  potential_income: float
  house_value: float
  company_id: int

  class Config:
    orm_mode = True

class Schedule(BaseModel):
  customer_loaction: str
  date_created: datetime
  scheduled_date: datetime
  potential_customer_id: int
  company_employee_id: int

  class Config:
    orm_mode = True

class RolesEnum(str, Enum):
  admin="Admin"
  user="User"

class CompanyEmployee(BaseModel):
  name: str
  address: str
  roles: RolesEnum
  company_id: int
  schedule_id: int

  class Config:
    orm_mode = True
    use_enum_values = True