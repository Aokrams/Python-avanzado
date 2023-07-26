# list comprehension tambien nos permite usar condicion 
"""
lista = [ expresion(elemento) for elemento in objeto_iterable if condicion ]
lista = [ expresion(condicion) for elemento in objeto_iterable ]
"""

def calcular_cuadrado(lado):
    return lado ** 2

def es_par(numero):
    return numero % 2 == 0

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

lista_cuadrados = [calcular_cuadrado(num) for num in lista_numeros]
print(lista_cuadrados)

# podemos ponerle una condicion usando if luego del for dentro del corchete
# en el siguiente caso calculara al cuadrado los elementos de la lista y luego solo pondra los que 
# son pares dentro de la lista
lista_condicion = [calcular_cuadrado(num) for num in lista_numeros if es_par(num)]
print(lista_condicion)

# tambien podemos usar un else para que en vez de acortar la lista solo con los pares, podamos 
# reemplazar los elementos que no son pares por cualquier otra cosa, en este caso con "no par"
lista_condicion_else = [calcular_cuadrado(num) if es_par(num) else "no par" for num in lista_numeros]
print(lista_condicion_else)