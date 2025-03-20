from people import Professor, Student


class Course:
    """Class enables creation of course objects: {id, title, instructor, student}"""

    year = 2025
    id_counter = 1000

    def __init__(self, title: str):
        """constructor: returns a valid course object."""
        if not isinstance(title, str):
            raise TypeError("title arg must be a string.")
        if title and len(title) > 5:
            Course.id_counter += 1
            self.id = f"CO{Course.year}UR{Course.id_counter}SE"
            self.title = title
            self.instructor: Professor = None
            self.students = []
        else:
            raise ValueError("Title string may not be less than 5.")

    def __str__(self) -> str:
        """Returns a string of all data for this object."""
        return f"""\ncourse_info:\nid: {self.id}\ntitle: {self.title}\ninstructor: {self.instructor if self.instructor else "TBD"}\nattendance: {len(self.students)}\n"""

    def assign_instructor(self, instructor: Professor):
        """Given a valid instructor, assign a Professor object to this course-object."""
        if isinstance(instructor, Professor):
            self.instructor = instructor
            return self.instructor
        else:
            raise TypeError("Object type provide is not valid. Must-be type:Professor")

    def add_student(self, student: Student):
        """Register students to attend specific courses."""
        self.students.append(student.id)
        return len(self.students)
