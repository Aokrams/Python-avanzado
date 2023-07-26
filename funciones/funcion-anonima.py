# las funciones anonimas son funciones sin nombre y solo argumentos, en python se llaman
# funciones lambda 
# asi se definen
# sirben para realizar tareas simples y que no se repitan mucho a lo largo del codigo
lambda num: num * 3

# otra forma es hacerlo entre parentesis con los parametros dados en otro parentesis
print((lambda num1: num1 *5)(2))

# tambien podemos ponerle esta funcion a una variable
multiplicacion = lambda num: num * 2 

print(multiplicacion(2))

print(multiplicacion(7))