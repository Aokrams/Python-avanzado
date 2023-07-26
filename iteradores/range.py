# range() sirve para crear un tipo range que empiece en un numero y termine en otro 
"""
range(inico, fin, paso)
"""

# utilizo list() pra que lo convierta en una lista
# recuarda que el ultimo numero es menos 1 ya que empieza desde el cero
# imprime: [0, 1, 2, 3, 4]
rango_1 = range(5)
print(list(rango_1))

# aqui le digo que empieze con el 5 y termine en el 10
# imprime: [5, 6, 7, 8, 9]
rango_2 = range(5, 10)
print(list(rango_2))

# aqui le digo que empieze en el 3, termine en el 10 y sea cada 2 numeros
# imprime: [3, 5, 7, 9]
rango_3 = range(3, 10, 2)
print(list(rango_3))

# podemos usar estas variables en un ciclo for 
for elemento in rango_3:
    print(elemento)