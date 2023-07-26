# en python existen 2 elemento que son break (permite romper el ciclo cuando se cumpla una condicion)
# y continue (permite saltar la siguiente parte de las instrucciones del cilo cuando se cumpla una
# condicion ) (tambien se pueden usar sin condicion pero no tendria sentido)
nombres = ["Jorge", "Brandon", "Dorado"]

for elemento in nombres:
    if elemento == "Brandon":
        break
    print(elemento)

for elemento in nombres:
    if elemento == "Brandon":
        continue
    print(elemento)