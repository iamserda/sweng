from course import Course
from people import *

class Registrar:
    count = 0
    def __init__(self):
        if Registrar.count == 0:
            self.__courses = list()
            self.__students = list()
            self.__professors = list()
            Registrar.count += 1
        else:
            raise ValueError("Only 1 Registrar instance can exist!\nPlease use the existing one or delete it and create a new one.")

    def create_course(self, name):
        new_course = Course(name)
        self.__courses.append(new_course)
        return new_course
    
    def hire_professor(self, first, last, address, dob):
        new_professor = Professor(first, last, address, dob)
        new_professor.salary = 200000
        self.__professors.append(new_professor)
        return new_professor
    
    def register_student(self, first, last, address, dob):
        new_student = Student(first, last, address, dob)
        self.__students.append(new_student)
        return new_student
    
    def assign_professor_to_course(course:Course, professor:Professor):
        if not course or not isinstance(course, Course):
            print(TypeError("No course was provided, or invalid data type for course. course object must be a valid Course."))
            return
        
        if not professor or not isinstance(professor, Professor):
            print(TypeError("No course was provided, or invalid data type for course. course object must be a valid Course."))
            return
        
        if course.instructor:
            print(f"WARNING: Changing professor for {course.id} from Professor: {course.instructor} to professor{professor}.")
        
        if len(professor.courses) >= 4:
            print(f"WARNING: Current professor: {course.instructor} will have more than the recommended limit. Message will be sent to Dean.")

        course.instructor = professor
        professor.courses.append(course.id)


    def list_current_course(self):
        course_offering = [course.id for course in self.__courses]
        return course_offering
    
    def delete_registrar(self):
        Registrar.count = 0
        del self