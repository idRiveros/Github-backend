#Ejercicio: Crear una funcion que reciba una cadena de texto y devuelva la misma cadena con la primera letra de cada palabra en mayuscula.

def capitalizar_palabras(cadena):
    palabras = cadena.split()
    resultado = " "
    for p in palabras:
        resultado += p.capitalize() + " "
    return resultado

print(capitalizar_palabras("hola mundo desde el zulia"))