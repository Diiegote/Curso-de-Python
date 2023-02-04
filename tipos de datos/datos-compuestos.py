#creando una lista (se pueden modificar)
lista= ["Lucas Dalto","Soy Dalto",True,1.85]

#creando una tupla (no se pueden modificar)
tupla=("Lucas Dalto","Soy Dalto",True,1.85)

#esto es valido
lista[3]="Maquinola"

#esto no es valido porque no se pueden modificar los datos de las tuplas
#tupla[3]="Maquinola"

#creando un conjunto(set) (no se accede al elemento por indice, no almacena datos duplicados)
conjunto={"Lucas Dalto","Soy Dalto",True,1.85}

#print(conunto[3]) -> no se puede acceder al elemento

#creando un diccionario(dict) (la estructura es key:value y separamos con comas)
diccionario={
   "nombre": "Lucas Dalto",
   "canal": "Soy Dalto",
   "esta_emocionado": True,
   "altura": 1.85,
   "dato_duplicado": "Soy Dalto"
}

print(diccionario["altura"])