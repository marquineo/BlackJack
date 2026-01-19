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
    max_puntuacion = max(j["Puntuacion_Final"] for j in jugadores)

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
    #FIXME siempre devuelve False
    activos = []
    if IA_facil["Plantado"]:
        activos.append(IA_facil)
    if IA_medio["Plantado"]:
        activos.append(IA_medio)
    if IA_dificil["Plantado"]:
        activos.append(IA_dificil)

    # Debe quedar solo un jugador activo
    if len(activos) != 1:
        return False

    ganador = activos[0]

    # No debe pasarse de 21
    if ganador["Puntuacion_Final"] > 21:
        return False

    # Debe tener más puntuación que todos los demás
    jugadores = [IA_facil, IA_medio, IA_dificil]
    for j in jugadores:
        if (
            j != ganador
            and j["Puntuacion_Final"] >= ganador["Puntuacion_Final"]
            and j["Puntuacion_Final"] <= 21
        ):
            return False

    return True


def menu_dataset():
    while True:
        print("=====GENERADOR DE DATASET=====")
        print("1. Generar dataset muy pequeño -> (1 partida)")
        print("2. Generar dataset pequeño -> (10 partidas)")
        print("3. Generar dataset mediano -> (100 partidas)")
        print("4. Generar dataset grande -> (1000 partidas)")
        print("5. Generar dataset muy grande -> (10000 partidas)")
        opcion = input("Selecciona tamaño de dataset (1-5):")
        if not opcion.isdigit():
            print("La opción debe ser un número")
            continue
        opcion = int(opcion)
        if opcion > 5 or opcion < 1:
            print("Opcion no válida (1-5)")
            continue
        return opcion


IA_facil = {
    "ID_partida": 0,
    "Tipo_IA": "IA_facil",
    "Puntuacion_Final": 0,
    "Resultado": "",
    "Cartas": 0,
    "Plantado": False,
}
IA_medio = {
    "ID_partida": 0,
    "Tipo_IA": "IA_medio",
    "Puntuacion_Final": 0,
    "Resultado": "",
    "Cartas": 0,
    "Plantado": False,
}
IA_dificil = {
    "ID_partida": 0,
    "Tipo_IA": "IA_dificil",
    "Puntuacion_Final": 0,
    "Resultado": "",
    "Cartas": 0,
    "Plantado": False,
}
breaker = False
contador_ronda = 0
print("=====Bienvenido al BlackJack!======")
try:
    tamanyo_dataset = menu_dataset()
    for _ in range(tamanyo_dataset):
        IA_facil["ID_partida"] += 1
        IA_medio["ID_partida"] += 1
        IA_dificil["ID_partida"] += 1
        print(f"*****PARTIDA {IA_dificil["ID_partida"]}*****")
        while not breaker:
            # IA_facil
            if IA_facil["Plantado"] == False:
                print("facil")
                IA_facil = logica_IA_facil(IA_facil)
            # IA_medio
            if IA_medio["Plantado"] == False:
                IA_medio = logica_IA_facil(IA_medio)
            # IA_dificil
            if IA_dificil["Plantado"] == False:
                IA_dificil = logica_IA_facil(IA_dificil)
            datos = [IA_facil,IA_medio,IA_dificil]
            breaker = is_fin_partida(IA_facil, IA_medio, IA_dificil)
            print(breaker)
    IA_facil, IA_medio, IA_dificil = quienGana(IA_facil, IA_medio, IA_dificil)

    with open("dataset.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "ID_Partida",
            "Tipo_IA",
            "Puntuacion_Final",
            "Resultado",
            "Cartas",
            "Plantado",
        ]
        escritor = csv.writer(file,fieldnames=fieldnames)
        escritor.writerow(fieldnames)
        escritor.writerows(datos)

except ValueError as error:
    print(f"ERROR: {error}")
