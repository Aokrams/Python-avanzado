# el debugging nos permite solucionar errores como su nombre indica
# podemos usar la libreria pdb en la terminal para ver que esta pasando con el codigo
# escribimos en terminal: python -m pdb nombre_archivo.extencion
# para escribir el archivo en la terminal dentro de otra carpeta primero escribimos la carpeta
# luego \ y despues el nombre del archivo: python -m pdb carpeta\archivo.extencion
# con l podemos ver todo el codigo y con q salimos del proceso

# sabemos que estamos en modo debugging ya que en la terminal nos aparece (Pdb)
# podemos definir un breakpoint (donde queremos que el codigo se detenga) 
# usando: break 5(linea_de_codigo)
# usamos continue para que el codigo se ejecute, en este caso se ejecuta hasta el breakpoint
# cada continue iterar una vez sobre el iterable y luego vuelve al segundo iterable
# next nos permite ejecutar la siguiente linea de codigo
# display nos permite ver el contenido de una variable, puede estar vacia dependiendo de 
# en que parte del codigo estemos
# undisplay nos sirve para dejar de ver lo que nombramos en el display
# restart nos permite reiniciar el codigo desde el principio, pero no borrara los breakpoints
def calcular_area_cuadrado(lado):
    area = lado * lado
    return area

numeros = [1, 4, 9]
area_numeros = []
for numero in numeros:
    area_num = calcular_area_cuadrado(numero)
    area_numeros.append(area_num)

