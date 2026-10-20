# 🧠 Super Memory Numbers Game

**Super Memory Numbers Game** es un desafiante juego de memoria y reacción desarrollado con **Pygame**. Tu objetivo es recordar la secuencia de posiciones en las que aparecen los números del 1 hasta el nivel actual y luego hacer clic en esas posiciones en el orden correcto para avanzar.

---

## 🎮 Características Principales

* **Secuencia de Memoria:** Los botones del 1 al $N$ se iluminan brevemente en secuencia. Debes recordar la posición de cada número en el orden correcto.
* **Dificultad Progresiva:** La complejidad del tablero y la velocidad de visualización aumentan con el nivel.
* **Múltiples Dificultades:** Juega en modos **Fácil**, **Normal** o **Difícil**, cada uno con tiempos de visualización y límites de tiempo de respuesta ajustados.
* **Modo Estrella (\*):** En niveles superiores, un número podría ser reemplazado por un $\star$. Esto indica que debes hacer clic en esa posición, aunque no corresponda al número esperado en ese momento.
* **Sistema de Vidas y Tiempo:** Tienes un número limitado de vidas y un tiempo límite para responder en cada paso, lo que añade tensión.
* **Hall de la Fama:** Las mejores puntuaciones se guardan localmente (`scores.json`), clasificadas por el nivel de dificultad para una competencia justa.

---

## 🚀 Cómo Jugar

### 1. Iniciar Partida

1.  Al iniciar, serás dirigido a la pantalla **SELECCIONA DIFICULTAD**.
2.  Elige tu modo de juego haciendo clic en **FÁCIL**, **NORMAL** o **DIFÍCIL**.

### 2. Fases de la Ronda

1.  **Fase de Visualización (MEMORIZA):**
    * Los números del 1 hasta el nivel actual aparecen brevemente en posiciones aleatorias del tablero.
    * **¡Concentrate!** Recuerda la posición de cada número.
2.  **Fase de Entrada (RESPONDE):**
    * El juego te pedirá qué posición del número debes marcar a continuación (ej: "Marca la posición del: 1").
    * **Haz clic** en el botón correcto en el tablero.

### 3. Resultados y Avance

* **Acierto:** Avanzas al siguiente número de la secuencia y el tiempo se recarga. Si completas toda la secuencia, subes de nivel y ganas puntos.
* **Fallo o Tiempo Agotado:** Pierdes una vida. Si aún te quedan vidas, la secuencia para el nivel actual se reinicia.

### 4. Fin del Juego

* Si pierdes todas las vidas, la partida termina.
* Se te pedirá introducir tu nombre para registrar tu puntuación final en el **Hall de la Fama**.

---

## 🏆 Hall de la Fama

* Puedes acceder a las puntuaciones desde el menú principal.
* **Navegación:** Usa las **teclas de flecha $\leftarrow$ y $\rightarrow$** o **haz clic en los botones de navegación** en pantalla para cambiar entre las tablas de dificultad (**FÁCIL**, **NORMAL**, **DIFÍCIL**).

---

## 💻 Requisitos y Ejecución (Escritorio)

Para ejecutar este juego, necesitas tener instalado **Python 3** y la biblioteca **Pygame**.

### 1. Requisitos

Asegúrate de tener **Python 3.x** instalado en tu sistema.

### 2. Instalación de Pygame

Abre tu terminal o símbolo del sistema y ejecuta el siguiente comando:

```bash
pip install pygame
```

## 🚀 Cómo ejecutar

```bash
python super_memory_numbers.py
```




---

# English Version

🧠 **Super Memory Numbers Game**

**Super Memory Numbers Game** is a challenging memory and reaction game developed with **Pygame**. Your goal is to remember the sequence of positions where the numbers from 1 up to the current level appear, and then click those positions in the correct order to advance.

---

## 🎮 Key Features

* **Memory Sequence:** Buttons from 1 to $N$ light up briefly in sequence. You must remember the position of each number in the correct order.
* **Progressive Difficulty:** Board complexity and display speed increase with the level.
* **Multiple Difficulties:** Play in **Easy**, **Normal** or **Hard** modes, each with adjusted display times and response time limits.
* **Star Mode (\*):** At higher levels, a number may be replaced by a $\star$. This means you must click that position even if it does not match the number expected at that moment.
* **Lives and Time System:** You have a limited number of lives and a time limit to respond at each step, which adds tension.
* **Hall of Fame:** Best scores are stored locally (`scores.json`), ranked by difficulty level for fair competition.

---

## 🚀 How to Play

### 1. Starting a Game

1.  On startup you will be taken to the **SELECT DIFFICULTY** screen.
2.  Choose your game mode by clicking **EASY**, **NORMAL** or **HARD**.

### 2. Round Phases

1.  **Display Phase (MEMORIZE):**
    * The numbers from 1 up to the current level appear briefly at random positions on the board.
    * **Focus!** Remember the position of each number.
2.  **Input Phase (ANSWER):**
    * The game will ask you which position of the number to click next (e.g.: "Click the position of: 1").
    * **Click** the correct button on the board.

### 3. Results and Progress

* **Correct:** You move to the next number in the sequence and the timer refills. If you complete the whole sequence you level up and earn points.
* **Wrong or Time Up:** You lose a life. If you still have lives, the sequence for the current level restarts.

### 4. Game Over

* If you lose all lives, the game ends.
* You will be asked to enter your name to register your final score in the **Hall of Fame**.

---

## 🏆 Hall of Fame

* You can access the scores from the main menu.
* **Navigation:** Use the **arrow keys $\leftarrow$ and $\rightarrow$** or **click the on-screen navigation buttons** to switch between the difficulty tables (**EASY**, **NORMAL**, **HARD**).

---

## 💻 Requirements and Execution (Desktop)

To run this game you need **Python 3** and the **Pygame** library installed.

### 1. Requirements

Make sure you have **Python 3.x** installed on your system.

### 2. Installing Pygame

Open your terminal or command prompt and run:

```bash
pip install pygame
```

## 🚀 How to Run

```bash
python super_memory_numbers.py
```

