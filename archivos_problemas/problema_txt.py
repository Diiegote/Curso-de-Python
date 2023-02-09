# 2 listas, una con nombres otra con apellidos
nombres = ["Lucas","Matias","Diego","Camila","Pedro","Roberto"]
apellidos = ["Dalto","Zing","Martinotti","Dalto","Robetix","Tarado"]

#registrar esta informacion en un TXT de forna optima

with open("archivos_problemas\\nombres_y_apellidos.txtnombres_y_apellidos.txt","w") as arch:
   arch.writelines("Los datos son:\n\n")
   [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]