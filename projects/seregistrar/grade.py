class Grade:
    def __init__(self, course_id, student_id, score):
        self.course_id = course_id
        self.student_id = student_id
        self.score = score
        self.grade = None
    def __str__(self):
        return f"""course: {self.course_id}\nstudent: {self.student_id}\nscore: {self.score}\ngrade: {self.grade}"""
    
    def get_grade(self):
        score = self.score
        grade_book = {
            90: "A",
            80: "B",
            70: "A",
            60: "D"}
        if score < 0 or score > 100:
            print("invalid score, score cannot be less than 0 or more than 100")
            return
        if score >= 90:
            self.grade = grade_book[90]
        elif score >= 80:
            self.grade = grade_book[80]
        if score >= 70:
            self.grade = grade_book[70]
        if score >= 60:
            self.grade = grade_book[60]
        if score <= 59:
            self.grade = "F"