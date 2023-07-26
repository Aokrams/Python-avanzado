# si queremos hacer funcionen que ocupen diferentes tipos de parametros debemos seguir un
# orden especifico para que no nos de error
# el orden correcto es los parametros normales, los *args y los **kwargs en este orden 
def parametros_ordenados(nombre, apellido, *args, **kwargs):
    pass

# el orden incorrecto se veria asi y daria error sobre la sintaxis
def parametros_desordenados(nombre, apellido, **kwargs, *args):
    pass