"""
Define una lista con los valores [1, 2, 3, 4, 5] e imprime el tamaño de la misma.
Luego genera un número aleatorio  entre el 1 y 10, agrega el nuevo valor en la lista.

Imprime cuantas veces se encuentra el valor nuevo en la lista.

"""
my_array = [1, 2, 3, 4, 5]
print(f"Longitud: {len(my_array)}")
import random
numero = random.randint(0,10)
print(f"Numero random: {numero}")
my_array.append(numero)
print(my_array)
carry = 0
for var in range(len(my_array)-1):
    if my_array[var] == numero:
        carry += 1
print(f"El numero random se repitio {carry} veces")