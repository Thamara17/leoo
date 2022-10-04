'''
Implementacion de colas mediante deque()
Demuestra las diferencias en la forma de implementacion

'''
SEPARADOR = ("*" * 20) + "\n"
import collections

cola = collections.deque()    #Cola utilizando deque

for cantidad in range(5):
    nuevo = input("Nombre del recien llegado: ")
    cola.append(nuevo)


print(f"Se agregaron {len(cola)}, elementos:")


