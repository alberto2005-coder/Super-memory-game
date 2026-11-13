# Super Memory Numbers Game

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-00A300)](https://www.pygame.org/)
[![MIT](https://img.shields.io/badge/Licencia-MIT-green)](LICENSE)

[Español](#español) · [English](#english)

---

## Español

### Índice

- [Descripción](#descripción)
- [Cómo se juega](#cómo-se-juega)
- [Características](#características)
- [Hall de la Fama](#hall-de-la-fama)
- [Requisitos](#requisitos)
- [Instalación y ejecución](#instalación-y-ejecución)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Licencia](#licencia)

### Descripción

**Super Memory Numbers Game** es un juego de memoria y reflejos hecho con **Pygame**. En cada ronda aparecen los números del 1 hasta el nivel actual en posiciones aleatorias del tablero; después hay que hacer clic en esas posiciones en el orden correcto para avanzar.

### Cómo se juega

1. Elige dificultad en la pantalla inicial: **Fácil**, **Normal** o **Difícil**.
2. **Memoriza**: los números se iluminan brevemente en el tablero.
3. **Responde**: el juego pide una posición concreta («Marca la posición del 1») y tienes un tiempo límite.
4. Si aciertas, avanzas y el cronómetro se recarga; al completar la secuencia subes de nivel.
5. Si fallas o se agota el tiempo, pierdes una vida y la secuencia del nivel se reinicia.
6. Sin vidas, la partida termina y puedes guardar tu nombre en el Hall de la Fama.

### Características

- **Secuencia de memoria** del 1 al nivel actual.
- **Dificultad progresiva**: más números, más rápido y menos tiempo de reacción.
- **Tres modos**: Fácil, Normal y Difícil, con tiempos y límites distintos.
- **Modo estrella**: en niveles altos un número puede sustituirse por `*`, y hay que pulsar esa posición aunque no toque el número esperado.
- **Vidas y temporizador** por paso.
- **Hall de la Fama** local en `scores.json`, separado por dificultad.

### Hall de la Fama

Se abre desde el menú principal. Cambia de tabla con las **flechas ← y →** o con los botones en pantalla. Cada dificultad tiene su propia clasificación para que la comparación sea justa.

### Requisitos

- **Python 3.x**.
- **Pygame**:

```bash
pip install pygame
```

### Instalación y ejecución

```bash
git clone https://github.com/alberto2005-coder/Super-memory-game.git
cd Super-memory-game
pip install pygame
python super_memory_numbers_game.py
```

> [!NOTE]
> El archivo de puntuaciones (`scores.json`) se crea o actualiza en la carpeta del proyecto. Si lo borras, empiezas con el Hall de la Fama vacío.

### Estructura del proyecto

```text
Super-memory-game/
├── super_memory_numbers_game.py  # Juego completo: menús, lógica y puntuaciones
├── scores.json                   # Hall de la Fama local
├── LICENSE
└── README.md
```

### Licencia

**MIT** — consulta [LICENSE](LICENSE).

---

## English

### Table of contents

- [Overview](#overview)
- [How to play](#how-to-play)
- [Features](#features)
- [Hall of Fame](#hall-of-fame)
- [Requirements](#requirements)
- [Installation and running](#installation-and-running)
- [Project structure](#project-structure)
- [License](#license)

### Overview

**Super Memory Numbers Game** is a memory and reaction game built with **Pygame**. Each round shows the numbers from 1 up to the current level at random board positions; you then click those positions in the right order to advance.

### How to play

1. Pick a difficulty on the start screen: **Easy**, **Normal** or **Hard**.
2. **Memorize**: the numbers light up briefly on the board.
3. **Answer**: the game asks for a specific position ("Click the position of 1") under a time limit.
4. A correct answer advances the sequence and refills the timer; finishing it levels you up.
5. A wrong answer or a timeout costs a life and restarts the current level's sequence.
6. With no lives left the run ends and you can record your name in the Hall of Fame.

### Features

- **Memory sequence** from 1 to the current level.
- **Progressive difficulty**: more numbers, faster display and less reaction time.
- **Three modes**: Easy, Normal and Hard, each with its own timings.
- **Star mode**: at higher levels a number may become `*`, and you must click that position even if it is not the expected number.
- **Lives and per-step timer**.
- **Local Hall of Fame** in `scores.json`, split by difficulty.

### Hall of Fame

Open it from the main menu. Switch tables with the **← and → arrow keys** or the on-screen buttons. Each difficulty keeps its own ranking so comparisons stay fair.

### Requirements

- **Python 3.x**.
- **Pygame**:

```bash
pip install pygame
```

### Installation and running

```bash
git clone https://github.com/alberto2005-coder/Super-memory-game.git
cd Super-memory-game
pip install pygame
python super_memory_numbers_game.py
```

> [!NOTE]
> The score file (`scores.json`) is created or updated inside the project folder. Delete it to start with an empty Hall of Fame.

### Project structure

```text
Super-memory-game/
├── super_memory_numbers_game.py  # Full game: menus, logic and scores
├── scores.json                   # Local Hall of Fame
├── LICENSE
└── README.md
```

### License

**MIT** — see [LICENSE](LICENSE).
