class Person:
    #constructor:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    #metodo
    def greet(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and I am a {self.gender}."
    

#herencia
#es la capacidad de una clase de heredar sus atributos o metodos a otra

class Animal:
    def __init__(self, name, species):
        pass    