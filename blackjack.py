import random
import time


def tirar() -> int:
    """Devulve un número aleatorio entre 1 y 6"""
    tirada = random.randint(1, 6)
    return tirada


def tirar_prob50() -> bool:
    """Devuleve True o False con una probabilidad del 50%"""
    num = random.randint(1, 2)
    if num == 1:
        return True
    return False


def tirar_IA_dificil(actitud: str) -> bool:
    """
    Determina si la IA pide carta o se planta teniendo en cuenta la actitud agresiva/defensiva
    con una probabilidad de 70/30 - 30/70
    Retora:
        True -> La IA pide carta
        False -> La IA se planta
    """
    rand = random.randint(1, 10)
    match actitud:
        case "agresiva":
            print("IA_dificil opta por una jugada agresiva")
            if rand > 3:
                return True
            else:
                return False
        case "defensiva":
            print("IA_dificil opta por una jugada defensiva")
            if rand > 7:
                return True
            else:
                return False


def quienGana(jugadores: list) -> str:
    """Devuelve quien gana y con que puntuación"""
    ganador = ""
    puntuacion = 0
    for jugador in jugadores:
        if puntuacion < jugador["puntuacion"] and jugador["puntuacion"] < 22:
            puntuacion = jugador["puntuacion"]
            ganador = jugador["jugador"]
        elif puntuacion == jugador["puntuacion"]:
            ganador = "Empate"
    return ganador, puntuacion


def construir_lista() -> list:
    """
    Devuelve una lista con los jugadores de la partida
    """
    jugadores = []
    # Humano
    while True:
        humano = input("Cuantas Humanos quieres? (minimo 1)")
        if not humano.isdigit():
            print("Error, ingrese un número valido")
            continue
        humano = int(humano)
        if humano < 1:
            print("Debe haber minimo 1 humano")
            continue
        break

    for _ in range(humano):
        jugador = {
            "jugador": "Humano",
            "puntuacion": 0,
            "plantado": False,
            "comodin_usado": False,
        }
        jugadores.append(jugador)
    # IA_FACIL
    while True:
        ia_facil = input("Cuantas IA_facil quieres? (minimo 1)")
        if not ia_facil.isdigit():
            print("Error, ingrese un número valido")
            continue
        ia_facil = int(ia_facil)
        if ia_facil <= 0:
            print("Debe haber minimo 1 ia_facil")
            continue
        break

    for _ in range(ia_facil):
        jugador = {"jugador": "IA_facil", "puntuacion": 0, "plantado": False}
        jugadores.append(jugador)
    # IA_MEDIO
    while True:
        ia_medio = input("Cuantas IA_medio quieres? (minimo 1)")
        if not ia_medio.isdigit():
            print("Error, ingrese un número valido")
            continue
        ia_medio = int(ia_medio)
        if ia_medio <= 0:
            print("Debe haber minimo 1 ia_medio")
            continue
        break

    for _ in range(ia_medio):
        jugador = {"jugador": "IA_medio", "puntuacion": 0, "plantado": False}
        jugadores.append(jugador)
    # IA_DIFICIL
    while True:
        ia_dificil = input("Cuantas IA_dificil quieres? (minimo 1)")
        if not ia_dificil.isdigit():
            print("Error, ingrese un número valido")
            continue
        ia_dificil = int(ia_dificil)
        if ia_dificil <= 0:
            print("Debe haber minimo 1 ia_dificil")
            continue
        break

    for _ in range(ia_dificil):
        jugador = {"jugador": "IA_dificil", "puntuacion": 0, "plantado": False}
        jugadores.append(jugador)

    for jugador in jugadores:
        print(jugador)
    return jugadores


def logica_humano(jugador: dict) -> dict:
    """
    Procesa la tirada del humano, recibe al jugador humano
    por parametro y lo devuelve con los cambios realizados
    """
    while True:
        if jugador["puntuacion"] == 0:
            opcion = "n"
        else:
            opcion = input("quieres plantarte? s/n: ")
        match opcion:
            case "s":
                print(f"{jugador["jugador"]} se PLANTA con {jugador["puntuacion"]}")
                jugador["plantado"] = True
                break
            case "n":
                dado = tirar()
                if dado == 6 and jugador["comodin_usado"] == False:
                    print(
                        "Has obtenido un 6, tienes la opcion de convertirlo en un 1, ¿quieres? s/n"
                    )
                    while True:
                        opcion = input()
                        match opcion:
                            case "s":
                                jugador["puntuacion"] += 1
                                jugador["comodin_usado"] = True
                                break
                            case "n":
                                jugador["puntuacion"] += 6
                                break
                            case _:
                                print("opcion no valida")
                else:
                    jugador["puntuacion"] += dado
                if jugador["puntuacion"] > 21:
                    print(f"Te has pasado con {jugador["puntuacion"]}, PIERDES!")
                    jugador["plantado"] = True
                else:
                    print(f"{jugador["jugador"]} tira {dado}")
                    print(
                        f"Puntuacion del {jugador["jugador"]}: {jugador["puntuacion"]}"
                    )
                break
            case _:
                print("opcion no valida")
                continue
    return jugador


def logica_IA_facil(jugador: dict) -> dict:
    """
    Procesa la logica de IA_facil, recibe por parametro al jugador
    y lo retorna con los cambios realizados.
    """
    if jugador["puntuacion"] < 17:
        dado = tirar()
        jugador["puntuacion"] += dado
        if jugador["puntuacion"] > 21:
            print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
            jugador["plantado"] = True
        else:
            print(f"{jugador["jugador"]} tira {dado}")
            print(f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}")
    else:
        jugador["plantado"] = True
        print(f"La {jugador["jugador"]} se PLANTA! con {jugador["puntuacion"]}")
    return jugador


def logica_IA_medio(jugador: dict) -> dict:
    """
    Procesa la logica de IA_medio, recibe por parametro al jugador
    y lo retorna con los cambios realizados.
    """
    if jugador["puntuacion"] < 17:
        dado = tirar()
        jugador["puntuacion"] += dado
        if jugador["puntuacion"] > 21:
            print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
            jugador["plantado"] = True
        else:
            print(f"{jugador["jugador"]} tira {dado}")
            print(f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}")
    elif jugador["puntuacion"] < 20:
        if tirar_prob50():
            dado = tirar()
            jugador["puntuacion"] += dado
            if jugador["puntuacion"] > 21:
                print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
                jugador["plantado"] = True
            else:
                print(f"{jugador["jugador"]} tira {dado}")
                print(f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}")
        else:
            jugador["plantado"] = True
            print(f"La {jugador["jugador"]} se PLANTA! con {jugador["puntuacion"]}")
    else:
        jugador["plantado"] = True
        print(f"La {jugador["jugador"]} se PLANTA! con {jugador["puntuacion"]}")
    return jugador


def logica_IA_dificil(jugador: dict) -> dict:
    """
    Procesa la logica de IA_dificil, recibe por parametro al jugador
    y lo retorna con los cambios realizados.
    """
    if jugador["puntuacion"] < 17:
        dado = tirar()
        jugador["puntuacion"] += dado
        if jugador["puntuacion"] > 21:
            print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
            jugador["plantado"] = True
        else:
            print(f"{jugador["jugador"]} tira {dado}")
            print(f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}")
    elif jugador["puntuacion"] < 20:
        if jugadores[0]["puntuacion"] > 17:
            is_pedir = tirar_IA_dificil("agresiva")
            if is_pedir:
                dado = tirar()
                jugador["puntuacion"] += dado
                if jugador["puntuacion"] > 21:
                    print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
                    jugador["plantado"] = True
                else:
                    print(f"{jugador["jugador"]} tira {dado}")
                    print(
                        f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}"
                    )
            else:
                jugador["plantado"] = True
                print(f"{jugador["jugador"]} se PLANTA con {jugador["puntuacion"]}")
        else:
            is_pedir = tirar_IA_dificil("defensiva")
            if is_pedir:
                dado = tirar()
                jugador["puntuacion"] += dado
                if jugador["puntuacion"] > 21:
                    print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
                    jugador["plantado"] = True
                else:
                    print(f"{jugador["jugador"]} tira {dado}")
                    print(
                        f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}"
                    )
            else:
                jugador["plantado"] = True
                print(f"IA_dificil se PLANTA! con {jugador["puntuacion"]}")
    else:  # significa que tiene 21, se planta
        print(f"{jugador["jugador"]} se PLANTA! con {jugador["puntuacion"]}")
        jugador["plantado"] = True
    return jugador

def is_fin_partida(jugadores: list) -> bool:
    activos = [j for j in jugadores if not j["plantado"]]

    # Debe quedar solo un jugador activo
    if len(activos) != 1:
        return False

    ganador = activos[0]

    # No debe pasarse de 21
    if ganador["puntuacion"] > 21:
        return False

    # Debe tener más puntuación que todos los demás
    for j in jugadores:
        if j != ganador and j["puntuacion"] >= ganador["puntuacion"] and j["puntuacion"] <= 21:
            return False

    return True



breaker = False
contador_ronda = 0


print("Bienvenido al BlackJack!")
try:
    jugadores = construir_lista()
    while not breaker:
        contador_ronda += 1
        print("=" * 30)
        print(f"******RONDA {contador_ronda}******")
        print("=" * 30)
        time.sleep(1)
        for jugador in jugadores:
            # Pasa los jugadores que se han plantado
            if jugador["plantado"] == True:
                continue
            match jugador["jugador"]:
                case "Humano":
                    jugador = logica_humano(jugador)
                case "IA_facil":
                    jugador = logica_IA_facil(jugador)
                case "IA_medio":
                    jugador = logica_IA_medio(jugador)
                case "IA_dificil":
                    jugador = logica_IA_dificil(jugador)
        breaker = is_fin_partida(jugadores)
    ganador, puntuacion = quienGana(jugadores)
    if ganador == "Empate":
        print(f"Ha habido un empate con {puntuacion} puntos!")
    else:
        print(f"El ganador es {ganador} con {puntuacion} puntos!")


except ValueError as error:
    print(f"ERROR: {error}")