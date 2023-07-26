# para leer un archivo json haremos lo siguiente
# importar json
# abrir el archivo json en su ruta
# definir una variable con json.load() parq eue el archivo cargue
# luego lo imprimimos o usamos de otra manera
import json

with open("./archivos-json/persona.json", "r") as archivo_persona:
    datos_persona = json.load(archivo_persona)

print(type(datos_persona))
print(datos_persona)