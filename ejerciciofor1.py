import random
numero = random.randint(0,10)
print(f"Tabla del {numero}")
for tabla in range(1,11):
    total = numero * tabla
    print(f"{numero} x {tabla} = {total}")