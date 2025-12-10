#funciones de tiempo
#son funciones que nos permiten trabajar con fechas y horas en Python

import time as tm

actualTm = tm.localtime()
print("Tiempo Actual: ", actualTm)

#sacar el año, mes y el dia actual
year = actualTm.tm_year
month = actualTm.tm_mon
day = actualTm.tm_mday
print(f"Año:", year)
print(f"Mes", month)
print(f"Dia:", day)

#construir una fecha especifica

