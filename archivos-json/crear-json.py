# existen 2 cosas que se pueden hacer con los json, crearlos y usarlos
# para crear un json debemos importar json luego crear nuestro objeto
# despues definimos una variable con json.dumps() como parametro usamos el objeto creado y segundo 
# parametro si queremos indent= para indentar el json
# luego abrimos el archivo con open() y definimos su ruta junto con "w" para que podamos escribir
# luego lo difinimos y le decimos que escriba con la variable creada con json.dumps()
import json

persona = {
    "nombre": "Brandon",
    "apellido": "Lopez",
    "edad": 22
}

# tambien podemos usar dump() para crear el json pero quedaria sin identacion 
# objeto_json = json.dumps(persona, indent=2)
with open("./archivos-json/persona.json", "w") as archivo_json:
    # archivo_json.write(objeto_json)
    json.dump(persona, archivo_json)