#creando una lista con list()
lista = list(["hola","daltos",34,56,41,True])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agragando un elemento a la lista
lista.append("JAJAJA")

#agragando un elemento a la lista en un indice especifico 
lista.insert(2,"Diego Martinotti")

#agregando varios elementos a la lista
lista.extend([False,45])

#eliminando un elemento de la lista (por su indice)
lista.pop(0) #-1 para eliminar el ultimo elemento de la lista, -2 para eliminar el anteultimo, y asi sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove("hola")

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de la lista (no los ordena, solo los da vuelta)
lista.reverse()

#eliminda todo los elementos de la lista
lista.clear()

print(lista)