with open("archivos\\texto_de_dalto.txt","w",encoding="utf-8") as archivo:
   #sobreescribiendo el archivo
   #archivo.write("fsdfsdfsdfsdf")
   
   #agregando dos lineas con writelines
   archivo.writelines([" - Hola maestro como andas\n"," - misericordia\n"])
   
   #agregando otras 2 lineas
   archivo.writelines([" - No se porque dijiste eso\n"," - yo tampoco\n"])
   
   