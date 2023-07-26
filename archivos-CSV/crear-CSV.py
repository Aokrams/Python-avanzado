# para crear una archivo CSV primero importaremos la libreria csv, luego definiremos una ruta
# que sera donde estara el archivo en este caso estara en esta misma carpeta
# luego definiremos que el archivo estara abierto para escribir y pasaremos como parametro la ruta y
# "w" que es escribir

# para definir una ruta podemos hacerlo de varias formas
# aqui importaremos la libreria os para las rutas
import csv
import os

ruta = "./archivos-CSV/csv_vacio.csv"
ruta_absoluta = "C:\\Users\\Usuario\\Desktop\\Python avanzado\\archivos-CSV\\csv_vacio.csv"
ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio.csv")

print(ruta_absoluta)
print(ruta_absoluta_os)
# archivo_abierto = open(ruta, "w")
# writer = csv.writer(archivo_abierto, delimiter=",")
# archivo_abierto.close()