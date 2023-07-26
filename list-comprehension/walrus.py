# walrus permite definir una variable con un valor dado en el momento en que la usamos
# sin necesidad de definirla con anterioridad
# se define asi:  (nombre_variable := funcion o valor)
def calcular_cuadrado(lado):
    return lado ** 2

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = []
for numero in lista_numeros:
    """ 
    por ejemplo comentamos la definicion de cuadrado y el if que lo usaba
    y definimos cuadrado en el mismo if 
    """

    # cuadrado = calcular_cuadrado(numero)
    # if cuadrado % 2 == 0:
    if (cuadrado := calcular_cuadrado(numero)) % 2 == 0:
        lista_pares.append(cuadrado)
        print(f"El cuadrado de {numero} es {cuadrado}, es un numero par")
    else:
        print(f"El cuadrado de {numero} es {cuadrado}, es un numero inpar")
print(lista_pares)

# se puede usar en todas partes por ejemplo en un comprehension
# esto seria lo mismo que el ejercicio de arriba
pares_lista = [cuadrado for numero in lista_numeros if (cuadrado := calcular_cuadrado(numero)) % 2 == 0]
print(pares_lista)