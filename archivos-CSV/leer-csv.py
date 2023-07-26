# para leer los csv primero importamos csv
import csv

# utilizamos la misma sistaxis pero "r" de reader en vez de "w" y encoding="UTF-8" que es un formato
# clasico
# luego usamos csv.reader() para leer y un for para mostrar los elementos
# si no queremos que aparesca la primera fila que es la que define a las demas
# utilizamos next(reader) antes del for para saltarnos la primera linea 
with open("./archivos-CSV/datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    # columnas = next(reader)
    # print("Columnas", columnas)
    for fila in reader:
        print(fila[0])

# tambien podemos usar dictreader para mostrar como un diccionario las columnas y datos
with open("./archivos-CSV/datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo)
    # columnas = next(reader)
    # print("Columnas", columnas)
    for fila in reader:
        print(fila["nombre"])