import random
rdm = random.randint(0,20)
numero = rdm*2
print(f"Numero random: {numero}")
carry = 0
for number in range(1,100):
    carry += number
    if number == numero:
        print(f"La suma de todos los numeros hasta el {number} es: {carry}")