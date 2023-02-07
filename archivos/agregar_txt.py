with open("archivos\\texto_de_dalto.txt","a",encoding="utf-8") as archivo:
    for i in range(5):
      #agregando lineas
      archivo.write(f"Linea {i+1} agregada\n")
   