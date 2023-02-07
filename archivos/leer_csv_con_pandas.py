import pandas as pd

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv('archivos\\archivo_csv.csv')

#obteniendo los datos de la columna nombre
nombres = df["nombre"]

