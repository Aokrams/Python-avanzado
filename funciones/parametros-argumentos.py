# son funciones con un numero determinado de parametros, al usar la funcion se deben colocar los
# parametros que uno quiere utilizar y correspondan con lo que uno quiere
def sumar_numeros(numero1, numero2):
    """Esta funcion permite sumar 2 numeros"""
    suma = numero1 + numero2
    return suma

numeros_sumados = sumar_numeros(3, 7)
print(numeros_sumados)