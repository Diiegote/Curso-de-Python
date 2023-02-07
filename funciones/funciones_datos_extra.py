#creando una funcion de 3 parametros

#def frase(nombre,apellido,adjetivo):
#      return f"hola {nombre} {apellido} sos muy {adjetivo}"


#utilizando keyword arguments
#frase_resultante = frase(adjetivo="capo",nombre="diego",apellido="martinotti")


#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo="tonto"):
   return f'hola {nombre} {apellido}, sos muy {adjetivo}'

frase_faltante= frase("diego","martinotti","inteligente")
print(frase_faltante)