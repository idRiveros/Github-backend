myList = [1,2,3,4,5]

def multiplyBy3(number):
    return number * 3

result = map(multiplyBy3,myList)

print (f"El resultado de map es: {list(result)}")

#segundo ejemplo, reduce (funcion, iterable):

from functools import reduce

myList = [1,2,3,4,5]

def sumTwoNumbers(accumulator,number):
    return accumulator + number

totalSum = reduce(sumTwoNumbers, myList)

print(f"El resultado de reduce es: {totalSum}")

#utilizando una funcion
myString = ["Hola ", "mi ", "nombre ", "es ", "Python"]
#utilizando una funcion lambda
myText = reduce (lambda accumulator, string: accumulator + string, myString)
print(f"El resultado de reduce es: '{myText}'")

# Tabla de funciones generales en Python para la transformación de datos
# +--------+------------------------------------------------------+
# | Nombre | Descripción                                          |
# +--------+------------------------------------------------------+
# | bool() | Convierte un valor en booleano.                      |
# | dict() | Crea un nuevo diccionario.                           |
# | float()| Convierte un número o cadena en un número de punto flotante. |
# | str()  | Convierte un objeto en una cadena.                   |
# | int()  | Convierte un número o cadena en un entero.           |
# | list() | Crea una lista.                                      |
# | tuple()| Crea una tupla.                                      |
# | float()| Convierte un número o cadena en un número de punto flotante. |
# +--------+------------------------------------------------------+

#int() ejemplo:
print(int("12345"))

#float() ejemplo:
print(float("3.14")+10)
print(float(10))

#str() ejemplo:
print(str(100)+" es un numero")
print(str(3.14)+" es un numero de punto flotante")

#bool() ejemplo:
print (bool(1))
print (bool(0))
print (bool(3))
print (bool(""))
print (bool("Holaa"))

#list() ejemplo:
print
print

#tupla() ejemplo:
print
print

#funciones para encontrar elementos en una coleccion:

#max() Devuelve el elemento con el valor maximo de una coleccion
print(f"El elemento con el valor maximo es: {max([2145,250,646,789])}")

#min() Devuelve el elemento con el valor minimo de una coleccion
print(f"El elemento con el valor maximo es: {min([2145,250,646,789])}")


#funciones para realizar operaciones matematicas:

#