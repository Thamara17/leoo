'''
Ejemplo para ilustrar la importancia de la libreria datetime en Python 3
Demuestre el uso de: hora, fecha y arimetica de fechas
'''
import datetime
from re import M
from sqlite3 import Date
import time
from tkinter import Y
SEPARADOR = ("*" * 20) + "\n"

#Creacion de una hora especifica
hora = datetime.time(10, 20, 30)
print(f"El tipo de objeto de la hora es {type(hora)}")
print(f"La hora es {hora}")
print(f"La hora de {hora} es {hora.hour}")      #Limitado 0..23
print(f"El minuto de {hora} es {hora.minute}")  #Limitado 0..59
print(f"El segundo de {hora} es {hora.second}") #Limitado 0..59
print(f"El microsegundo de {hora} es {hora.microsecond}")   #Limitado 0..59
print(SEPARADOR * 2)

#Determinar la fecha del sistema
fecha_actual = datetime.date.today()
print(f"El tipo de objeto de la fecha es {type(fecha_actual)}")
print(f"La fecha actual es {fecha_actual}")
print(f"El año actual es {fecha_actual.year}")
print(f"El mes actual es {fecha_actual.month}")
print(f"El dia actual es {fecha_actual.day}")
print(SEPARADOR * 2)

#Convertir un string a fecha
fecha_capturada = input("Dime una fecha(dd/mm/aaaa): \n")
fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%Y").date()

#Aritmetica de fechas basica
cant_dias = int(input("Dime la cantidad de dias a adelantar:\n"))
nueva_fecha = fecha_procesada + datetime.timedelta(days=+cant_dias)
print(f"La nueva fecha es {nueva_fecha}")
print(SEPARADOR)
