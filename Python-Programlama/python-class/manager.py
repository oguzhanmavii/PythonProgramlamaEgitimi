from ders11 import *

#Inherited or Subclass (note Human in bracket)

class Manager(Human):
    def __init__(self,firstname,lastname,status,age):
        super().__init__(firstname,lastname,status,age)


manager=Manager(input("firstname:"),input("lastname:"),input("status:"),input("age:"))
manager.display()    