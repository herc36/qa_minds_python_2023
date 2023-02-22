age = int(input("Ingrese su edad porfavor: "))
height = float(input("Ingrese su estatura porfavor: "))

if age <= 14 or height < 1.62:
    print(f'Lo siento usted no puede ingresar a la montaña rusa “Push-Pull" debido a que su edad es de '
          f'{age} y su estatura es de {height}')
else:
    print('Bienvenido a la montaña rusa “Push-Pull" diviertase')