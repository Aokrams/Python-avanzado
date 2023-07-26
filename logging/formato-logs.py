# se puede dar formato a los mensajes que nos de logging
import logging

# se le da el parametro format y entre comillas un %(levelname)s que seria el nivel de error
# lo separamos con algo en este caso - y luego %(message)s que seria lo que escribimos dentro
# del logging, %(asctime)s sirve para saber en que momento ocurrio el logging
# datefmt= sirve para darle un formato a la hora y que solo aparesca lo que queremos mostrar
# en este caso solo mostraremos la hora, minutos y segundos, no milesimas ni dia
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)

# cuando estemos en los registros necesitaremos saber mas especificamente que ocasiono el error
# y esto se mostraria en el mensaje asi
nombre = "Brandon"
logging.error(f"{nombre} ocasiono el error")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error critico")

# tambien podemos usar los logs en ecepciones (bloques de codigo que capturan errores)
try:
    division = 4 / 0
except:
    # podemos usar exception para que nos muestre el error completamente y no solo el mensaje 
    logging.exception("Division entre 0")