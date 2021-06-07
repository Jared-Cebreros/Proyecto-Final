# Proyecto-Final
Proyecto final programacion avanzada

El proyecto consiste en un lector de lenguaje de señas universal, ayudando al usuario a aprender y identificar cada letra del abecedario universal de señas. Utlizando las librerias basicas como son Cv2 y Numpy, es posible realizar un facil lector de señas, ya que solo es necesario comparar los contornos generados en cada imagen o video, de esta forma saber a que letra se refiere.

Una vez dicho esto, las imágenes que se usaron como datos o elemntos de entrada de un modelo computacional óptimo que puede predecir el significado de una nueva imagen presentada, Evaluamos el rendimiento del método utilizando medidas de clasificación y comparando diferentes contornos.

Nuestro proposito fue la creacion del reconocimiento de un lenguaje de señas para personas sordas con una accesibilidad a un ordenador.
import random 
 
def buscarElemento(lista, elemento): #es para ubicar un elemnto de una lista nos podria servia para ubicar imagines. 
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
