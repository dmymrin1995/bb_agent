from sqlalchemy import Column, Integer, String, Date, Text
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    tnum = Column(Integer, primary_key=True, index=True)  # Табельный номер
    full_name = Column(String, nullable=False)  # ФИО
    hire_date = Column(Date, nullable=False)  # Дата приема на работу
    phone_number = Column(String, nullable=False)  # Номер телефона
    email = Column(String, nullable=False, unique=True)  # Почта
    gender = Column(String, nullable=True)  # Пол (опционально)
    birth_date = Column(Date, nullable=True)  # Дата рождения
    hobbies = Column(Text, nullable=True)  # Хобби
