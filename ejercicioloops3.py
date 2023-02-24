"""
Escribe un script que dado un número aleatorio permita encontrar su valor por medio de interacción
con usuario, mostrando cuantos intentos le llevó al mismo detectarlo.
Para realizar este script será necesario utilizar la librería random
y del comando input para ingresar el número por consola.
"""

import random
numero = random.randint(0,10)
print(numero)
my_value = -1
intento=0

while numero != my_value:
     my_value = int(input("Ingrese un numero: "))
     intento = intento+1

if numero == my_value:
    print(f"Le atinaste al numero secreto al intento numero {intento}")

