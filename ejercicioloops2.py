"""Escribe un script que dado dos números permita mostrar todos los números que existen entre ambos.
Ejemplo:
numero_a = 8
numero_b = 5
Resultado: 6,7"""

my_value_a = int(input("Ingrese un numero A: "))
my_value_b = int(input("Ingrese un numero B: "))

if my_value_a > my_value_b:
    while (my_value_a - my_value_b) != 1 :
        my_value_b = my_value_b + 1
        print(my_value_b)
else:
    while (my_value_b - my_value_a) != 1:
        my_value_a = my_value_a + 1
        print(my_value_a)