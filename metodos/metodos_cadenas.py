cadena1= "Hola soy Dalto"
cadena2= "Bienvenido maquinola"

# dir() devuelve la lista de atributos validos del objeto pasado, para que te lo muestre hay que envolverlo en print()
dir(cadena1)
#print(dir(cadena1))

#convierte en mayusculas
mayusc= cadena1.upper()

#convierte a minusculas
minusc= cadena1.lower()

#primera letra en mayuscula
primera_letra_mayusc= cadena1.capitalize()

#buscamos una cadena adentro de otra cadena, si no hay coincidencias devuelve -1
busqueda_find= cadena1.find("D")

#buscamos una cadena adentro de otra cadena, si no hay coincidencias lanza una exepcion(error)
busqueda_index= cadena1.index("D")

print(primera_letra_mayusc)