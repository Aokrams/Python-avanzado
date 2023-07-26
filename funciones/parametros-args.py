# los *args se utilizan como parametros en una funcion, cuando uno no sabe cuantos parametros 
# llevara lo que deseamos hacer, por ejemplo una funcion que quiere calcular el perimetro de 
# un objeto cuadriculado, llevaria mas o menos paramateros dependiendo de cuantos lados
# tenga el objeto, pero realizaria la misma funcion
def calcular_perimetro(*args):
    print(args)
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro

perimetro = calcular_perimetro(1, 2, 3, 4)
print(perimetro)

triangulo = calcular_perimetro(1, 2, 3)
print(triangulo)