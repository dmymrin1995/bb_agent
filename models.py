from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Date, 
    Text,
    ForeignKey
)
from sqlalchemy.orm import relationship
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
    
    # Связь с родственниками
    relatives = relationship("Relative", back_populates="employee")

class Relative(Base):
    __tablename__ = "relatives"

    r_num = Column(Integer, primary_key=True, index=True)  # Уникальный номер родственника
    tnum = Column(Integer, ForeignKey("employees.tnum"), nullable=False)  # Табельный номер сотрудника
    full_name = Column(String, nullable=False)  # ФИО родственника
    gender = Column(String, nullable=True)  # Пол родственника
    birth_date = Column(Date, nullable=True)  # Дата рождения родственника
    relation_type = Column(String, nullable=False)  # Степень родства

    # Связь с сотрудником
    employee = relationship("Employee", back_populates="relatives")