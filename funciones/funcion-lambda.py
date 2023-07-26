# un ejemplo para saber que funcion podemos convertirla en una funcion lambda es ver 
# cuan larga es la funcion o cuan sencilla es, en este caso la funcion separar_por_impar
# no la podemos hacer lambda ya que es muy extensa y compleja, en cambio la funcion
# calcular_area_cuadrado podemos hacerla lambda ya que es corta y solo hace una cosa
def separar_por_impar(lista_numeros):
    pares = []
    impares = []
    for numero in lista_numeros:
        if numero %2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

def calcular_area_cuadrado(lado):
    return lado ** 2

# para hace la funcion calcular_area_cuadrado en una funcion lambda haremos lo siguiente
area_cuadrado = lambda num: num ** 2

print(area_cuadrado(3))