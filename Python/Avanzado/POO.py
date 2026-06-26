#POO

""" La programacion orientada a objetos es un paradigma de programacion que nos permite crear objetos que contienen datos y funcionalidades.
    Estos objetos pueden interactuar entre si y con otros objetos para crear programas complejos y modulares.
    La POO se basa en cuatro conceptos principales: clases, objetos, herencia y polimorfismo. """
    
class Person:
    #constructor: se utiliza para inicializar los atributos de la clase
    #atributos: son las caracteristicas o propiedades de la clase
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    #Metodo
    def greet(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old and I am {self.gender}."
    def is_adult(self):
        return self.age >= 18
      
      
#Instanciemos la clase Person para crear objetos

person1 = Person("Andreina", 25, "Femenino")
print(person1.greet())
print("Is adult:", person1.is_adult())
print("El nombre de esta persona es:", person1.name)

person2 = Person("Jesus", 26, "Masculino")
print(f"El nombre de esta persona es: {person2.name}")
print(person2.greet())

#Ejercicio:

#Crear una clase llamada "Estudiante" que tenga los atributos "nombre", "edad" y "carrera".
#Agregar un metodo llamado "estudiar" que imprima un mensaje indicando que el estudiante esta estudiando su carrera.

class Estudiante:
    def __init__(self, name, age, career):
        self.name = name
        self.age = age
        self.career = career
        
    def estudiar(self):
        print(f"{self.name} tiene {self.age} y está estudiando {self.career}.")
        
estudiante1 = Estudiante("Andreina", 25, "Ingenieria")
estudiante1.estudiar()

#Herencia 
#Es la capacidad de una clase de heredar sus atributos o metodos a otra
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("El animal hace ruido")

class Dog(Animal):
  def dog_run(self):
       print(f"{self.name} está corriendo.")
    
  #Polimorfismo: la capacidad de una clase de modificar un metodo heredado de la clase padre
  def make_sound(self):
        print("El perro ladra")
        
class Michi(Animal):
    def make_sound(self):
        print("El gato maulla")


genericAnimal = Animal("Animal Generico", "Desconocida")
genericAnimal.make_sound()

dog = Dog("Firulais", "Canino")
dog.make_sound()
dog.dog_run()

cat = Michi("Michi", "Felino")
cat.make_sound()