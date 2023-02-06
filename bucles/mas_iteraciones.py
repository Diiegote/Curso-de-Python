frutas= ["banana","manzana","pera","durazno","granada","sandia","frutilla"]
cadena="Hola Dalto"
numeros=[2,5,8,7,6]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
   if fruta == "manzana":
      continue
   print(f"Me voy a comer una {fruta}")
   
#evitar que el bucle se siga ejecutando (el else no se ejecuta tampoco)
for fruta in frutas:
   if fruta == "pera":
      break
   print(f"Me voy a comer una {fruta}")
else:
   print("terminado")
   
#recorrer una cadena de texto
for letra in cadena:
   print(letra)
   
   
#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados=[x*2 for x in numeros]
print(numeros_duplicados)