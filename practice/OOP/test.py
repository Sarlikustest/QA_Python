class Person:
    def __init__(self,name,age):
        self.name = name #self.name - атрибут name
        self.age = age #self.age - атрибут age
    
    def greet(self):
        print('etllo', self.name)