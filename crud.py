from sqlalchemy.orm import Session
from models import Employee
from typing import List

# Функция для получения всех сотрудников
def get_all_employees(db: Session) -> List[Employee]:
    return db.query(Employee).all()
