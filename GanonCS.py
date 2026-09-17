class Student:
    pass

class Course:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        
course = Course()

student1 = Student()
student2 = Student()

course.add_student(student1)
course.add_student(student2)

print(course.students)

