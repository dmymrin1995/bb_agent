from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from crud import (
    get_all_employees, 
    get_all_relatives,
    get_employee_by_contact,
    get_relatives_by_employee_id)
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date
from populate import populate_from_csv, populate_relatives_from_csv

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

# populate_from_csv(SessionLocal(), "./tables/employees.csv")

# Заполнение таблицы родственников
# populate_relatives_from_csv(SessionLocal(), "./tables/relation.csv")



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

class RelativeOut(BaseModel):
    r_num: int
    tnum: int
    full_name: str
    gender: Optional[str] = None
    birth_date: Optional[date] = None
    relation_type: str

    class Config:
        orm_mode = True

class RelationsSearchResponse(BaseModel):
    message: dict


# GET маршрут для получения всех сотрудников
@app.get("/employees/all", response_model=List[EmployeeOut])
def read_employees(db: Session = Depends(get_db)):
    employees = get_all_employees(db)
    return employees

# GET маршрут для получения всех родтсвенников
@app.get("/employees/relatives", response_model=List[RelativeOut])
def read_relatives(db: Session = Depends(get_db)):
    relatives = get_all_relatives(db)
    return relatives

# Новый GET маршрут
@app.get("/employees/search", response_model=RelationsSearchResponse)
def search_employee(
    email: Optional[str] = None,
    phone_number: Optional[str] = None,
    db: Session = Depends(get_db)
):
    # Ищем сотрудника
    employee = get_employee_by_contact(db, email=email, phone_number=phone_number)
    if not employee:
        return {
            "message": {
                "employee": "Не удалось найти",
                "relation": "Не удалось найти"
            }
        }

    # Получаем родственников сотрудника
    relatives = get_relatives_by_employee_id(employee.tnum, db)
    if not relatives:
        relatives_response = "Не удалось найти"
    else:
        relatives_response = [
            {
                "r_num": relative.r_num,
                "full_name": relative.full_name,
                "gender": relative.gender,
                "birth_date": relative.birth_date,
                "relation_type": relative.relation_type,
            }
            for relative in relatives
        ]

    # Формируем ответ
    return {
        "message": {
            "employee": {
                "id": employee.tnum,
                "full_name": employee.full_name,
                "hire_date": employee.hire_date,
                "phone_number": employee.phone_number,
                "email": employee.email,
                "gender": employee.gender,
                "birth_date": employee.birth_date,
                "hobbies": employee.hobbies,
            },
            "relation": relatives_response
        }
    }