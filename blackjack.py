import random
import time


def tirar() -> int:
    """Devulve un número aleatorio entre 1 y 6"""
    tirada = 6
    return tirada


def tirar_prob50() -> bool:
    """Devuleve True o False con una probabilidad del 50%"""
    num = random.randint(1, 2)
    if num == 1:
        return True
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
    # Humano
    while True:
        humano = input("Cuantas Humanos quieres?")
        if not humano.isdigit():
            print("Error, ingrese un número valido")
            continue
        humano = int(humano)
        if humano < 0:
            print("No se permiten numeros negativos")
            continue
        break

    for _ in range(humano):
        jugador = {"jugador": "IA_facil", "puntuacion": 0, "plantado": False}
        jugadores.append(jugador)
    # IA_FACIL
    while True:
        ia_facil = input("Cuantas IA_facil quieres?")
        if not ia_facil.isdigit():
            print("Error, ingrese un número valido")
            continue
        ia_facil = int(ia_facil)
        if ia_facil < 0:
            print("No se permiten numeros negativos")
            continue
        break

    for _ in range(ia_facil):
        jugador = {"jugador": "IA_facil", "puntuacion": 0, "plantado": False}
        jugadores.append(jugador)
    # IA_MEDIO
    while True:
        ia_medio = input("Cuantas IA_medio quieres?")
        if not ia_medio.isdigit():
            print("Error, ingrese un número valido")
            continue
        ia_medio = int(ia_medio)
        if ia_medio < 0:
            print("No se permiten numeros negativos")
            continue
        break

    for _ in range(ia_medio):
        jugador = {"jugador": "IA_medio", "puntuacion": 0, "plantado": False}
        jugadores.append(jugador)
    # IA_DIFICIL
    while True:
        ia_dificil = input("Cuantas IA_dificil quieres?")
        if not ia_dificil.isdigit():
            print("Error, ingrese un número valido")
            continue
        ia_dificil = int(ia_dificil)
        if ia_dificil < 0:
            print("No se permiten numeros negativos")
            continue
        break

    for _ in range(ia_dificil):
        jugador = {"jugador": "IA_dificil", "puntuacion": 0, "plantado": False}
        jugadores.append(jugador)

    for jugador in jugadores:
        print(jugador)


jugadores = [
    {"jugador": "Humano", "puntuacion": 0, "plantado": False, "comodin_usado": False},
    {"jugador": "IA_facil", "puntuacion": 0, "plantado": False},
    {"jugador": "IA_medio", "puntuacion": 0, "plantado": False},
    {"jugador": "IA_dificil", "puntuacion": 0, "plantado": False},
]
breaker = False
contador_ronda = 0


print("Bienvenido al BlackJack!")
try:
    construir_lista()
    while not breaker:
        contador_ronda += 1
        print("=" * 30)
        print(f"******RONDA {contador_ronda}******")
        print("=" * 30)
        time.sleep(0.5)
        for jugador in jugadores:
            # Pasa los jugadores que se han plantado
            if jugador["plantado"] == True:
                continue
            """Tirada Humano"""
            match jugador["jugador"]:

                case "Humano":
                    if jugador["puntuacion"] == 0:
                        jugador["puntuacion"] = tirar()
                        print(
                            f"{jugador["jugador"]} empieza con una puntuación de {jugador["puntuacion"]}"
                        )
                    elif not jugador["plantado"]:
                        while True:
                            opcion = input("quieres plantarte? s/n: ")
                            match opcion:
                                case "s":
                                    print(f"{jugador["jugador"]} se PLANTA")
                                    jugador["plantado"] = True
                                    break
                                case "n":
                                    dado = tirar()
                                    if dado == 6 and jugador["comodin_usado"] == False:
                                        print(
                                            "Has obtenido un 6, tienes la opcion de convertirlo en un 1, ¿quieres? s/n"
                                        )
                                        opcion = "x"
                                        while True:
                                            opcion = input()
                                            match opcion:
                                                case "s":
                                                    jugador["puntuacion"] += 1
                                                    break
                                                case "n":
                                                    jugador["puntuacion"] += 6
                                                    break
                                                case _:
                                                    print("opcion no valida")
                                    else:
                                        jugador["puntuacion"] += dado
                                    if jugador["puntuacion"] > 21:
                                        print(
                                            f"Te has pasado con {jugador["puntuacion"]}, PIERDES!"
                                        )
                                        jugador["plantado"] = True
                                    else:
                                        print(
                                            f"Puntuacion del {jugador["jugador"]}: {jugador["puntuacion"]}"
                                        )
                                    break
                                case _:
                                    print("opcion no valida")
                                    continue

                case "IA_facil":
                    """Tirada IA_facil"""
                    if jugador["puntuacion"] < 17:
                        jugador["puntuacion"] += tirar()
                        if jugador["puntuacion"] > 21:
                            print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
                            jugador["plantado"] = True
                        else:
                            print(
                                f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}"
                            )
                    else:
                        jugador["plantado"] = True
                        print(f"La {jugador["jugador"]} se PLANTA!")

                case "IA_medio":
                    """Tirada IA_medio"""
                    if jugador["puntuacion"] < 17:
                        jugador["puntuacion"] += tirar()
                        if jugador["puntuacion"] > 21:
                            print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
                            jugador["plantado"] = True
                        else:
                            print(
                                f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}"
                            )
                    elif jugador["puntuacion"] < 20:
                        if tirar_prob50():
                            jugador["puntuacion"] += tirar()
                            if jugador["puntuacion"] > 21:
                                print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
                                jugador["plantado"] = True
                            else:
                                print(
                                    f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}"
                                )
                        else:
                            jugador["plantado"] = True
                            print(f"La {jugador["jugador"]} se PLANTA!")
                    else:
                        jugador["plantado"] = True
                        print(f"La {jugador["jugador"]} se PLANTA!")

                case "IA_dificil":
                    """Tirada IA_dificil"""
                    if jugador["puntuacion"] < 17:
                        jugador["puntuacion"] += tirar()
                        if jugador["puntuacion"] > 21:
                            print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
                            jugador["plantado"] = True
                        else:
                            print(
                                f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}"
                            )
                    elif jugador["puntuacion"] < 20:
                        if jugadores[0]["puntuacion"] > 17:
                            print(f"{jugador["jugador"]} opta por una jugada agresiva")
                            rand = random.randint(1, 10)
                            if rand > 3:
                                jugador["puntuacion"] += tirar()
                                if jugador["puntuacion"] > 21:
                                    print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
                                    jugador["plantado"] = True
                                else:
                                    print(
                                        f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}"
                                    )
                            else:
                                jugador["plantado"] = True
                                print(f"{jugador["jugador"]} se PLANTA")
                        else:
                            print(f"{jugador["jugador"]} opta por una jugada defensiva")
                            rand = random.randint(1, 10)
                            if rand > 7:
                                jugador["puntuacion"] += tirar()
                                if jugador["puntuacion"] > 21:
                                    print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
                                    jugador["plantado"] = True
                                else:
                                    print(
                                        f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}"
                                    )
                            else:
                                jugador["plantado"] = True
                                print(f"IA_dificil se PLANTA!")
                    else:  # significa que tiene 21, se planta
                        print(f"{jugador["jugador"]} se PLANTA!")
                        jugador["plantado"] = True

        """Si todos estan plantados se compara ganador"""
        breaker = True
        for jugador in jugadores:
            if not jugador["plantado"]:
                breaker = False
    ganador, puntuacion = quienGana(jugadores)
    if ganador == "Empate":
        print(f"Ha habido un empate con {puntuacion} puntos!")
    else:
        print(f"El ganador es {ganador} con {puntuacion} puntos!")


except ValueError as error:
    print(f"ERROR: {error}")
