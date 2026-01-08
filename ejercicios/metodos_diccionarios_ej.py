"""

Ejercicio de Complejidad Media: Sistema de Gestión de Biblioteca

Enunciado:
Crea un programa que gestione una biblioteca con las siguientes funcionalidades:

Registrar libros:

Pedir título, autor, año de publicación y género.

Almacenar los libros en una lista de diccionarios.

Validar que el año sea un número entre 1000 y 2025.

Buscar libros:

Permitir búsqueda por: título, autor o género.

Mostrar todos los libros que coincidan (aunque sea parcialmente).

Usar match-case para determinar el tipo de búsqueda.

Préstamos de libros:

Permitir "prestar" un libro cambiando su estado (agregar clave disponible: bool).

Llevar registro de libros prestados y disponibles.

No permitir préstamo si no hay ejemplares disponibles.

Estadísticas:

Mostrar:

Total de libros

Libros disponibles vs prestados

Género más popular

Usar bucles for y condicionales para calcular datos.

Menú interactivo:

Usar while para mantener el programa activo hasta que el usuario elija salir.

Mostrar opciones numeradas y manejar entradas inválidas.

"""