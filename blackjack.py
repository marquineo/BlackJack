import random
import csv


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


def quienGana(IA_facil, IA_medio, IA_dificil) -> str:
    jugadores = [IA_facil, IA_medio, IA_dificil]

    # Obtenemos maxima puntuacion
    max_puntuacion = max(j["Puntuacion_Final"] for j in jugadores if j["Puntuacion_Final"] <= 21)

    # Cuantos jugadores tiene la maxima puntacion de la partida (ganadores)
    ganadores = [j for j in jugadores if j["Puntuacion_Final"] == max_puntuacion]
    es_empate = len(ganadores) > 1

    # actualizamos atributo
    for j in jugadores:
        """
        Si tienes la maxima puntuacion y solo hay un ganador -> Victoria
        Hay mas de 1 ganador -> Empate
        Si no tienes la maxima puntuacion -> Derrota
        """
        if j["Puntuacion_Final"] == max_puntuacion:
            j["Resultado"] = "Empate" if es_empate else "Victoria"
        else:
            j["Resultado"] = "Derrota"
    return jugadores[0], jugadores[1], jugadores[2]


def logica_IA_facil(jugador: dict) -> dict:
    """
    Procesa la logica de IA_facil, recibe por parametro al jugador
    y lo retorna con los cambios realizados.
    """
    if jugador["Puntuacion_Final"] < 17:
        dado = tirar()
        jugador["Cartas"] += 1
        jugador["Puntuacion_Final"] += dado
        if jugador["Puntuacion_Final"] > 21:
            # print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
            jugador["Plantado"] = True
        # else:
        # print(f"{jugador["jugador"]} tira {dado}")
        # print(f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}")
    else:
        jugador["Plantado"] = True
        # print(f"La {jugador["jugador"]} se PLANTA! con {jugador["puntuacion"]}")
    return jugador


def logica_IA_medio(jugador: dict) -> dict:
    """
    Procesa la logica de IA_medio, recibe por parametro al jugador
    y lo retorna con los cambios realizados.
    """
    if jugador["Puntuacion_Final"] < 17:
        dado = tirar()
        jugador["Cartas"] += 1
        jugador["Puntuacion_Final"] += dado
        if jugador["Puntuacion_Final"] > 21:
            # print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
            jugador["Plantado"] = True
        # else:
        #     print(f"{jugador["jugador"]} tira {dado}")
        #     print(f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}")
    elif jugador["Puntuacion_Final"] < 20:
        if tirar_prob50():
            dado = tirar()
            jugador["Cartas"] += 1
            jugador["Puntuacion_Final"] += dado
            if jugador["Puntuacion_Final"] > 21:
                # print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
                jugador["Plantado"] = True
            # else:
            #     print(f"{jugador["jugador"]} tira {dado}")
            #     print(f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}")
        else:
            jugador["Plantado"] = True
            # print(f"La {jugador["jugador"]} se PLANTA! con {jugador["puntuacion"]}")
    else:
        jugador["Plantado"] = True
        # print(f"La {jugador["jugador"]} se PLANTA! con {jugador["puntuacion"]}")
    return jugador


def logica_IA_dificil(jugador: dict) -> dict:
    """
    Procesa la logica de IA_dificil, recibe por parametro al jugador
    y lo retorna con los cambios realizados.
    """
    if jugador["Puntuacion_Final"] < 17:
        dado = tirar()
        jugador["Cartas"] += 1
        jugador["Puntuacion_Final"] += dado
        if jugador["Puntuacion_Final"] > 21:
            # print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
            jugador["Plantado"] = True
        # else:
        # print(f"{jugador["jugador"]} tira {dado}")
        # print(f"Puntuacion_Final de {jugador["jugador"]}: {jugador["puntuacion"]}")
    elif jugador["Puntuacion_Final"] < 20:
        # verifica si hay alguna IA con mas de 17
        if IA_facil["Puntuacion_Final"] > 17 or IA_medio["Puntuacion_Final"] > 17:
            is_pedir = tirar_IA_dificil("agresiva")
            if is_pedir:
                dado = tirar()
                jugador["Cartas"] += 1
                jugador["Puntuacion_Final"] += dado
                if jugador["Puntuacion_Final"] > 21:
                    # print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
                    jugador["Plantado"] = True
                # else:
                #     print(f"{jugador["jugador"]} tira {dado}")
                #     print(
                #         f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}"
                #     )
            else:
                jugador["Plantado"] = True
                # print(f"{jugador["jugador"]} se PLANTA con {jugador["puntuacion"]}")
        else:
            is_pedir = tirar_IA_dificil("defensiva")
            if is_pedir:
                dado = tirar()
                jugador["Cartas"] += 1
                jugador["Puntuacion_Final"] += dado
                if jugador["Puntuacion_Final"] > 21:
                    # print(f"{jugador["jugador"]} se ha pasado, PIERDE!")
                    jugador["Plantado"] = True
                # else:
                #     print(f"{jugador["jugador"]} tira {dado}")
                #     print(
                #         f"Puntuacion de {jugador["jugador"]}: {jugador["puntuacion"]}"
                #     )
            else:
                jugador["Plantado"] = True
                # print(f"IA_dificil se PLANTA! con {jugador["puntuacion"]}")
    else:  # significa que tiene 21, se planta
        # print(f"{jugador["jugador"]} se PLANTA! con {jugador["puntuacion"]}")
        jugador["Plantado"] = True
    return jugador


def is_fin_partida(IA_facil, IA_medio, IA_dificil) -> bool:
    # FIXME siempre devuelve False
    jugadores = [IA_facil, IA_medio, IA_dificil]
    ganador = [j for j in jugadores if j["Puntuacion_Final"] == 21]

    if len(ganador) == 1:
        return True

    # is_todos_plantado = all(j["Plantado"] for j in jugadores)
    # if is_todos_plantado:
    #     return True

    activos = [j for j in jugadores if not j["Plantado"]]

    if len(activos) == 0:
        return True
    elif len(activos) == 1:
        posible_ganador = activos[0]
        max_puntuacion = max(j["Puntuacion_Final"] for j in jugadores)
        if max_puntuacion == posible_ganador["Puntuacion_Final"]:
            return True
    return False


def menu_dataset():
    while True:
        print("=====GENERADOR DE DATASET=====")
        print("1. Generar dataset muy pequeño -> (1 partida)")
        print("2. Generar dataset pequeño -> (10 partidas)")
        print("3. Generar dataset mediano -> (100 partidas)")
        print("4. Generar dataset grande -> (1000 partidas)")
        print("5. Generar dataset muy grande -> (10000 partidas)")
        opcion = input("Selecciona tamaño de dataset (1-5):")

        match (opcion):
            case "1":
                cantidad_partidas = 1
            case "2":
                cantidad_partidas = 10
            case "3":
                cantidad_partidas = 100
            case "4":
                cantidad_partidas = 1000
            case "5":
                cantidad_partidas = 10000
            case _:
                print("Opcion no válida (1-5)")
                continue
        print(f"cant: {cantidad_partidas}")
        return cantidad_partidas

datos = []
print("=====Bienvenido al BlackJack!======")
try:
    tamanyo_dataset = menu_dataset()
    for i in range(tamanyo_dataset):
        # Construimos IAs
        IA_facil = {
            "ID_partida": i+1,
            "Tipo_IA": "IA_facil",
            "Puntuacion_Final": 0,
            "Resultado": "",
            "Cartas": 0,
            "Plantado": False,
        }
        IA_medio = {
            "ID_partida": i+1,
            "Tipo_IA": "IA_medio",
            "Puntuacion_Final": 0,
            "Resultado": "",
            "Cartas": 0,
            "Plantado": False,
        }
        IA_dificil = {
            "ID_partida": i+1,
            "Tipo_IA": "IA_dificil",
            "Puntuacion_Final": 0,
            "Resultado": "",
            "Cartas": 0,
            "Plantado": False,
        }
        breaker = False
        print(f"*****PARTIDA {IA_dificil["ID_partida"]}*****")
        while not breaker:
            # IA_facil
            if IA_facil["Plantado"] == False:
                IA_facil = logica_IA_facil(IA_facil)
                if IA_facil["Puntuacion_Final"] == 21:
                    breaker = is_fin_partida(IA_facil, IA_medio, IA_dificil)
                    continue
            # IA_medio
            if IA_medio["Plantado"] == False:
                IA_medio = logica_IA_facil(IA_medio)
                if IA_medio["Puntuacion_Final"] == 21:
                    breaker = is_fin_partida(IA_facil, IA_medio, IA_dificil)
                    continue
            # IA_dificil
            if IA_dificil["Plantado"] == False:
                IA_dificil = logica_IA_facil(IA_dificil)
                if IA_dificil["Puntuacion_Final"] == 21:
                    breaker = is_fin_partida(IA_facil, IA_medio, IA_dificil)
                    continue
            breaker = is_fin_partida(IA_facil, IA_medio, IA_dificil)
        IA_facil, IA_medio, IA_dificil = quienGana(IA_facil, IA_medio, IA_dificil)
        print(f"facil ->{IA_facil}")
        print(f"medio ->{IA_medio}")
        print(f"dificil ->{IA_dificil}")
        datos.append(IA_facil)
        datos.append(IA_medio)
        datos.append(IA_dificil)
    with open("dataset.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "ID_partida",
            "Tipo_IA",
            "Puntuacion_Final",
            "Resultado",
            "Cartas",
            "Plantado",
        ]
        escritor = csv.DictWriter(file,fieldnames=fieldnames)
        escritor.writeheader()
        escritor.writerows(datos)

except ValueError as error:
    print(f"ERROR: {error}")
