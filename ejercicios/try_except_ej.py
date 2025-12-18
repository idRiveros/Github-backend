#Ejercicio práctico

#Crea una función que tome una lista de números y devuelva la suma de todos los números en la lista.
#La función debe manejar posibles excepciones, como si la lista contiene elementos que no son números.

numList = [5,6,7,8,9,"r",10,"q"]

def sumNumbers(numList):
    total = 0
    for elemento in numList:
        try:
            total += (elemento)
        except (TypeError): 
            print(f"Elemento inválido: {elemento}")
    return total

print(sumNumbers(numList))