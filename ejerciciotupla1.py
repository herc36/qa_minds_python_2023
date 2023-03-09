"""
Define una tupla con los valores [1, 2, 3, 4, 5] e imprime el tamaño de la misma.
Luego dado un número aleatorio  entre el 1 y 5 recorrer la tupla
e imprime todos los números hasta que coincida el número generado.
"""
tupla = (1, 2, 3, 4, 5)
print(f"El tamano de la tupla es {len(tupla)}")
import random
numrdm = random.randint(1, 5)
print(f"Numero random: {numrdm}")
for num in tupla:
    print(num)
    if num == numrdm:
        print(f"Encontraste el numero: {num}")
        break
