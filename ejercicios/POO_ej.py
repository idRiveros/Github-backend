## Ejercicio:
# Crear una clase llamada "Estudiante" que tenga los atributos "nombre", "edad" y "carrera".
# Agregar un método llamado "estudiar" que imprima un mensaje indicando que el estudiante está estudiando su carrera.

class Student:
    def __init__(self,name,age,career):
        self.name = name
        self.age = age
        self.career = career
    def greet(self):
        return f"Hello my name is {self.name}, I am {self.age}, and I'm studying {self.career}"
    
persona1 = Student("Juan", 21, "Marketing")
print(persona1.greet())

##Ejercicio de herencia y polimorfismo
#Crear una clase llamada "Vehiculo" con los atributos "marca", "modelo" y "año".
#Agregar un metodo llamado "info" que imprima la informacion del vehiculo.
#Crear dos clases hijas llamadas "Coche" y "Motocicleta" que hereden de la clase "Vehiculo".
#Modificar el metodo "info" en ambas clases hijas para que imprima informacion especifica de cada tipo de vehiculo

class Vehicle:
    def __init__(self, brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print (f"This vehicle's brand is {self.brand}, the model is {self.model}, and the year is {self.year}")
    
"""car1 = Vehicle("Renault", "Scenic", 2007)
print(car1.info())"""

class Cars(Vehicle):
    def info(self):
        print(f"Informacion del carro; es un {self.brand}, del modelo {self.model}, del año {self.year}")

class Motorcycle(Vehicle):
    def info(self):
        print(f"Informacion de la moto; es un {self.brand}, del modelo {self.model}, del año {self.year}")

car1 = Cars("Renault", "Scenic", 2007)
car1.info()

motorcycle1 = Motorcycle("Honda", "CB750", 1970)
motorcycle1.info()

"""class Vehicle:
    def __init__(self, brand, model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print (f"This vehicle's brand is {self.brand}, the model is {self.model}, and the year is {self.year}")
    
car1 = Vehicle("Renault", "Scenic", 2007)
print(car1.info())

class Cars(Vehicle):
    def car_model(self):
        print(f"El carro es un {self.model}.")
    def car_year(self):
        print(f"El carro es del año {self.year}.")
    def car_brand(self):
        print(f"El carro es de la marca {self.brand}")

carrogenerico = Vehicle("Scenic")
carrogenerico.brand"""

#mostrar atributos en forma de diccionario

print(car1.__dict__)

class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def info(self):
        super().info()
        print(f"Capacidad de bateria: {self.battery_capacity} kWh")

electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
electric_car.info()