# los **kwargs se utilizan cuando queremos hacer funciones con diccionarios (json)
# aqui se itera sobre las llaves y su valor y se ocupa .items para que itere sobre los 2
def funcion_kwargs(**kwargs):
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f"llave: {llave}, valor: {valor}")
    print(kwargs["nombre"], kwargs["apellido"])

funcion_kwargs(nombre="Brandon", apellido="Lopez")