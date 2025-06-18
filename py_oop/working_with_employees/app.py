import csv, json
from datetime import datetime


def employee_factory(
    id, first, middle, last, age, salary, position, department
) -> dict:
    return {
        "id": int(id),
        "name": f"{first} {middle}. {last}",
        "age": int(age),
        "salary": round(float(salary), 2),
        "position": position,
        "department": department,
        "hired_date": str(datetime.now().date()),
    }


employees = []

with open("./employees.csv") as csvfile, open("./employee.json", "w+") as jsonfile:
    """hint:
    csv-format: id,first,middle,last,age,salary,position,department"""
    data = csvfile.readlines()
    header = data[0][:-1].split(",")
    # employees = [dict(zip(header, current[:-1].split(","))) for current in data[1:]]
    employees = [employee_factory(*employee[:-1].split(",")) for employee in data[1:]]
    json.dump(employees, jsonfile)


if __name__ == "__main__":
    for employee in employees[:10]:
        print(employee)
