"""
Dada una lista de Poker Planning [0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, 100 ] indique:
- Cuantos de estos números son pares
- Cuantos son divisibles por el numero anterior y que de un resultado entero mayor que cero. Ejemplo 2 / 1 = 2.
- Cual seria la sumatoria de todos los números.
"""
pp = [0,0.5,1,2,3,5,8,13,20,40,100]
np = 0
dp = 0
carry = 0
for var in range(len(pp)):
    carry += pp[var]
    if pp[var] % 2 == 0:
        np += 1
    if var > 0:
        if pp[var-1] != 0:
            if (pp[var] % pp[var-1]) == 0:
                dp += 1
print(f"Numeros pares: {np}")
print(f"Numeros divisibles por el numero anterior y que de un resultado entero mayor que cero: {dp}")
print(f"Suma total: {carry}")