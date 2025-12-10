#Ejercicio 1 
# Dado una lista de numeros, utiliza la funcion reduce para encontrar el producto de todos los numeros en la lista. 
# Muestra el resultado por consola.

from functools import reduce

myList2 = [3,4,5,6,7,8,9]

def sumTheseNumbers(accumulator,number):
    return accumulator + number

totalSuma = reduce (sumTheseNumbers,myList2)

print(f"El resultado de este reduce es: {totalSuma}")

#Ejercicio 2
# Dada una lista de palabras, utiliza la funcion reduce para concatenar todas las palabras en una sola cadena 
# separada por espacios. Muestra el resultado por consola.

listaPalabras = ["Hola ", "este ", "es ", "un ", "ejercicio ", "en ", "Python"]

myText = reduce (lambda accumulator, string: accumulator + string, listaPalabras)
print(f"El resultado de reduce es: '{myText}'")