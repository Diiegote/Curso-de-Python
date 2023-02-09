#creando mi propia exepcion personalizada
class MiExepcion(Exception):
   def __init__(self,err):
      print(f"Impresionante, cometiste el siguiente error: {err}")
      
      
      
#Lanzando mi propia exepcion
#raise MiExepcion("JAJAJA, persona poco culta")

#manejandola
try:
   raise MiExepcion("JAJAJA, persona poco culta")
except:
   print("Como vas a cometer ese error?")
