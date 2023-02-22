mes = int(input("Ingrese el numero del mes del año en el que se encuentra: "))

if mes < 1 or mes > 12:
    print("El mes ingresado no existe\nPorfavor ingrese un numero del 1 al 12 e intente de nuevo\n'La Gerencia'")
elif mes >= 3 and mes <= 5:
    print("La estacion en la que se encuentra es Primavera")
elif mes >= 6 and mes <= 8:
    print("La estacion en la que se encuentra es Verano")
elif mes >= 9 and mes <= 11:
    print("La estacion en la que se encuentra es Otoño")
else:
    print("La estacion en la que se encuentra es invierno")