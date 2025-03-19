class Person:
    def __init__(self, first, last, address, dob):
        self.first_name = first
        self.last_name = last
        self.address = address
        self.date_of_birth = dob

class Professor(Person):
    year = 2025
    id_counter = 200
    def __init__(self, first, last, address, dob, salary):
        Professor.id_counter += 1
        self.id = f"INS{Professor.year}-{Professor.id_counter}"
        self.salary = salary
        self.courses = []
        super(first, last, address, dob)

class Student(Person):
    year = 2025
    id_counter = 2000
    def __init__(self, first, last, address, dob):
        Student.id_counter += 1
        self.id = f"STU{Student.year}-{Student.id_counter}"
        self.courses = []
        super(first, last, address, dob)