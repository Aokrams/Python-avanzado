# map sirve para modificar los elementos de una lista 
# esto se puede hacer por un for para iterar sobre cada uno de ellos y luego 
# hacerle algo a estos, pero es mas facil y rapido utilizar map como el ejemplo a continuacion
def calcular_cuadrado(lado):
    return lado ** 2

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = []

for numero in lista_numeros:
    cuadrado = calcular_cuadrado(numero)
    lista_cuadrados.append(cuadrado)

print(lista_cuadrados)

# el orden seria primero lo que queremos hacerle a los elementos de una lista (puede ser una funcion)
# y luego la lista
map_cuadrados = list(map(calcular_cuadrado, lista_numeros))

print(map_cuadrados)