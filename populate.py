import pandas as pd
from sqlalchemy.orm import Session
from models import Employee

def populate_from_csv(db: Session, file_path: str):
    df = pd.read_csv(file_path)

    for _, row in df.iterrows():
        hobbies = row['hobbies'] if isinstance(row['hobbies'], str) else None

        employee = Employee(
            tnum=row['tnum'],
            full_name=row['full_name'],
            hire_date=pd.to_datetime(row['hire_date']).date(),
            phone_number=row['phone_number'],
            email=row['email'],
            gender=row.get('gender', None),
            birth_date=pd.to_datetime(row['birth_date']).date() if not pd.isna(row['birth_date']) else None,
            hobbies=hobbies,
        )
        db.add(employee)
    db.commit()