#Ejercicio: Crear una funcion que reciba una cadena de texto y devuelva la misma cadena con la primera 
#letra de cada palabra en mayuscula. (usando append for)

def capitalizar_palabras(cadena):
    palabras = cadena.split()
    resultado = []
    for p in palabras:
        resultado.append(p.capitalize())
    return " ".join(resultado)

print(capitalizar_palabras("hola mundo desde el zulia"))

"""def capitalizar_palabras(cadena):
    palabras = cadena.split()
    for p in palabras:
        palabras.append(p.capitalize)
    return palabras

print(capitalizar_palabras("hola mundo desde el zulia"))"""

#Ejercicio: Crear una funcion que reciba una lista de numeros y devuelva una nueva lista con los numeros ordenados de mayor a menor, 
#sin modificar la lista original.

def numberlist(lista):
    new_list = lista.copy()
    new_list.sort(reverse=True)
    return new_list

print(numberlist([1,8,6,4,79,5,5,7]))
    