from people import Professor, Student
from grade import Grade
from course import Course
from registrar import Registrar

sole_registrar = Registrar()

def get_info():
    _data = {
        "first":"",
        "last":"",
        "address":"",
        "dob":""
    }
    _data["first"] = input("Enter First Name: ")
    _data["last"] = input("Enter Last Name: ")
    _data["address"] = input("Enter Address: ")
    _data["dob"] = input("Enter DOB: MM-DD-YYYY: ")

def register_student():
    

