#creando un conjunto con set()
conjunto = set(["Dato 1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato 1", "Dato 2"])
conjunto2 = {conjunto1,"Dato 3"}

#Teoria de conjuntos
conjunto1 = {1,2,3,5,7}
conjunto2 = {1,3,7}

#Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1) 
resultado = conjunto2 <= conjunto1 # verifica lo mismo que la variable de arriba pero sin usar el issubset

#Verificando si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2

#verificar si hay algun numero en comun (si hay alguno devuelve false, si no hay ninguno devuelve true)
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)