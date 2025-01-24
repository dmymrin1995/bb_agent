from database import SessionLocal
from populate import populate_from_csv, populate_relatives_from_csv

db = SessionLocal()

# Заполнение таблицы сотрудников
populate_from_csv(db, "./tables/employees.csv")

# Заполнение таблицы родственников
populate_relatives_from_csv(db, "./tables/relation.csv")

print("Данные успешно добавлены в базу!")
db.close()
