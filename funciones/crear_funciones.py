#creando una funcion simple
def saludar():
   print("Hola como estas")
   
#ejecutando la funcion simple
saludar()

#creando una funcion que tenga parametros
def saludar(nombre,sexo):
   sexo=sexo.lower()
   if (sexo == "mujer"):
      adjetivo ="reina"
   elif(sexo == "hombre"):
      adjetivo = "titan"
   else:
      adjetivo = "amor"
      
   print(f"Hola {nombre}, mi {adjetivo} como andas?")
   
saludar("diego","hombre")

#crear funciones que nos retorne multiples valores
def crear_contraseña_random(num):
   chars = "abcdefghij"
   num_entero= str(num)
   num = int(num_entero[0])
   c1= num -2
   c2 =num
   c3=num -5
   contraseña= f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
   return contraseña,num

#desempaquetando la funcion
password,primer_numero= crear_contraseña_random(981)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}") 
print(f"el numero utilizado para crearla fue: {primer_numero}")