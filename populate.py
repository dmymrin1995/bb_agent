import pandas as pd
from sqlalchemy.orm import Session
from models import Employee, Relative, Event, DiscountCard

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

def populate_relatives_from_csv(db: Session, file_path: str):
    df = pd.read_csv(file_path)

    for _, row in df.iterrows():
        relative = Relative(
            r_num=row['r_num'],
            tnum=row['tnum'],
            full_name=row['full_name'],
            gender=row.get('gender', None),
            birth_date=pd.to_datetime(row['birth_date']).date() if not pd.isna(row['birth_date']) else None,
            relation_type=row['relation_type'],
        )
        db.add(relative)
    db.commit()

def populate_events_from_csv(db: Session, file_path: str):
    df = pd.read_csv(file_path)

    for _, row in df.iterrows():
        event = Event(
            e_num=row['e_num'],
            event_date=pd.to_datetime(row['event_date']).date() if not pd.isna(row['event_date']) else None,
            event_name=row['event_name'],
            age_limit=row['age_limit'],
            price=row['price'].replace(',', '.'),
            discount=row['discount'].replace(',', '.'),
        )
        db.add(event)
    db.commit()

def populate_card_discount_from_csv(db: Session, file_path: str):
    df = pd.read_csv(file_path)

    for _, row in df.iterrows():
        event = DiscountCard(
            p_num=row['p_num'],
            partner=row['partner'],
            discription=row['discription'],
            card_discount=row['card_discount'],

        )
        db.add(event)
    db.commit()