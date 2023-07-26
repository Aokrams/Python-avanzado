# logging sirve para hacer registro de nuestras funciones y para hacer los seguimientos de errores 
# desde el registro
import logging

# logging toma a warning como primero a mostrar ya que es su primer nivel 
# para cambiar el primer nivel de logging hacemos lo siguiente
# basicconfig tambien sirve para crear nuestro registro de logs al poner el parametro filename
# basicconfig se define una unica vez en el archivo
# hay otro parametro que es filemode sirve para sobreescribir los registros del log y que no
# se agreguen los mismos cada vez que corramos el programa, se escribe asi filemode="w"
logging.basicConfig(level=logging.DEBUG, filename="./logging/ejemplo_logs.log", filemode="w")

logging.debug("Log de debuging")
logging.info("Log informativo")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error critico")