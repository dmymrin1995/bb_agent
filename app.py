from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from crud import get_all_employees
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date
from populate import populate_from_csv

# Инициализация базы данных
Base.metadata.create_all(bind=engine)

# Инициализация приложения
app = FastAPI()

# Подключение к базе данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# populate_from_csv(SessionLocal(), './tables/employees.csv')


# Pydantic-модель для отображения сотрудников
class EmployeeOut(BaseModel):
    tnum: int
    full_name: str
    hire_date: date
    phone_number: str
    email: EmailStr
    gender: Optional[str] = None
    birth_date: Optional[date] = None
    hobbies: Optional[str] = None

    class Config:
        orm_mode = True

# GET маршрут для получения всех сотрудников
@app.get("/employees/", response_model=List[EmployeeOut])
def read_employees(db: Session = Depends(get_db)):
    employees = get_all_employees(db)
    return employees
