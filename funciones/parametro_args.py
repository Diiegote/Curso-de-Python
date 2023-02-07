#forma no optima de sumar valores
#def suma(lista):
#      numeros_sumados=0
#      for numeros in lista:
#            numeros_sumados= numeros_sumados + numeros
#      return numeros_sumados

#resultado = suma([5,5,3,5,8])

#forma optima de sumar valores con el parametro arg (*arg)
def suma(*numeros):
   return sum(numeros)

resultado= suma(5,6,2)
print(resultado)

#lo mismo que arriba y agregando dos parametros (tener en cuenta que los parametros adicionales van antes del *arg)
def suma(nombre,*numeros):
   return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado= suma("diego",5,6,2)
print(resultado)