"""
Dada una tupla de distribución de puntos para la Fórmula 1 (25, 18, 15, 12, 10, 8, 6, 4, 2, 1 ) indique:
Cuántos de estos números son pares
Cuantos puntos se le entregan a los tres primeros.
Cual seria la sumatoria de todos los números.
"""
f1 = (25, 18, 15, 12, 10, 8, 6, 4, 2, 1 )
my_clone = list(f1)
np = 0
sum = 0
for num in f1:
    sum += num
    if num % 2 == 0:
        np += 1
my_clone.sort()

print(my_clone)