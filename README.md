# BlackJack en Python

Juego de BlackJack por consola desarrollado en Python. Permite partidas con múltiples jugadores humanos e IAs de distintas dificultades.

---

## Características

- Soporte para múltiples jugadores humanos simultáneos
- Tres niveles de IA: fácil, medio y difícil
- La IA difícil adapta su estrategia (agresiva/defensiva) según la puntuación del humano
- Comodín disponible para el jugador humano: convierte un 6 en un 1
- Detección automática de fin de partida y ganador

## Reglas del juego

- El objetivo es acumular la mayor puntuación posible sin superar **21 puntos**
- En cada turno, el jugador puede **pedir carta** o **plantarse**
- Si se supera 21, el jugador pierde automáticamente
- El jugador humano dispone de **un comodín por partida**: si saca un 6, puede convertirlo en 1

## Comportamiento de las IAs

| IA | Estrategia |
|---|---|
| `IA_facil` | Se planta a partir de 17 |
| `IA_medio` | Se planta a partir de 17; entre 17-20 decide aleatoriamente (50/50) |
| `IA_dificil` | Adapta su jugada según la puntuación del humano: agresiva si el humano va fuerte, defensiva si va flojo |

## Requisitos

- Python 3.10 o superior (se usa `match/case`)

## Cómo ejecutar

```bash
python blackjack.py
```

Al iniciar, el juego te pedirá cuántos jugadores de cada tipo quieres incluir en la partida.

## Estructura del proyecto

```
blackjack.py   # Archivo principal con toda la lógica del juego
```

## Autor

Desarrollado como proyecto de aprendizaje de Python.
