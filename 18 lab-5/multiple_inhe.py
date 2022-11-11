class School:
    def __init__(self, name) -> None:
        self.schoolName = name

    def say_name(self):
        print(f'Hello i am {self.schoolName}')

    def __repr__(self) -> str:
        return f'School({self.schoolName})'

class Teacher:
    def __init__(self, name) -> None:
        self.teacherName = name

    def say_name(self):
        print(f'Hello i am {self.teacherName}')

    def __repr__(self) -> str:
        return f'Teacher({self.teacherName})'

class Student(Teacher, School):    #class Student(School, Teacher):
    def __init__(self, name, teacherName, schoolName) -> None:
        Teacher.__init__(self,teacherName)
        School.__init__(self,schoolName)
        # super().__init__(teacherName)
        # super().__init__(schoolName)
        self.studentName = name

    def __repr__(self) -> str:
        return f'Student({self.studentName})'

student = Student('Jhon','David', 'ACJMHS')
# print(student.teacherName)
student.say_name()