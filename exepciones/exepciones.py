# creando funcion que suma numeros
def suma_dos():
   while True:
      #pidiendo numeros
      a= input('Numero 1: ')
      b= input('Numero 2: ')
      #intentando convertirlos a entero y sumarlos
      try:
         resultado = int(a) + int(b)
         #si lanzo una exepcion, pedirle que reingrese los datos
      except ValueError as e:
         print("Te pedi un numero")
         print(f"Error: {e}")
      #si todo sale bien terminamos el bucle
      else:
         break
      #el finally se ejecuta siempre
      finally:
         print("Esto se ejecuta siempre")
         
      #mostrando el resultado
   return resultado
   
print(suma_dos())