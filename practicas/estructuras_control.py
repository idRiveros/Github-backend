age = 16

if age >=18:
    print("Puedes pasar eres mayor")
elif age < 18 & age > 0:
    print("Eres menos no puedes pasar")
else:
    print("No es una edad valida")

print ("Selecciona un idioma, con su numero respectivo: 1 Espanol, 2. Ingles, 3. Frances")
answer = input()

match answer:
  case "1":
    print("Elegiste el idioma Espanol")
  case "2":
    print("Elegiste el idioma Ingles")
  case "3":
    print("Elegiste el idioma Frances")
  case _:
    print("Idioma no valido")