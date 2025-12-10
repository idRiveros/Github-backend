def sayHello():
    print("Hola mundo")

sayHello()

def sayHelloUser(name):
    print(f"Hola {name}")

sayHelloUser("Ivan")
sayHelloUser("Juan")
sayHelloUser("Delvis")

#crear una funcion saludo que salude a una persona por su nombre y apellido y mostrar el resultado

def diHolaUsuario(name, apellido):
    print(f"Hola {name} {apellido}")

diHolaUsuario("Ivan", "Riveros")

#Ejercicio
# Enunciado:  
# Define una función "calculator", que reciba dos numeros, y el tipo de operacion 
# y segun el tipo de operacion la realice y retorne el resultado. luego muestra el resultado por consola

def miniCalculadora(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    if operacion == "-":
        return num1 - num2
    if operacion == "*":
        return num1 * num2
    if operacion == "/":
        return num1 / num2

resultado = miniCalculadora(5,53,"*")
print (resultado)

#tipos de funciones
#lambda, funciones que nos permiten crear funciones en 1 linea

funcion = lambda name: print (f"Hola {name}")

funcion("Ivan")

def process(list, callback):
        """process recibira una lista de elementos y una funcion (callback)
        para cada uno de los elementos dentro de la lista, aplicara esa funcion
        y asi, devolvera una nueva lista con los elementos transformados
    """
        return[callback(item) for item in list]

result = process([1,2,3], lambda item: item *2)
print(result)

#Ejercicio 2
#Crear una funcion que reciba una lista de numeros y una funcion callback
#y devuelva una nueva lista con los numeros transformados divididos entre 2 
#y luego mostrar los primos y no primos segun la funcion callback

def numerosprimos(n):
    if n <=1:
        return f"El numero {n} no es primo"
    for i in range (2, n):
        if n % i == 0:
            return f"El numero {n} no es primo"
    return f"El numero {n} es primo"

def numeros(list, callback): 
    return [callback(item) for item in list]

resultado = numeros([2,3,4,5,6,7,8,9,10,11,12,13,14,15], lambda item: item/2)
clasificacion = [numerosprimos(int(num)) for num in resultado]

print ("Lista de numeros: ", resultado)
print("Clasificación:", clasificacion)