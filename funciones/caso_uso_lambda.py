# un caso de uso es usar filter sobre una lista para saber algo de esta
# en este caso la funcion filtra los numeros pares de la lista 
# se usa list() para que los convierta en lista, se usa filter() para que los filtre por pares
lista_numeros = [1,2,3,4,5,6,7,8]

lista_pares = list(filter(lambda numero: numero %2 == 0, lista_numeros))
print(lista_pares)

# otro caso es usar map() para hacerle algo a una lista de numeros 
# en este caso multiplicaremos todos los numeros por 10 y los pondremos en la lista
nueva_lista = list(map(lambda numero: numero *10, lista_numeros))
print(nueva_lista)

# LAS FUNCIONES LAMBDA NO SON RECOMENDADAS POR LA COMUNIDAD YA QUE ES DIFICIL DE LEER Y ENTENDER
# POR LO CUAL SOLO SE USAN POCOS VECES Y PARA COSAS MINIMAS