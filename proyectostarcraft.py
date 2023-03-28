"""
QA Minds Lab con motivo de finalizar el módulo de Introducción a Python realizará un torneo de Starcraft 2.
Para ello requiere de un sistema que permita gestionar el torneo.
En este sentido el sistema debe contar con la posibilidad de crear Jugadores,
los cuales tendrán un nombre, un email, puntos ganados y una Raza con la que jugarán, el cual pueden ser: Terran, Zerg o Protoss.
Los jugadores también tendrán un estado el cual puede ser: Activo o Inactivo, el cual permitirá poder asociarlo a nuevas partidas o no.
Los jugadores también tendrán un contador de partidas.
Los jugadores también tendrán un contador de puntos.
"""

"""
Las Partidas tienen un nombre (Ejemplo: A vs B) y están compuestas por dos (2) Jugadores que estarán en estado Jugando.
Siempre habrá un Ganador por cada partida quien obtendrá 3 puntos y el perdedor obtendrá 1 punto y pasará a estado Inactivo,
es decir, no puede seguir jugando.

Las partidas se deben de crear de manera aleatoria tomando dos jugadores activos con el mismo número de partidas.

El resultado de la partida se debe determinar de manera aleatoria.
"""
from enum import Enum
import json

##########################################################################################
# ABSTRACIONES DEL JUGADOR
##########################################################################################
class Estado(Enum):
    ACTIVO = 1
    INACTIVO = 2

class Raza(Enum):
    TERRAN = 1
    ZERG = 2
    PROTOSS = 3

class Player:
    def __init__(self, nombre: str, mail: str, puntos: int, raza: Raza, estado: Estado, partidas: int):
        self.__nombre = nombre
        self.__mail = mail
        self.__score = puntos
        self.__race = raza
        self.__estado = estado
        self.__games = partidas

    def obtener_nombre(self):
        return self.__nombre
    def obtener_puntaje(self):
        return self.__score
    def obtener_estado(self):
        return self.__estado
    def obtener_numpartidas(self):
        return self.__games
    def cambiar_estado(self,estado):
        self.__estado = estado

    def cambiar_puntaje(self,puntos):
        self.__score = puntos

    def cambiar_partidas(self,partidas):
        self.__games = partidas
    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"(Nombre={self.__nombre}, Mail={self.__mail}, Puntos={self.__score}, Raza={self.__race}, Estado={self.__estado}, Partidas={self.__games})"


##########################################################################################
# ACCIONES DEL SISTEMA
##########################################################################################
def alta():
    raza = None
    imprimir_header("ALTA")
    nombre = input("nombre?")
    mail = input("mail?")
    #mail = "a@hotmail.com"
    puntos = 0
    while raza != "TERRAN" and raza != "ZERG" and raza != "PROTOSS":
        raza = input("raza(TERRAN, ZERG o PROTOSS)?")
        if raza != "TERRAN" and raza != "ZERG" and raza != "PROTOSS":
            print(f"Raza no soportada: {raza}\nIngrese un tipo de raza valida por favor")
    #raza = "ZERG"
    estado = "ACTIVO"
    #estado = input("estado?")
    partidas = 0
    jugador = Player(nombre, mail, puntos, Raza[raza], Estado[estado], partidas)
    JUGADORES.append(jugador)
    print(f"Jugador registrado: {jugador}")


def empezar_torneo():
    imprimir_header("EMPEZANDO TORNEO")
    juegan,onlineplayers,winner = contar_jugadores_activos()
    if onlineplayers >= 4:   #filtrar que haya mas de 4 jugadores
        if onlineplayers % 2 != 1: #filtrar que haya un numero par de jugadores
            while len(juegan)>1:
                #print(f"Se juegan -> {juegan}")#numerodegames = numero_de_participaciones(juegan) #guardar el numero de participaciones de los jugadores
                playerA, playerB = combate(juegan)
                partidasA = JUGADORES[playerA].obtener_numpartidas()
                partidasB = JUGADORES[playerB].obtener_numpartidas()
                JUGADORES[playerA].cambiar_partidas(partidasA + 1)
                JUGADORES[playerB].cambiar_partidas(partidasB + 1)
                import random
                numero = random.randint(0,1)
                #print(f"nmrdm{numero}")
                if numero == 0:
                    print(f"El jugador #{playerA} {JUGADORES[playerA].obtener_nombre()} ha ganado el encuentro")
                    puntosA = JUGADORES[playerA].obtener_puntaje()
                    puntosB = JUGADORES[playerB].obtener_puntaje()
                    JUGADORES[playerA].cambiar_puntaje(puntosA + 3)
                    JUGADORES[playerB].cambiar_puntaje(puntosB + 1)
                    JUGADORES[playerB].cambiar_estado("INACTIVO")
                    juegan.pop(1)
                    juegan,x,winner = contar_jugadores_activos()
                else:
                    print(f"El jugador #{playerB} {JUGADORES[playerB].obtener_nombre()} ha ganado el encuentro")
                    puntosB = JUGADORES[playerB].obtener_puntaje()
                    puntosA = JUGADORES[playerA].obtener_puntaje()
                    JUGADORES[playerB].cambiar_puntaje(puntosB + 3)
                    JUGADORES[playerA].cambiar_puntaje(puntosA + 1)
                    JUGADORES[playerA].cambiar_estado("INACTIVO")
                    juegan.pop(0)
                    juegan,x,winner = contar_jugadores_activos()

            else:
                print(f"Partidas finalizadas")
                print(f"El ganador de todo el torneo es: {JUGADORES[winner].obtener_nombre()}")

        else:
             print(
                    f"Se necesita un numero par jugadores para empezar el torneo, acualmente hay {onlineplayers} "
                     f"jugadores activos")
    else:
             print(
                    f"Se necesitan al menos 4 jugadores para empezar el torneo, acualmente hay {onlineplayers} jugadores"
                    f" activos")


def exportar_registros():
    imprimir_header("EXPORTAR REGISTROS")
    x1,onlineplayers,ganador = contar_jugadores_activos()
    if onlineplayers > 0:
        if ganador is not None:
            copiadata = JUGADORES.copy()
            with open("starcraft.json", "w") as file:
                json.dump(f"El ganador de toda la partida es el jugador #{ganador} {JUGADORES[ganador].obtener_nombre()} Aqui tienes toda la tabla de puntajes: \n {copiadata}", file)
                print(f"Los regsitros han sido exportados, se ha determinado un ganador de la partida y se cerrara la misma, gracias por jugar STARCRAFT")
                exit()
        else:
            print(f"Aun no hay torneos realizados para definir un ganador")
    else:
        print(f"Aun no hay jugadores registrados para definir un ganador")


def imprimir_header(header: str):
    print(f"{40 * '='} {header} {40 * '='}")


def contar_jugadores_activos():
    onlineplayers = 0
    juegan = []
    winner = None
    for index, player in enumerate(JUGADORES):
        if player.obtener_estado() == Estado["ACTIVO"]:
            onlineplayers += 1  #contar jugadores activos
            juegan.append((index,player.obtener_numpartidas()))#guardar el index de jugador activo
            if len(juegan) == 1:
                winner = index
    #print(f"Indexes que participan {juegan}")

    return juegan,onlineplayers, winner

def numero_de_participaciones(juegan):
    numerodegames = []
    for num in juegan:
        participaciones = JUGADORES[num].obtener_numpartidas()
        numerodegames.append(participaciones)
    return numerodegames

def combate(juegan):
    print(f"Matchmaking....")
    sorted_juegan=juegan.copy()
    sorted_juegan.sort(key = lambda x: x[1])
    #print(f"Orden {sorted_juegan}")
    playerA=sorted_juegan[0][0]#cambie cero por 1
    playerB=sorted_juegan[1][0]
    print(f"El jugador #{playerA} {JUGADORES[playerA].obtener_nombre()} luchara contra el jugador #{playerB} {JUGADORES[playerB].obtener_nombre()}")
    return playerA, playerB

##########################################################################################
# CONTROL PRINCIPAL
##########################################################################################
JUGADORES = []

MENU = {
    "alta": alta,
    "empezar torneo": empezar_torneo,
    "exportar registros": exportar_registros,
}

OPTIONS = ' | '.join(MENU.keys())

while True:
    action = input(f"Que accion deases realizar? {OPTIONS}\n")
    if action in MENU.keys():
        MENU[action]()
    else:
        print(f"Accion not soportada: {action}")