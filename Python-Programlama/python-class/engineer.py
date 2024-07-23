from ders11 import *

#Inherited or Subclass (note Human in bracket)

class Engineer(Human):
    def __init__(self,firstname,lastname,status,age):
        super().__init__(firstname,lastname,status,age)


engineer=Engineer(input("firstname:"),input("lastname:"),input("status:"),input("age:"))
engineer.display()        