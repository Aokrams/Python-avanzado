# las peticiones se hacen importando requests y son los get, post, put, delete
import requests

# usa una direccion de url real (por si acaso)
# podemos buscar coincidencia utilizando query params
respuesta = requests.get(
    "https://api.github.com",
    params={"q": "python"}
    )
# para ver los header de respuesta se escribe .headers
# para saber el codigo de estado de respuesta se escribe .status_code
# .content entrega los datos de manera bit 
# .text entrega los datos en forma de texto
# .json()[""] entrega los datos en forma de diccionario usando llaves y corchetes para llamar algo
# en especifico 
print(respuesta.json())

# podemos pedirle solo algunos datos en este caso solo las llaves de el json entregado 
# con anterioridad, lo entregaria con dict_keys()
datos = respuesta.json()
print(datos.keys())