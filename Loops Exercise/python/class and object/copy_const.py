import copy
class Student:
    def __init__(self,name,age):
            self.name = name
            self.age = age
s1 = Student("Abhinandan",20)
s2 = copy.copy(s1)

print("Student 1:",s1.name,s1.age)
print("Student 2:",s2.name,s2.age)