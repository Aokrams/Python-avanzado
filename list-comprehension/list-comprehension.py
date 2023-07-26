# es una manera de construir listas o objetos iterables usando solo 1 linea de codigo
"""
lista = [ expresion(elemento) for elemento in objeto_iterable ]
"""

def calcular_cuadrado(lado):
    return lado ** 2

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = []

for numero in lista_numeros:
    cuadrado = calcular_cuadrado(numero)
    lista_cuadrados.append(cuadrado)

print("ciclo for", lista_cuadrados)

# list comprehension crea una lista y le dice que es lo que tiene que hacer dentro de los corchetes
# aqui utiliza el for dentro y llama a la otra lista
lista_comprehension = [numero ** 2 for numero in lista_numeros]

print("list comprehension", lista_comprehension)