from ders11 import *

#Inherited or Subclass (note Human in bracket)

class Developer(Human):
    def __init__(self,firstname,lastname,status,age):
        super().__init__(firstname,lastname,status,age)


developer=Developer(input("firstname:"),input("lastname:"),input("status:"),input("age:"))
developer.display()   