#while

""" count=0

while count <3:
    print(f"me ejecuto, estoy en la vuelta {count}")
    count +=1

print("sali del bucle")

choice = int(input("Para iniciar escribe 1:"))

while choice == 1:
    num1 = int(input("Ingresa el primer numero a sumar: "))
    num2 = int(input("Ingresa el segundo numero a sumar: "))
    total = num1 + num2
    print(f"El resultado de tu suma fue {total}")
    choice = int(input("Para reiniciar escribe el numero 1: "))

print("Fin del programa") """

fruits = ["apple", "orange", "banana"]
print(fruits)

for fruit in fruits:
    print(fruit)

for number in range (0,11):
    print(f"El numero es: {number}")


myList = ["Eduardo", "Ivan", "Juan", "Delvis"]

for name in myList:
    if name == "Juan":
        break
    print(f"El nombre es: {name}")

for name in myList:
    if name == "Juan":
        continue
    print(f"El nombre es: {name}")