# Proyecto-Final
Proyecto final programacion avanzada

El proyecto consiste en un lector de lenguaje de señas universal, ayudando al usuario a aprender y identificar cada letra del abecedario universal de señas. Utlizando las librerias basicas como son Cv2 y Numpy, es posible realizar un facil lector de señas, ya que solo es necesario comparar los contornos generados en cada imagen o video, de esta forma saber a que letra se refiere.

import random 
 
def buscarElemento(lista, elemento): #es para ubicar un elemnto de una lista nos podria servia para ubicar imagines, faltan cambios 
    for i in range(0,len(lista)):
        if(lista[i] == elemento):
            return i
 
def imprimirLista(lista,nombre):
    for i in range(0,len(lista)):
        print nombre + "[" + str(i) + "]=" + str(lista[i])
 
def leerLista():
    lista=[]
 
    i=0
    while i < 10:
        lista.append(int(random.randint(0, 10)))
        i=i+1
    return lista
 
A=leerLista()
imprimirLista(A,"A")
cn=int(raw_input("Numero a buscar: "))
print "A[" + str(buscarElemento(A,cn)) + "]"
