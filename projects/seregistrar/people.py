# [missing-module-docstring]

class Person:

    def __init__(
        self, first_name: str, last_name: str, address: str, date_of_birth: str
    ):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.address: str = address
        self.date_of_birth: str = date_of_birth

    def __str__(self) -> str:
        return f"person_info:\nID: {None}\nFirst: {self.first_name}\nLast: {self.last_name}\nAddress: {self.address}\nDOB: {self.date_of_birth}\n"


class Professor(Person):
    year: int = 2025
    id_counter: int = 2000

    def __init__(
        self,
        first_name: str,
        last_name: str,
        address: str,
        date_of_birth: str,
        salary=0,
    ):
        Professor.id_counter += 1
        super().__init__(first_name, last_name, address, date_of_birth)
        self.id = f"INS{Professor.year}-{Professor.id_counter}"
        self.salary: float = salary
        self.courses: list = []

    def __str__(self) -> str:
        return f"professor_info:\nID: {self.id}\nFirst: {self.first_name}\nLast: {self.last_name}\nAddress: {self.address}\nDOB: {self.date_of_birth}\n"

    def get_salary(self):
        """Returns object's salary."""
        return self.salary

    def get_courses(self):
        """Returns a list of courses a professor is currently teaching"""
        return self.courses


class Student(Person):
    year = 2025
    id_counter = 3000

    def __init__(self, first_name: str, last_name, address, date_of_birth):
        Student.id_counter += 1
        super().__init__(first_name, last_name, address, date_of_birth)
        self.id = f"STU{Student.year}-{Student.id_counter}"
        self.courses = []

    def __str__(self):
        """prints a string of this object's info"""
        return f"""student_info:\nID: {self.id}\nFirst: {self.first_name}\nLast: {self.last_name}\nAddress: {self.address}\nDOB: {self.date_of_birth}\n"""
