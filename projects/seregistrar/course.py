from people import Professor, Student

class Course:
    year = 2025
    id_counter = 100
    def __init__(self, title):
        Course.id_counter += 1
        self.id = f"CO{Course.year}UR{Course.id_counter}SE"
        self.title = title
        self.instructor:Professor = None
        self.students = []
    def __str__(self):
        return f"""id: {self.id}\ntitle: {self.title}\ninstructor: {self.instructor if self.instructor else "TBD"}\nregistered: {len(self.students)}"""
    def assign_instructor(self, instructor: Professor):
        self.instructor = instructor
        return self.instructor
    
    def add_student(self, student:Student):
        self.students.append(student)
        return len(self.students)

if __name__ == "__main__":
    new_course = Course("Psychology")
    print(new_course)