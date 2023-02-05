diccionario = {
   "nombre": "lucas",
   "apellidos": "dalto",
   "subs":1000000
}

#nos devuelve un objeto dict_item (que se usa para iterar)
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua sin tirar una excepción)
valor_de_diego = diccionario.get("diego")

#eliminando un elemento del diccionario
diccionario.pop("apellido")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

#eliminando todo del diccionario
diccionario.clear()

print(diccionario_iterable)