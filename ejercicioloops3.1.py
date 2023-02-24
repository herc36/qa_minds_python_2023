"""
Extra:
Cambia el ejercicio 3: El script tiene que adivinar el numero que esta pensando el usuario.
Muestra un numero aleatorio entre 0-10
Pregunta al usuario si ese es el numero que el selecciono. Si es el correcto terminar, de lo contrario repetir
"""
import random
numero = random.randint(0,10)
print(numero)
my_value = int(input("Ingrese un numero: "))
intento=1

while numero != my_value:
     my_value = int(input("Ingrese un numero: "))
     intento = intento+1

if numero == my_value:
    print(f"Le atinaste al numero secreto al intento numero {intento}")