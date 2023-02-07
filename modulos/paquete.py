#para que me lo reconozca como paquete necesito crear un archivo __init__.py en la carpeta paquete
import paquete.saludar as m_saludar
import paquete.saludar_raro as m_saludar_raro

print(m_saludar.saludar("Diego"))
print(m_saludar_raro.saludar_raro("martin"))

#de esta manera obtenemos dos archivos diferentes de la misma carpeta, gracias a los paquetes