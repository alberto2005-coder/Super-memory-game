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
