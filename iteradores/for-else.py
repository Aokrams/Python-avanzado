# podemos usar else al final de un for para decir que haga algo cuando el for termine de iterar todo
# si utilizamos break antes del else este no se imprimira
lista_nombres = ["Brandon", "Ramsen", "Sandys", "Dorado"]

for nombre in lista_nombres:
    print(nombre)
    if nombre == "Sandys":
        break
else:
    print("Se a terminado la iteracion de los nombres")