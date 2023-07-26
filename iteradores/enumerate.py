# enumerate devuelve el indice de los iterables que se le dan como parametros
# ademas podemos decirle desde que numero empiece a enumerar 
"""
enumerate(iterable, start=0)
"""

nombres = ["Juan", "Teresa", "Yeimy", "Brandon", "Dorado"]

nombres_enumerados = enumerate(nombres, start=4)
print(list(nombres_enumerados))

# tambien se puede usar enumerate en un for
for indice, nombre in enumerate(nombres, start=1):
    print(indice, nombre)