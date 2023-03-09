"""
QA Minds Labs estaría necesitando de un sistema que permita administrar sus cursos.

En este sentido el sistema debe contar con la posibilidad de crear un  Curso, el cual tendrán un nombre,
cantidad de alumnos, un estado y cantidad de clases.

El sistema debe poder dar de alta un Curso.

El sistema debe permitir buscar un curso y poder modificar su estado (Ejemplo: de No Iniciado a Activo)

El sistema debe permitir mostrar TODOS los Cursos existentes, como también la posibilidad de mostrar toda la información del curso.
"""


def add_course(lst: list):
    print("|" * 80)
    print("Agregar nuevo curso:")
    print("|" * 80)
    nombre = input("Nombre del curso: ")
    ca = input("Cantidad de alumnos: ")
    estado = input("Estado del curso(Escriba 'Activo' o 'No Iniciado): ")
    cc = input("Cantidad de clases: ")
    nueva_entrada = {
        "nombre": nombre,
        "cantidad_de_alumnos": ca,
        "estado": estado,
        "cantidad_de_clases": cc
    }
    lst.append(nueva_entrada)


def search(lst: list):
    if len(lst) > 0:
        for value in range(len(lst)):
            name = lst[value].get("nombre")
            print(f"Curso #{value+1}: {name}\n")
        print("Desea mostrar toda la informacion de un curso en especifico?")
        answer = input("Escriba 'YES' para mostrarla o 'NO' para salir al menu principal: ")
        if answer == "YES":
            for value in range(len(lst)):
                name = lst[value].get("nombre")
                print(f"Ingrese la opcion '{value}' para escoger el curso: {name} ")
            opc = int(input(f"Opcion: "))
            print(f"\n")
            for key, val in lst[opc].items():
                 print(f"{key} = {val}")
        elif answer == "NO":
            print("Saliendo al menu principal...")
        else:
            print(f"Operacion no soportada: {answer}")
        print(f"\n")
    else:
        print("Aun no hay cursos registrados\n")
def edit(lst: list):
    if len(lst) > 0:
        print("De cual curso quiere editar un dato: ")
        for value in range(len(lst)):
            name = lst[value].get("nombre")
            print(f"Ingrese la opcion '{value}' para escoger el curso: {name} ")

        opc = int(input(f"Opcion: "))
        name = lst[opc].get("nombre")
        print("Que dato desea modificar:\n1.-Cantidad de alumnos\n2.-Estado\n3.-Cantidad de clases: ")
        selection = int(input(f"Opcion: "))
        if selection == 1:#Cantidad de alumnos
            status = lst[opc].get("cantidad_de_alumnos")
            print(f"El numero de alumnos del curso {name} es: {status}\n")
            nuevoestado = input("Ingrese el nuevo numero de alumnos: ")
            lst[opc]["cantidad_de_alumnos"] = nuevoestado
            print(f"Se actualizo con exito el estado del curso {name} a '{nuevoestado}'\n")
        elif selection == 2: #Estado
            status = lst[opc].get("estado")
            print(f"El numero de clases del curso {name} es: {status}\n")
            nuevoestado = input("Ingrese el estado al que desea cambiarlo('Activo' o 'No Iniciado'): ")
            lst[opc]["estado"] = nuevoestado
            print(f"Se actualizo con exito el estado del curso {name} a '{nuevoestado}'\n")

        elif selection == 3:#Cantidad de clases
            status = lst[opc].get("cantidad_de_clases")
            print(f"El estado del curso {name} es: {status}\n")
            nuevoestado = input("Ingrese el nuevo numero de alumnos: ")
            lst[opc]["cantidad_de_clases"] = nuevoestado
            print(f"Se actualizo con exito el estado del curso {name} a '{nuevoestado}'\n")
        else:
            print(f"Operacion no soportada: {selection}")

    else:
        print("Aun no hay cursos registrados\n")
def delete(lst: list):
    if len(lst) > 0:
        print("Que curso desea eliminar: ")
        for value in range(len(lst)):
            name = lst[value].get("nombre")
            print(f"Ingrese la opcion '{value}' para escoger el curso: {name} ")

        opc = int(input(f"Opcion: "))
        print(f"Eliminando el curso {name}...")
        lst.pop(opc)
    else:
        print("Aun no hay cursos registrados\n")
CURSOS = []  # Es una lisa de diccionarios

ACTIONS = ("ADD","SEARCH","EDIT","DELETE","EXIT")

while True:
    print("\nBienvenido al menu escoja una de las siguientes opciones\n\nPara dar de alta un curso escriba 'ADD'\n"
          "Para buscar entre todos los cursos existentes escriba 'SEARCH'\nPara editar la informacion de un curso escriba 'EDIT'\n"
          "Para eliminar un curso del registro escriba 'DELETE'\nPara salir escriba 'EXIT'\n")
    actions_list = " | ".join(ACTIONS)
    action = input(f"Seleccione una accion: {actions_list}\n")
    if action == ACTIONS[0]:
        add_course(CURSOS)
    elif action == ACTIONS[1]:
        search(CURSOS)
    elif action == ACTIONS[2]:
        edit(CURSOS)
    elif action == ACTIONS[3]:
        delete(CURSOS)
    elif action == ACTIONS[4]:
        print("Cerrando programa...")
        break
    else:
        print(f"Operacion no soportada: {action}")