#len {string}: Devuelve la longitud de la cadena de texto

stringChange = "Mi cadena de texto"
print (f"La longitud de la cadena es: {len(stringChange)}")

#count (substring): Cuenta cuantas veces aparece una subcadena en la cadena de texto
print(f"La subcadena 'cadena' aparece: {stringChange.count ('cadena')} veces.")
print(f"Muy bien, no usaste la palabra cadena" if stringChange.count("cadena") == 0 else "Usaste la palabra cadena")

#upper(): convierte la cadena de texto a mayusculas
username = "imperIOUS"
print(username.upper())

#lower(): convierte la cadena de texto a minusculas
print(username.lower())

#capitalize(): convierte el primer caracter de la cadena de texto a mayuscula
print(username.capitalize())

#replace(old,new): reemplaza una subcadena por otra en la cadena de texto
userStatus = "Usuario no autorizado"
print (userStatus.replace("no autorizado", "autorizado"))

#split(separator): divide la cadena de texto en una lista de subcadenas utilizando un separador

testText = "Este es un texto de prueba"
print(testText.split(" "))