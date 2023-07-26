# zip() sirve para unir 2 listas en tuplas, con cada indice en su respectiva posicion
# si agregamos otro elemento y no corresponde a lo largo de la otra lista, solo imprimira
# la cantidad de tuplas de el numeros mas bajo de elementos de una de las listas
nombres = ["Juan", "Teresa", "Yeimy", "Brandon", "Dorado"]
apellidos = ["Lopez", "Villa", "Lopez", "Lopez"]

zip_1 = list(zip(nombres, apellidos))
print(zip_1)

# tambien se pueden desempaquetar los elementos ya juntados con zip() usando zip(*)
nombres_separados, apellidos_separados = zip(*zip_1)
print(nombres_separados)
print(apellidos_separados)

# tambien podemos usar zip en un for 
for nombre, apellido in zip(nombres, apellidos):
    print(nombre, apellido)