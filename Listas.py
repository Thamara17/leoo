'''
Ejemplo para demostrar el manejo de listas
Demuestra: Creacion, acceso a elementos, ordenamiento y comprension de listas
'''
SEPARADOR = ("*" * 20) + " \n"

#Creacion de listas
#Lista vacía
Lista_vacia = list()
Otra_lista_vacia=[]
#Lista con elementos iniciales
Lista_uno = [1, 2, 3, 4]
print(Lista_uno)
print(SEPARADOR)
pass


#Agregar elementos a listas existentes
Lista_uno.append(5)
print(Lista_uno)
Lista_uno.append((6,7)) #Una lista puede ser un elementro de otra lista
print(Lista_uno)
print(SEPARADOR)
pass


#Remover elementos de una lista
Lista_uno.remove((6,7)) #Se le pasa el valor del elemento a remover
print(Lista_uno)
print(SEPARADOR)
pass


#Ordenar elementos de una lista
#sort()
lista_original1 = [3, 4, 2]
print(lista_original1)
lista_original1.sort()
print(lista_original1)
pass



#Sorted()
lista_original2 = [23, 10, 30, 5]
lista_ordenada = sorted(lista_original2)
print(f"lista original = {lista_original2}, y la version ordenada es {lista_ordenada}")
print(SEPARADOR)
pass




#Comprension de listas
print(f"lista original = {Lista_uno}")

#SIN comprension de listas
Lista_uno_al_doble = []
for valor in Lista_uno:
    Lista_uno_al_doble.append(valor * 2)
print(f"Lista resultante, cada elemento al doble = {Lista_uno_al_doble}")
pass

#CON comprension de listas
Lista_uno_al_doble = [valor * 2 for valor in Lista_uno]
print(f"Mismo resultado, pero con comprension de listas = {Lista_uno_al_doble}")
pass

#Comprension de listas con condicion
lista_valores_pares = [valor for valor in Lista_uno if (valor % 2 == 0)]
print(f"Solamente se agregaron los elementos con valor par : {lista_valores_pares}")