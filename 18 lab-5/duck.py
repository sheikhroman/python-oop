class Teacher:
    def __init__(self, name) -> None:
        self.teacherName = name
        self.students = []

    def entry_student(self, studentObj):
        self.students.append(studentObj)

class Student():
    def __init__(self, name) -> None:
        self.studentName = name

    def enter_in_a_teacher(self,teacherObj):
        teacherObj.students.append(self)

    def __repr__(self) -> str:
        return f'Student({self.studentName})'


david = Teacher('David')
dio = Teacher('Dio')

student = Student('Jhon')
# print(student.students)
student.enter_in_a_teacher(dio)
student.enter_in_a_teacher(david)
print(dio.students)
print(david.students)