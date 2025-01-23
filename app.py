from fastapi import FastAPI, HTTPException

app = FastAPI()

employees = [
    {"tnum": 1488, "fio":"Мымрин Дмитрий Николаевич", "brithday": "19.08.1995", "gender": "male", "phone": "9642142945", "email": "dmymrin1995@gmail.com"}
]

relations = [
    {'r_id': 1, "tnum": 1488, "fio": "Мымрин Евгений Дмитриевич", "brithday": "19.09.2015", "relation_type": "сын"}
]

def find_employee_by_contact(employees, contact):
    """
    Функция для поиска сотрудника по email или номеру телефона.
    :param employees: список сотрудников
    :param contact: email или номер телефона для поиска
    :return: найденный сотрудник или None, если не найден
    """
    for employee in employees:
        if employee["email"] == contact or employee["phone"] == contact:
            return employee
    return None

def find_relations_by_employee(relations, tnum):
    """
    Функция для поиска родственников сотрудника по табельному номеру (tnum).
    :param relations: список родственников
    :param tnum: табельный номер сотрудника
    :return: список родственников
    """
    return [relation for relation in relations if relation["tnum"] == tnum]

@app.get("/home")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/search/")
async def search_employee(contact: str):
    # Ищем сотрудника по контакту
    employee = find_employee_by_contact(employees, contact)
    if not employee:
        return {"message": "Сотрудник не найден"}

    # Ищем родственников сотрудника
    employee_relations = find_relations_by_employee(relations, employee["tnum"])
    return {
        "employee": employee,
        "relations": employee_relations
    }
