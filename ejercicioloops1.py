"""Escribe un script que dado un número permita calcular la sumatoria de todos los números
que lo preceden desde cero. Ejemplo: número = 5 resultado = 1+2+3+4+5"""

my_value = int(input("Ingrese un numero: "))
def sumatoria(numero,var,total):
    while numero > 0:
        var = var + 1
        numero = numero - 1
        total += var
    return total
print(f"La sumatoria de todos los numeros que lo preceden desde cero es {sumatoria(my_value,0,0)}")