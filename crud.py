from datetime import date

from models import Employee, Relative, Event, DiscountCard
from sqlalchemy.orm import Session
from typing import List, Optional

# Получение всех сотрудников
def get_all_employees(db: Session) -> List[Employee]:
    return db.query(Employee).all()

# Получение родственников сотрудника по табельному номеру
def get_all_relatives(db: Session) -> List[Relative]:
    return db.query(Relative).all()

# Поиск сотрудника по email или номеру телефона
def get_employee_by_contact(db: Session, email: Optional[str] = None, phone_number: Optional[str] = None) -> Optional[Employee]:
    query = db.query(Employee)
    if email:
        query = query.filter(Employee.email == email)
    if phone_number:
        query = query.filter(Employee.phone_number == phone_number)
    return query.first()

# Получение родственников сотрудника
def get_relatives_by_employee_id(employee_id: int, db: Session):
    return db.query(Relative).filter(Relative.tnum == employee_id).all()

def get_events(db: Session):
    query = db.query(Event).filter(Event.event_date >= date.today()).all()
    return query

def get_card_discounts(db: Session):
    return db.query(DiscountCard).limit(100).all()