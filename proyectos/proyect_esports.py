"""
Punto de Parada 1: Consolidación de Lógica y Datos

Temas cubiertos: Variables, Operadores, Estructuras de control, Bucles, Funciones, Listas, Strings, Tuplas y Diccionarios.

### Proyecto Retador 1: "Sistema de Gestión de Torneos E-Sports"

*Duración:* 3 a 4 días.

*Fecha de entrega:* 2 de Diciembre de 2025.

Descripción:

Los estudiantes deben crear un programa de consola (CLI) que administre un torneo de videojuegos. El programa no guardará datos en 
archivos (aún no saben hacerlo), por lo que todo vivirá en la memoria (variables) mientras el programa corra.

*Requerimientos Técnicos:*

1. *Estructuras de Datos:* Usar una lista de diccionarios para almacenar los equipos. 
Ejemplo: [{ "nombre": "Team A", "puntos": 10, "jugadores": ["Juan", "Pedro"] }].
2. *Menú Interactivo (While + Match/If):* Un bucle infinito que muestre opciones: Registrar equipo, Registrar Jugador, 
Actualizar Puntos, Ver Tabla de Posiciones, Eliminar Equipo, Salir.
3. *Funciones:* Cada opción del menú debe llamar a una función específica (ej: registrar_equipo(), mostrar_tabla()).
4. *Manipulación de Strings:* Los nombres de los equipos deben guardarse siempre capitalizados (.capitalize() o .title()) y validarse
que no estén vacíos.
5. *Manejo de Errores:* Usar try-except para evitar que el programa se rompa si el usuario ingresa letras en lugar de puntos numéricos.
"""

equipos = [
    {"Nombre del equipo": "Moist", 
    "puntos": 0, 
    "jugadores": ["Joyo", "rehzzy", "oaly."],
    "victorias":0, "empates":0, "derrotas":0},
    {"Nombre del equipo": "Vitality", 
    "puntos": 0, 
    "jugadores": ["Zen", "ExoTiik","Stizzy"],
    "victorias":0, "empates":0, "derrotas":0},
    {"Nombre del equipo": "NRG",
    "puntos": 0,
    "jugadores": ["Atomico","Modo Bestia","Daniel"],
    "victorias":0, "empates":0, "derrotas":0},
    {"Nombre del equipo": "Dignitas",
    "puntos": 0,
    "jugadores": ["Aqua", "Evoh", "Fiv3Up"],
    "victorias":0, "empates":0, "derrotas":0},
]

while True:
    print("---MENU TORNEO DE ROCKET LEAGUE---")
    print("1. Registrar equipo")
    print("2. Registrar jugador")
    print("3. Actualizar puntos")
    print("4. Ver tabla de posiciones")
    print("5. Eliminar equipo")
    print("6. Salir")
    
    options = input("Seleccione una opcion: ")

    match options:
        case "1":
            nombre = input("Nombre del equipo: ").strip().title()
            existe = False
            for equipo in equipos:
                if equipo["Nombre del equipo"]==nombre:
                    existe = True
                    break
            if existe:
                print ("Este equipo ya existe.")
            else:
                equipos.append({"Nombre del equipo": nombre, "puntos":0, "jugadores": [], "victorias": 0, "empates":0, "derrotas": 0})
                print(f"Equipo {nombre} ha sido registrado.")
        case "2":
            nombre = input("Nombre del equipo: ").strip().title()
            for equipo in equipos:
                if equipo ["Nombre del equipo"] == nombre:
                    if len(equipo["jugadores"]) >= 3:
                        print(f"El equipo ya tiene un maximo de 3 miembros")
                    else:
                        jugador = input("Nombre del jugador: ").strip().title()
                        if not jugador:
                            print("El nombre no puede estar vacío.")
                        else:
                            equipo["jugadores"].append(jugador)
                            print(f"Jugador {jugador} agregado al equipo {nombre}.")
                    break
                else:
                    print("El equipo no existe")
        case "3":
            nombre = input ("Nombre del equipo: ").strip().title()
            for equipo in equipos:
                if equipo ["Nombre del equipo"] == nombre:
                    try:
                        resultado = int(input("Ingrese resultado (3 = victoria, 1 = empate, 0 = derrota): "))
                        if resultado in [0,1,3]:
                            equipo["puntos"] += resultado
                            if resultado == 3:
                                equipo["victorias"] += 1
                            elif resultado == 1:
                                equipo["empates"] += 1
                            elif resultado == 0:    
                                equipo["derrotas"] += 1
                            print(f"Los puntos han sido actualizados, el equipo {nombre} ahora suma {equipo['puntos']} puntos.")
                        else:
                            print("Solo se permiten los valores 3, 1 y 0")
                    except ValueError:
                        print("Debes imgresar un numero entero, el 3, 1 o 0")
                    break
                else:
                    print("Este equipo no existe, intenta de nuevo.")
        case "4":
            print("--- TABLA DE POSICIONES ---")
            tabla = sorted(equipos, key=lambda x: x["puntos"], reverse=True)
            for ranking, equipo in enumerate(tabla, start=1):
                print(f"{ranking}. {equipo['Nombre del equipo']} - {equipo['puntos']} puntos")
                print(f"Jugadores: {', '.join(equipo['jugadores'])}")
                print(f"Victorias: {equipo['victorias']} | Empates: {equipo['empates']} | Derrotas: {equipo['derrotas']}")
        case "5":
            nombre = input("Nombre del equipo: ")
            if not nombre:
                print("El nombre no puede estar vacío, intente de nuevo.")
            else:
                for equipo in equipos:
                    if equipo ["Nombre del equipo"] == nombre:
                        equipos.remove(equipo)
                        print(f"El equipo {nombre} ha sido eliminado")
                        break
        case "6":
            print("Ha salido del menu.")
            break
        case _:
            print("Opcion inválida, intente de nuevo")