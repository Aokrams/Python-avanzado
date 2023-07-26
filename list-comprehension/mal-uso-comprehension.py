# caso 1: crear una lista para que sume los elementos de una lista muy grande 
# (comprehension requiere crear una lista)
total = sum([num for num in range(100)])
print(total)

# correccion: no es necesario crear una lista dentro de sum() para obtener su resultado
total1 = sum(num for num in range(100))
print(total1)


# caso 2: cuando queremos imprimir cada elemento de una lista
[print(element) for element in range(10)]

# correccion: para imprimir los elementos de una lista usamos el for 
for element in range(10):
    print(element)


# caso 3: cuando tenemos una lista que tiene listas anidadas dentro y quereos imprimir cada elemento
# en una lista, esto seria algo complejo de leer por lo cual no se usa asi
lista_anidada = [[1, 2], [3, 4], [5, 6]]

valores_lista = [numero for elemento in lista_anidada for numero in elemento]
print(valores_lista)

# correccion: para hacer esto utilizaremos un for dentro de otro for ya que es mucho mas legible
lista_anidada1 = [[1, 2], [3, 4], [5, 6]]
lista_numeros = []

for elemento in lista_anidada1:
    for numero in elemento:
        lista_numeros.append(numero)
    
print(lista_numeros)