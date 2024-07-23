from ders11 import *

#Inherited or Subclass (note Human in bracket)

class Teacher(Human):
    def __init__(self,firstname,lastname,status,age):
        super().__init__(firstname,lastname,status,age)


teacher=Teacher(input("firstname:"),input("lastname:"),input("status:"),input("age:"))
teacher.display()   