import datetime
day = int(input("Ingrese su el dia de su fecha de nacimiento porfavor: "))
month = int(input("Ingrese su el mes de su fecha de nacimiento porfavor: "))
year = int(input("Ingrese su el año de su fecha de nacimiento porfavor: "))

currentdate = datetime.date.today()
currentyear = currentdate.year
currentmonth = currentdate.month

if month > currentmonth:
    currentyear = currentyear-1
    print(f"Usted tiene la edad de {currentyear - year} y no ha celebrado su cumpleaños aun este año")
else:
    print(f"Usted tiene la edad de {currentyear - year} y ya ha celebrado su cumpleaños este año")

if year >= 1920 and year <= 1939:
    print(f"Usted forma parte de 'La generación silenciosa'")
elif year >= 1940 and year <= 1959:
    print(f"Usted forma parte de 'Los baby boomers'")
elif year >= 1960 and year <= 1979:
    print(f"Usted forma parte de 'Generación X'")
elif year >= 1980 and year <= 1989:
    print(f"Usted forma parte de 'Generación Y o millennials'")
else:
    print(f"Usted forma parte de 'Generación Z'")