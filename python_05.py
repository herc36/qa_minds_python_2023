
def suma(numa,numb):
    print(f"Operacion Suma: {numa} + {numb}")
    return numa + numb
def resta(numa,numb):
    print(f"Operacion Resta: {numa} - {numb}")
    return numa - numb
def multiplicacion(numa,numb):
    print(f"Operacion Multiplicacion: {numa} * {numb}")
    return numa * numb
def division(numa,numb):
    print(f"Operacion Division: {numa} / {numb}")
    return numa / numb
def modulo(numa,numb):
    print(f"Operacion Modulo: {numb} % {numa}")
    return numb % numa
def entero(val1):
    print(f"Convertir el numero: {val1} a entero")
    return (int(val1))
def flotante(val2):
    print(f"Convertir el numero: {val2} a flotante")
    return (float(val2))
def temperatura(grados):
    print(f"Convertir {grados}°C a °F")
    return ((grados * 9/5) + 32)
def es_par(numero):
    if ((numero%2)==1):
        print(f"El numero {numero} es impar")
    else:
        print(f"El numero {numero} es par")
    return (bool((numero/2)))

num1 = int(input("Numero A: "))
num2 = int(input("Numero B: "))
temp = float(input("Ingrese temperatura en °C: "))
var1 = float(input("Ingrese un numero para convertir a entero: "))
var2 = input("Ingrese un numero para convertir a flotante: ")
numero = int(input("Ingrese un numero para saber si es par o impar: "))
print(f"Resultado suma: {suma(num1,num2)}")
print(f"Resultado resta: {resta(num1,num2)}")
print(f"Resultado multiplicacion: {multiplicacion(num1,num2)}")
print(f"Resultado division: {division(num1,num2)}")
print(f"Resultado modulo: {modulo(num1,num2)}")
print(f"Resultado conversion a entero: {entero(var1)}")
print(f"Resultado conversion a flotante: {flotante(var2)}")
print(f"Resultado: {temperatura(temp)} °F")

es_par(numero)