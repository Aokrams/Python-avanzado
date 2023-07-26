# comprehension nos permite crear set o diccionarios no solo listas
lista_numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 2, 3, 6]

# aqui creamos un set con los numeros de la lista_numeros y solo agregamos los pares
# le decimos que queremos el numero luego el for y luego el if con la condicion
set_pares = {numero for numero in lista_numeros if numero % 2 == 0}
print(set_pares)

# para hacer un diccionario utilizamos un str vocales y definimos primero la llave
# en este caso usaremos las letras del str con .lower() que convierte las letras en 
# minuscula y : luego de definir la llave para que la reconosca como llave, 
# y el valor de la llave se escribe despues, usaremos .upper() que convierte las letras en mayuscula
# para definirla como valor de la llave, luego usamos el for y lo imprimimos
vocales = "aeiou"
diccionario = {vocal.lower(): vocal.upper() for vocal in vocales}
print(diccionario)