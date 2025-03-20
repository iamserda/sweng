from people import Professor, Student
from grade import Grade
from course import Course
from registrar import Registrar

app_admin = Registrar()


def get_person_info():
    _data = {}
    _data["first"] = input("Enter First Name: ")
    _data["last"] = input("Enter Last Name: ")
    _data["address"] = input("Enter Address: ")
    _data["dob"] = input("Enter DOB: MM-DD-YYYY: ")
    return _data


def create_new_student():
    student_info = get_person_info()
    if student_info:
        new_student = app_admin.hire_professor(**student_info)
        print("Success: A new student was created.")
        return new_student
    return ValueError("Could not create new student with the info given.")


def hire_new_professor():
    professor_info = get_person_info()
    if professor_info:
        new_prof = app_admin.hire_professor(**professor_info)
        print("Success: A new professor was created.")
        return new_prof
    return ValueError("Could not create new professor with the info given.")


def create_new_course():
    course_details = {}
    course_details["title"] = input("Enter Course Title: ")
    course_details["prof_id"] = input("Enter Professor ID: ")
    if course_details["title"]:
        new_course = app_admin.create_course(course_details["title"])
        print(f"Sucess: A new course with title: {new_course.title} was created.")
        if course_details["prof_id"] and new_course:
            professor: Professor = app_admin.__professors[course_details["prof_id"]]
            new_course.assign_instructor(professor)
            print(
                f"Sucess: Prof. {professor.first_name} {professor.last_name}  was assigned to this course."
            )
        return new_course
    return ValueError("Could not create new course with the info given.")


def display_options():
    message = """Options:\n1- Create new course\n2- Add a new student\n3- Add a new Professor\n4- Show all courses\n9- Display this menu\nx- Exit app.\n\n"""
    print(message)


def get_all_courses():
    for course in app_admin.list_current_course():
        print(f"course:\ncourse\n")


if __name__ == "__main__":
    set_of_options = set(list("0123456789x"))
    user_input = "1"
    display_options()
    while user_input.lower() in set_of_options:
        user_input = input("$-> ")
        match user_input:
            case "1":
                create_new_course()
            case "2":
                create_new_student()
            case "3":
                hire_new_professor()
            case "4":
                get_all_courses()
            case "9":
                display_options()
            case "x":
                break
            case _:
                print("Invalid options, please try again!\n")
                user_input = "0"

""" 
TODO:
- register a student to a course -> register_course(course_id, student_id)
- assign a professor to a course -> Registrar.assign_instructor(course_id, instructor.id)
- search for a student -> search(id, type:student, professor, or course)
- 
"""
