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

#si es numerico, devuelve true si no devuelve false
es_numerico= cadena1.isnumeric()

#si es alfanumerico devolvemos true, si no devolvemos false 
es_alfanum= cadena1.isalpha()

#contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias= cadena1.count("Hola")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con= cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con= cadena1.startswith("o")

#si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("Hola", "Holaaaa")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")
print(cadena_separada)