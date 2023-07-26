# estas hacen cambios enviando nuevos datos a un servidor 
# hay una pagina que nos genera una url donde hacer peticiones sin hacer ningun
# cambio en servicios o servidores, por lo cual es muy util para practicar 
# " webhook.site " es la pagina
import requests

# la pagina nos muestra todo lo que hacemos por lo cual es muy conveniente
url = "https://webhook.site/6c381dc6-94b3-4dc6-ad90-51cf12d80a7b"
peluche = {"nombre": "pochita", "cantidad": 1}
query_params = {"nombre": "Brandon"}
respuesta = requests.post(url, data=peluche, params=query_params)
