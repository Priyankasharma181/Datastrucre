from os import name


class car:
    def __init__(self,name,surname):
        self.name = name
        self.surname  = surname
    def a(self):
        print(self.name ,self.surname)
b = car("kruna","jaiswal")   
b.a() 