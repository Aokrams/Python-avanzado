import csv

columnas = ["nombre", "apellido", "edad"]
dato = ["Brandon", "Lopez", 22]

datos_lista = [
    ["Juan", "Lopez", 51],
    ["Teresa", "Villa", 57],
    ["Yeimy", "Lopez", 30],
    ["Brandon", "Lopez", 22]
    
]
datos_dicc = [
    {"nombre": "Juan", "apellido": "Lopez", "edad": 51},
    {"nombre": "Teresa", "apellido": "Villa", "edad": 57},
    {"nombre": "Yeimy", "apellido": "Lopez", "edad": 30},
    {"nombre": "Brandon", "apellido": "Lopez", "edad": 22}
]

# para enviar un conjunto de datos utilizamos writerows en vez de writerow
# el parametro newline="" despues de "w" en open sirve para que no se salte una linea 
# para enviar los datos desde un diccionario utilizamos csv.dictwriter() y como segundo parametro 
# usamos fieldnames y despues le decimos las columnas con writeheader() vacio
# ademas usamos writerows para poner el diccionario
with open("./archivos-CSV/datos.csv", "w", newline="") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=columnas)
    writer.writeheader()
    writer.writerows(datos_dicc)