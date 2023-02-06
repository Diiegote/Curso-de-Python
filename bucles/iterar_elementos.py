animales = ["pez","gato","perro","loro","vaca","dinosaurio"]

numeros = [1,2,3,46,78,145]

#recorriendo la lista animales
for animal in animales:
   print(f"Ahora la varibale animal es igual a : {animal}")
   
   
#recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
   resultado = numero *10
   print(resultado)
   
#iterando dos listas del mismo tamaño al mismo tiempo

for numero,animal in zip(numeros, animales):
   print(f"recorriendo lista1: {numero}")
   print(f"recorriendo lista2: {animal}")
   
   
#forma no optima de recorrer una lista con su indice (no funciona en conjuntos)
for num in range(len(numeros)):
   print(numeros[num])
   
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
   print(num)#de esta manera nos devuelve una tupla con indice y valor
   print(num[0])#de esta manera nos devuelve solo el indice
   print(num[1])#de esta manera nos devuelve solo el valor
   
   #de esta manera obtenemos los dos valores
   indice = num[0]
   valor= num[1]
   print(f"El indice es {indice} y el valor es {valor}")
   

#usando el else en un bucle for
for numero in numeros:
   print(f"ejecutando el ultimo blucle, valor actual: {numero}")
else:
   print("el bucle termino") #el else siempre se va a ejecutar
   
#(todo) lo anterior funciona igual para tuplas y conjuntos