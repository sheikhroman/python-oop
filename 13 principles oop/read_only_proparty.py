class Student: 
    def __init__(self, name, id, marks):
        self._name = name
        self.__id = id
        self.marks = marks

    @property
    def student_id(self):
        return self.__id
    
    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name

khan = Student('King Khan', 12, 55)
print(khan.student_id)
# khan.student_id = 77
print(khan.name)
del khan.name
print(dir(khan))
