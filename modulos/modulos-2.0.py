#si el modulo estuviera dentro de una carpeta en la misma ruta se importa asi
#import funciones_buenas.saludar as m_saludar

#print(m_saludar.saludar("Diego"))

import sys
#de esta manera verificamos las rutas de nuestro proyecto
#print(sys.path)

#para agregar una nueva ruta de la carpeta funciones_buenas y acceder a su funcion saludar se hace de esta manera
sys.path.append('C:\\Users\\Diegote\\Desktop\\Curso de Python Dalto\\funciones_buenas')

import saludar as modulo_saludo #parece que nos da error pero no es un error

print(modulo_saludo.saludar("Diego"))