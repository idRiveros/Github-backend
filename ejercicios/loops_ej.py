#Enunciado de ejercicios:

# Ejercicio 1: Contador Selectivo (For + If)
# Enunciado:  
# Escribe un programa que pida al usuario un número entero positivo n. 
# Luego, usando un bucle for, imprime todos los números del 1 al n que cumplan una de estas condiciones:
# 1. El número es múltiplo de 3.
# 2. El número es mayor que 10 y menor que 20.
# 3. El número es igual a 25 o 50.  
# Si el número no cumple ninguna condición, no se imprime.

numero = int(input("Para iniciar, escribe un numbero positivo: "))

for number in range (1, numero +1):
    if (10 < number > 20) or (number % 3 ==0) or (number ==25 or number ==30):
        print (f"El numero {number} cumple con alguno de los requisitos")

#Ejercicios opcionales para practica

# Ejercicio 2:
#Enunciado: 
# Crea un programa que simule la validación de una contraseña:
# 1. Define una contraseña secreta (ej: "python123").
# 2. Pide al usuario que ingrese una contraseña.
# 3. Usa un bucle while para:
#    - Permitir hasta 3 intentos.
#    - Si la contraseña es correcta, muestra "¡Acceso concedido!" y termina.
#    - Si es incorrecta, muestra "Contraseña incorrecta. Intentos restantes: X".
#    - Si se agotan los intentos, muestra "¡Cuenta bloqueada!".

password = "python123"
attempts = 3

print("Bienvenido al sistema de validacion")
while attempts > 0:
    userInput = input ("Ingresa tu contraseña: ")
    if userInput == password:
        print ("Acceso concedido!")
        break
    else:
        attempts -=1
        print (f"Contraseña incorrecta. Intentos restantes: {attempts}")

if attempts == 0:
    print("Cuenta bloqueada!")

#Ejercicio 3
# Enunciado:  
# Pide al usuario 5 números enteros. Usando un bucle for y match-case:
# 1. Clasifica cada número en:
#    -"Pequeño" si es menor que 10.
#    -"Mediano" si está entre 10 y 50.
#    -"Grande" si es mayor que 50.
#    -"Cero" si es 0.
# 2. Al final, muestra cuántos números hubo en cada categoría.

pequeno = mediano = grande = cero = 0

for _ in range(5):
    num = int(input("ingresa un numero: "))
    match num:
        case 0:
            cero +=1
        case n if n < 10:
            pequeno += 1
        case n if 10 <= n <=50:
            mediano +=1
        case _:
            grande +=1

print ("Resultados: ")
print ("Pequeno: ", pequeno)
print ("Mediano: ", mediano)
print ("Grande: ", grande)
print ("Cero: ", cero)