class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
student1 =Student("khushi",89,98)
student2 =Student("raj",89,98)
print(student1.name,student1.age,student2.age)