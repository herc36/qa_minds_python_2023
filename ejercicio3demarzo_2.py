"""
Define una lista de 9 registros con valores aleatorios del 1 al 9.

Recorre la lista en búsqueda de números repetidos.
Si existe un número repetido cancela el proceso y manda un mensaje indicando cuál número está repetido.
De lo contrario, muestra un mensaje que indique que no existen números repetidos.
"""
import random
my_array = []
for var in range(9):
    numrdm = random.randint(0, 9)
    print(f"Numero random: {numrdm}")
    my_array.append(numrdm)
print(my_array)
for var in my_array:
    if my_array.count(var) > 1:
        print(f"El numero {var} se repite {my_array.count(var)} veces")
        break
else:
    print(f"No hay numeros negativos")

