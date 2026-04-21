import csv
import matplotlib.pyplot as plt
import numpy as np


with open("dataset.csv","r",newline="",encoding="utf=8-sig") as file:
    lector = csv.DictReader(file)
    datos = list(lector)

    print(f"Cantidad de lineas cargadas: {len(datos)}")

#Iniciamos diccionarios
IA_facil = {
    "victoria": 0,
    "empate": 0,
    "derrota": 0,
    "bust": 0,
    "media_puntos_plantado": 0,
    "media_puntos": 0,
    "mediana_puntos_plantado": 0,
    "mediana_puntos_victoria": 0
}

IA_medio = {
    "victoria": 0,
    "empate": 0,
    "derrota": 0,
    "bust": 0,
    "media_puntos_plantado": 0,
    "media_puntos": 0,
    "mediana_puntos_plantado": 0,
    "mediana_puntos_victoria": 0
}

IA_dificil = {
    "victoria": 0,
    "empate": 0,
    "derrota": 0,
    "bust": 0,
    "media_puntos_plantado": 0,
    "media_puntos": 0,
    "mediana_puntos_plantado": 0,
    "mediana_puntos_victoria": 0
}
cantidad_partidas = len(datos) // 3
puntos_totales_facil = 0
lista_puntos_plantado_facil = []
lista_puntos_victoria_facil = []
lista_puntos_facil = []

puntos_totales_medio = 0
lista_puntos_plantado_medio = []
lista_puntos_victoria_medio = []
lista_puntos_medio = []


puntos_totales_dificil = 0
lista_puntos_plantado_dificil = []
lista_puntos_victoria_dificil = []
lista_puntos_dificil = []

for jugador in datos:
    # Normalizamos datos
    jugador["Puntuacion_Final"] = int(jugador["Puntuacion_Final"])
    jugador["Plantado"] = jugador["Plantado"] == "True"
    match (jugador["Tipo_IA"]):
        case "IA_facil":
            match (jugador["Resultado"]):
                case "Victoria":
                    IA_facil["victoria"] += 1
                    lista_puntos_victoria_facil.append(jugador["Puntuacion_Final"])
                case "Empate":
                    IA_facil["empate"] += 1
                case "Derrota":
                    IA_facil["derrota"] += 1
            if jugador["Puntuacion_Final"] > 21:
                IA_facil["bust"] += 1
            if jugador["Plantado"] and jugador["Puntuacion_Final"] <= 21:
                lista_puntos_plantado_facil.append(jugador["Puntuacion_Final"])
            puntos_totales_facil += jugador["Puntuacion_Final"]
            lista_puntos_facil.append(jugador["Puntuacion_Final"])
        case "IA_medio":
            match (jugador["Resultado"]):
                case "Victoria":
                    IA_medio["victoria"] += 1
                    lista_puntos_victoria_medio.append(jugador["Puntuacion_Final"])
                case "Empate":
                    IA_medio["empate"] += 1
                case "Derrota":
                    IA_medio["derrota"] += 1
            if jugador["Puntuacion_Final"] > 21:
                IA_medio["bust"] += 1
            if jugador["Plantado"] and jugador["Puntuacion_Final"] <= 21:
                lista_puntos_plantado_medio.append(jugador["Puntuacion_Final"])
            puntos_totales_medio += jugador["Puntuacion_Final"]
            lista_puntos_medio.append(jugador["Puntuacion_Final"])
        case "IA_dificil":
            match (jugador["Resultado"]):
                case "Victoria":
                    IA_dificil["victoria"] += 1
                    lista_puntos_victoria_dificil.append(jugador["Puntuacion_Final"])
                case "Empate":
                    IA_dificil["empate"] += 1
                case "Derrota":
                    IA_dificil["derrota"] += 1
            if jugador["Puntuacion_Final"] > 21:
                IA_dificil["bust"] += 1
            if jugador["Plantado"] and jugador["Puntuacion_Final"] <= 21:
                lista_puntos_plantado_dificil.append(jugador["Puntuacion_Final"])
            puntos_totales_dificil += jugador["Puntuacion_Final"]
            lista_puntos_dificil.append(jugador["Puntuacion_Final"])
        case _:
            print("Error en los case")
# Rellenamos media puntos
IA_facil["media_puntos"] = puntos_totales_facil / cantidad_partidas
IA_medio["media_puntos"] = puntos_totales_medio / cantidad_partidas
IA_dificil["media_puntos"] = puntos_totales_dificil / cantidad_partidas

#GRAFICA RATIO VICTORIAS - DERROTAS
cantidad_partidas = len(datos) // 3

victorias = np.array([IA_facil["victoria"],IA_medio["victoria"],IA_dificil["victoria"]])
porcentajes_vic = (victorias / cantidad_partidas) * 100

tipo_bot = ('IA_facil', 'IA_medio', 'IA_dificil')
estadisticas_bots = {
    'Victoria': np.array([porcentajes_vic[0],porcentajes_vic[1],porcentajes_vic[2]]),
    'Derrota': np.array([100 - porcentajes_vic[0],100 - porcentajes_vic[1],100 - porcentajes_vic[2]]),
}
grosor = 0.6  # el grosor de la barra

fig, ax = plt.subplots()
bottom = np.zeros(3)

for partida_resultado, partida_cuenta in estadisticas_bots.items():
    p = ax.bar(tipo_bot, partida_cuenta, grosor, label=partida_resultado,bottom=bottom)
    bottom += partida_cuenta

    ax.bar_label(p, label_type='center')

ax.set_title('Porcentaje de victorias')
ax.legend()

#plt.ylim(0,100)

plt.savefig(
    "% victoria-derrotas",
    dpi=300,
    bbox_inches="tight" # elimina márgenes en blanco
)

#plt.savefig('ejemplo_plot1.png')
plt.show()


#PUNTUACION MEDIA 
x = np.array(["IA_facil", "IA_medio", "IA_dificil"])
media_facil_redondeada = round(IA_facil["media_puntos"],2)
media_medio_redondeada = round(IA_medio["media_puntos"],2)
media_dificil_redondeada = round(IA_dificil["media_puntos"],2)
y = np.array([IA_facil["media_puntos"],IA_medio["media_puntos"],IA_dificil["media_puntos"]])

plt.text(0,IA_facil["media_puntos"] + 0.5,f"$ {media_facil_redondeada:.2f} $", color="k")
plt.text(1,IA_medio["media_puntos"] + 0.5,f"$ {media_medio_redondeada:.2f} $", color="k")
plt.text(2,IA_dificil["media_puntos"] + 0.5,f"$ {media_dificil_redondeada:.2f} $", color="k")

plt.plot(x, y, "r", marker='o', linestyle='-')

plt.ylim(0, 25)
plt.margins(x=0.5)

plt.xlabel("IA")
plt.ylabel("puntos")

plt.title("Puntuación media")

plt.savefig(
    "Media puntos",
    dpi=300,
    bbox_inches="tight" # elimina márgenes en blanco
)
plt.show()

#COMPARACION MEDIA VICTORIA - MEDIANA VICTORIA

# Ordenamos listas para la mediana
sorted_lista_puntos_victoria_facil = sorted(lista_puntos_victoria_facil)
sorted_lista_puntos_victoria_medio = sorted(lista_puntos_victoria_medio)
sorted_lista_puntos_victoria_dificil = sorted(lista_puntos_victoria_dificil)

#Calculamos mediana
IA_facil["mediana_puntos_victoria"] = sorted_lista_puntos_victoria_facil[len(sorted_lista_puntos_victoria_facil) // 2]
IA_medio["mediana_puntos_victoria"] = sorted_lista_puntos_victoria_medio[len(sorted_lista_puntos_victoria_medio) // 2]
IA_dificil["mediana_puntos_victoria"] = sorted_lista_puntos_victoria_dificil[len(sorted_lista_puntos_victoria_dificil) // 2]


x1 = np.array(["IA_facil", "IA_medio","IA_dificil"])
y1 = np.array([media_facil_redondeada, media_medio_redondeada,media_dificil_redondeada])

x2 = np.array(["IA_facil", "IA_medio","IA_dificil"])
y2 = np.array([IA_facil["mediana_puntos_victoria"],IA_medio["mediana_puntos_victoria"],IA_dificil["mediana_puntos_victoria"]])

plt.plot(x2, y2, "g", marker='o', linestyle='-', label="mediana victoria")
plt.text(0,IA_facil["mediana_puntos_victoria"] + 0.5,f"$ {IA_facil["mediana_puntos_victoria"]:.2f} $", color="g")
plt.text(1,IA_medio["mediana_puntos_victoria"] + 0.5,f"$ {IA_medio["mediana_puntos_victoria"]:.2f} $", color="g")
plt.text(2,IA_dificil["mediana_puntos_victoria"] + 0.5,f"$ {IA_dificil["mediana_puntos_victoria"]:.2f} $", color="g")

plt.plot(x1, y1, "r", marker='o', linestyle='-', label="media victoria")
plt.text(0,IA_facil["media_puntos"] + 0.5,f"$ {media_facil_redondeada:.2f} $", color="k")
plt.text(1,IA_medio["media_puntos"] + 0.5,f"$ {media_medio_redondeada:.2f} $", color="k")
plt.text(2,IA_dificil["media_puntos"] + 0.5,f"$ {media_dificil_redondeada:.2f} $", color="k")


plt.ylim(0, 25)
plt.margins(x=0.5)

plt.xlabel("IA")
plt.ylabel("puntos")

plt.legend()

plt.title("Media victoria vs Mediana victoria")

plt.savefig(
    "parte2_1 victoria.png",
    dpi=300,
    bbox_inches="tight" # elimina márgenes en blanco
)

plt.show()

# BURTS RATIO TARTA
#facil
porc_burst_facil = (IA_facil["bust"] / cantidad_partidas) * 100
porc_burst_medio = (IA_medio["bust"] / cantidad_partidas) * 100
porc_burst_dificil = (IA_dificil["bust"] / cantidad_partidas) * 100

y = np.array([porc_burst_facil, 100 - porc_burst_facil])
etiquetas = ["burst", "dentro del rango"]
colores = ["g", "y"]

plt.title("Burst Ratio IA_facil")
plt.pie(y, labels = etiquetas, colors = colores, autopct="%0.1f %%")

plt.savefig(
    "burst_ratio_IA_facil",
    dpi=300,
    bbox_inches="tight" # elimina márgenes en blanco
)

plt.show()

#medio
y = np.array([porc_burst_medio, 100 - porc_burst_medio])
etiquetas = ["burst", "dentro del rango"]
colores = ["g", "y"]

plt.title("Burst Ratio IA_medio")
plt.pie(y, labels = etiquetas, colors = colores, autopct="%0.1f %%")

plt.savefig(
    "burst_ratio_IA_medio",
    dpi=300,
    bbox_inches="tight" # elimina márgenes en blanco
)

plt.show()
#dificil
y = np.array([porc_burst_dificil, 100 - porc_burst_dificil])
etiquetas = ["burst", "dentro del rango"]
colores = ["g", "y"]

plt.title("Burst Ratio IA_dificil")
plt.pie(y, labels = etiquetas, colors = colores, autopct="%0.1f %%")

plt.savefig(
    "burst_ratio_IA_dificil",
    dpi=300,
    bbox_inches="tight" # elimina márgenes en blanco
)

plt.show()

# MODA PUNTUACION
#facil
puntos_IAfacil = np.array(lista_puntos_facil)

# 1. Calculamos los límites para que las barras queden centradas en los números
# Creamos bins que vayan desde el mínimo al máximo + 1
minimo = puntos_IAfacil.min()
maximo = puntos_IAfacil.max()
bins = np.arange(minimo, maximo + 2) - 0.5

# 2. Dibujamos el histograma especificando los bins y el alineado
plt.hist(puntos_IAfacil, bins=bins, edgecolor="black", color="skyblue")

# 3. Forzamos a que el eje X solo muestre números enteros
plt.xticks(range(minimo, maximo + 1))

plt.title("Distribución de puntos - IA Facil")
plt.xlabel("Puntos")
plt.ylabel("Frecuencia (Partidas)")
plt.savefig(
    "Distribución de puntos - IA Facil",
    dpi=300,
    bbox_inches="tight" # elimina márgenes en blanco
)
plt.show()

#medio
puntos_IAmedio = np.array(lista_puntos_medio)

minimo = puntos_IAmedio.min()
maximo = puntos_IAmedio.max()
bins = np.arange(minimo, maximo + 2) - 0.5

plt.hist(puntos_IAmedio, bins=bins, edgecolor="black", color="skyblue")

plt.xticks(range(minimo, maximo + 1))

plt.title("Distribución de puntos - IA Medio")
plt.xlabel("Puntos")
plt.ylabel("Frecuencia (Partidas)")
plt.savefig(
    "Distribución de puntos - IA Medio",
    dpi=300,
    bbox_inches="tight" # elimina márgenes en blanco
)
plt.show()

#dificil
puntos_IAdificil = np.array(lista_puntos_dificil)

minimo = puntos_IAdificil.min()
maximo = puntos_IAdificil.max()
bins = np.arange(minimo, maximo + 2) - 0.5

plt.hist(puntos_IAdificil, bins=bins, edgecolor="black", color="skyblue")

plt.xticks(range(minimo, maximo + 1))

plt.title("Distribución de puntos - IA Dificil")
plt.xlabel("Puntos")
plt.ylabel("Frecuencia (Partidas)")
plt.savefig(
    "Distribución de puntos - IA Dificil",
    dpi=300,
    bbox_inches="tight" # elimina márgenes en blanco
)
plt.show()