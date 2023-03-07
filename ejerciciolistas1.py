
def exists(myc: str, yourlist:    list):
    for number in yourlist:
        if myc == yourlist:
            print(f"Tu pais si se encuentra en la lista, pais: {myc}")


paises = ["México", "Venezuela", "Argentina", "Brasil", "Colombia", "Panama"]
paises.append("Chile")
paises.sort()
print(paises)
exists("Venezuela",paises)