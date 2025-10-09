import pygame
import random
import sys
import time
import json
from datetime import datetime
import os

# --- Inicialización ---
pygame.init()

# --- Configuración de pantalla ---
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Memory Numbers Game")

# --- Constante del Archivo de Puntuaciones ---
SCORES_FILE = 'scores.json'

# --- Colores ---
WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
BLUE = (52, 152, 219)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
GRAY = (180, 180, 180)
YELLOW = (241, 196, 15)
LIGHT_BLUE = (135, 206, 250)
DARK_GRAY = (100, 100, 100)
ORANGE = (230, 126, 34)

# --- Fuentes ---
font_big = pygame.font.SysFont("Arial", 48)
font_medium = pygame.font.SysFont("Arial", 28)
font_small = pygame.font.SysFont("Arial", 22)
font_input = pygame.font.SysFont("Arial", 36)

# --- Reloj ---
clock = pygame.time.Clock()

# --- Estados ---
MENU = 0
SHOW_SEQUENCE = 1
PLAYER_INPUT = 2
GET_NAME = 3
GAME_OVER = 4
HALL_OF_FAME = 5
LEVEL_TRANSITION = 6
DIFFICULTY_SELECT = 7

game_state = MENU

# --- Variables de Juego ---
score = 0
level = 1
lives = 3
sequence_display_time = 2.0
player_input_count = 0 
sequence = [] 
player_name = ""
score_saved = False
time_remaining = 0.0
max_time_per_level = 0.0
difficulty_mode = 'NORMAL'

# --- Configuración de dificultad ---
DIFFICULTY_SETTINGS = {
    'EASY': {'label': 'FÁCIL', 'key': pygame.K_e, 'display_time': 3.0, 'time_bonus': 6.0, 'star_prob_base': 0.1, 'star_prob_multiplier': 0.05, 'max_board_level': 15},
    'NORMAL': {'label': 'NORMAL', 'key': pygame.K_n, 'display_time': 2.0, 'time_bonus': 5.0, 'star_prob_base': 0.2, 'star_prob_multiplier': 0.1, 'max_board_level': 10},
    'HARD': {'label': 'DIFÍCIL', 'key': pygame.K_d, 'display_time': 1.0, 'time_bonus': 4.0, 'star_prob_base': 0.3, 'star_prob_multiplier': 0.15, 'max_board_level': 5}
}
DIFFICULTY_KEYS = list(DIFFICULTY_SETTINGS.keys())
current_hof_difficulty_index = 1 # Empieza en 'NORMAL'

# --- Tablero (Botones base) ---
button_texts = [
    '1','2','3','4','5','6','7','8','9','*','0','#',
    'A','B','C'
]
buttons = []
button_size = (100, 100)

# --- Contenedor de Rects de Dificultad (para clic) ---
difficulty_rects = {} 

# --- Rects de navegación de Hall of Fame ---
hof_nav_buttons = {}

# --- Funciones de Botones Dinámicos ---
def create_buttons(current_level):
    """Crea la disposición de los botones 4x3 o 5x3 basada en el nivel y la dificultad."""
    global buttons, button_size
    
    settings = DIFFICULTY_SETTINGS.get(difficulty_mode, DIFFICULTY_SETTINGS['NORMAL'])
    max_level_for_4x3 = settings['max_board_level']
    
    if current_level <= max_level_for_4x3:
        rows, cols = 4, 3
        start_y = 150
        gap_x, gap_y = 120, 120
        button_size = (100, 100)
    else: # Transición a 5x3
        rows, cols = 5, 3
        start_y = 100
        gap_x, gap_y = 90, 90
        button_size = (70, 70) 

    buttons = []
    current_texts = button_texts[:rows * cols]
    
    for i, text in enumerate(current_texts):
        row = i // cols
        col = i % cols
        grid_width = cols * button_size[0] + (cols - 1) * (gap_x - button_size[0])
        start_x = (WIDTH - grid_width) // 2
        
        rect = pygame.Rect(start_x + col*gap_x, start_y + row*gap_y, *button_size)
        buttons.append({'rect': rect, 'text': text})
    
    return buttons

# --- Funciones de Registro de Puntuaciones ---

def load_scores():
    """Carga las puntuaciones existentes desde el archivo JSON."""
    try:
        with open(SCORES_FILE, 'r') as f:
            # Asegura que la dificultad por defecto sea 'NORMAL' si falta
            scores = json.load(f)
            for score in scores:
                if 'difficulty' not in score:
                    score['difficulty'] = 'NORMAL' 
            return scores
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Archivo de puntuaciones corrupto. Reiniciando historial.")
        return []

def save_score(name, final_score, final_level, difficulty):
    """Guarda la puntuación actual en el archivo JSON, incluyendo el nombre y dificultad."""
    
    new_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name": name if name else "Anonimo", 
        "score": final_score,
        "level": final_level,
        "difficulty": difficulty
    }
    
    scores_data = load_scores()
    scores_data.append(new_entry)
    
    try:
        # Ordenar antes de guardar para asegurar la coherencia
        sorted_scores = sorted(scores_data, key=lambda x: (x['score'], x['level']), reverse=True)
        with open(SCORES_FILE, 'w') as f:
            json.dump(sorted_scores, f, indent=4)
        print(f"Partida registrada: Jugador={name}, Puntos={final_score}")
    except IOError:
        print("Error al guardar el archivo de puntuaciones.")

# --- Funciones de Dibujo y Lógica del Juego ---

def draw_text(text, font, color, x, y, center=True):
    render = font.render(text, True, color)
    rect = render.get_rect(center=(x, y)) if center else render.get_rect(topleft=(x, y))
    screen.blit(render, rect)

def draw_buttons(highlight_idx=None, empty_mode=False):
    for idx, b in enumerate(buttons):
        color = LIGHT_BLUE if idx == highlight_idx else BLUE
        pygame.draw.rect(screen, color, b['rect'], border_radius=15)
        
        if not empty_mode: 
            draw_text(b['text'], font_big, WHITE, b['rect'].centerx, b['rect'].centery)

def show_game_info():
    """Muestra información del juego: Nivel, Vidas, Puntos y Dificultad."""
    diff_label = DIFFICULTY_SETTINGS.get(difficulty_mode, DIFFICULTY_SETTINGS['NORMAL'])['label']
    draw_text(f"Nivel: {level} ({diff_label}) Vidas: {lives} Puntos: {score}", font_small, BLACK, WIDTH//2, 25)

def generate_sequence(set_new_timer=True):
    """Genera una nueva secuencia y establece el temporizador si es necesario."""
    global sequence, max_time_per_level, sequence_display_time, time_remaining
    
    settings = DIFFICULTY_SETTINGS[difficulty_mode]
    sequence_display_time = settings['display_time']
    star_prob_base = settings['star_prob_base']
    star_prob_multiplier = settings['star_prob_multiplier']
    time_bonus = settings['time_bonus']
    
    create_buttons(level) 

    numbers_to_show = list(range(1, level + 1))
    
    star_probability = star_prob_base + (level - 1) * star_prob_multiplier
    star_probability = min(0.75, star_probability)
    
    star_index = -1
    if level >= 2 and random.random() < star_probability: 
        star_index = random.randint(0, level - 1)
        
    available_indices = list(range(len(buttons)))
    random.shuffle(available_indices)
    
    sequence = []
    num_to_generate = min(len(available_indices), level) 
    
    for i in range(num_to_generate):
        expected_num = numbers_to_show[i] 
        idx = available_indices[i]        
        
        symbol_to_display = str(expected_num)
        if i == star_index:
            symbol_to_display = '*'
            
        sequence.append((symbol_to_display, expected_num, idx))
        
    sequence.sort(key=lambda x: x[1])

    # Establecer temporizador
    if set_new_timer:
        max_time_per_level = time_bonus + (level * 0.3)
        time_remaining = max_time_per_level

def show_sequence_and_transition(seq):
    screen.fill(WHITE)
    create_buttons(level)
    draw_buttons(empty_mode=True) 
    show_game_info()
    
    for symbol, _, idx in seq:
        color_display = RED if symbol == '*' else YELLOW
        draw_text(symbol, font_big, color_display, buttons[idx]['rect'].centerx, buttons[idx]['rect'].centery)
        
    pygame.display.flip()
    
    time.sleep(sequence_display_time)
        
    screen.fill(WHITE)
    draw_buttons(empty_mode=True) 
    show_game_info()
    pygame.display.flip()
    time.sleep(0.5) 

def draw_progress_indicator(current, total):
    """Dibuja una barra de progreso de la secuencia de entrada."""
    bar_width = 300
    bar_height = 15
    bar_x = WIDTH//2 - bar_width//2
    bar_y = 85
    
    # Marco
    pygame.draw.rect(screen, BLACK, (bar_x - 2, bar_y - 2, bar_width + 4, bar_height + 4), 2, border_radius=5)
    
    # Progreso
    progress_ratio = current / total if total > 0 else 0
    fill_width = bar_width * progress_ratio
    
    progress_color = GREEN if progress_ratio == 1 else (YELLOW if progress_ratio > 0.5 else LIGHT_BLUE)
    
    pygame.draw.rect(screen, progress_color, (bar_x, bar_y, fill_width, bar_height), border_radius=5)
    draw_text(f"Paso {current}/{total}", font_small, BLACK, WIDTH//2, bar_y + bar_height + 15)


def show_input_screen():
    screen.fill(WHITE)
    create_buttons(level)
    draw_buttons(empty_mode=True) 
    show_game_info()
    
    # Contador de tiempo
    timer_text = f"Tiempo: {time_remaining:.1f}s"
    timer_color = RED if time_remaining < 3.0 else BLACK
    draw_text(timer_text, font_medium, timer_color, WIDTH//2, 45) 
    
    # Indicador de progreso
    draw_progress_indicator(player_input_count, level)
    
    # Instrucción
    next_number = player_input_count + 1
    
    if next_number <= level:
        draw_text(f"Marca la posición del: {next_number}", font_medium, BLACK, WIDTH//2, 130)
    
    pygame.display.flip()

def get_player_name_screen(name):
    """Muestra la pantalla para introducir el nombre."""
    screen.fill(WHITE)
    
    draw_text("PARTIDA TERMINADA", font_medium, BLACK, WIDTH//2, HEIGHT//3 - 50)
    draw_text(f"Puntuación: {score}", font_medium, BLUE, WIDTH//2, HEIGHT//3)
    
    draw_text("Introduce tu nombre y pulsa ENTER:", font_small, BLACK, WIDTH//2, HEIGHT//2 - 40)
    
    input_box = pygame.Rect(WIDTH//2 - 150, HEIGHT//2, 300, 50)
    pygame.draw.rect(screen, GRAY, input_box, border_radius=5)
    
    text_surface = font_input.render(name + ("_" if int(time.time() * 2) % 2 else ""), True, BLACK)
    screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))
    
    draw_text("Máx 10 caracteres (A-Z, 0-9)", font_small, GRAY, WIDTH//2, HEIGHT//2 + 80)
    
    pygame.display.flip()

def show_game_over():
    """Muestra la pantalla final después de guardar la puntuación."""
    screen.fill(WHITE)
    
    draw_text("HAS PERDIDO", font_big, RED, WIDTH//2, HEIGHT//3)
    draw_text(f"Puntuación final: {score}", font_medium, BLACK, WIDTH//2, HEIGHT//2)
    draw_text(f"Guardada como: {player_name if player_name else 'Anonimo'} ({DIFFICULTY_SETTINGS[difficulty_mode]['label']})", font_small, BLUE, WIDTH//2, HEIGHT//2 + 40)
    
    draw_text("Presiona R para JUGAR DE NUEVO", font_small, BLACK, WIDTH//2, HEIGHT*0.7)
    draw_text("o ESC para salir", font_small, GRAY, WIDTH//2, HEIGHT*0.7 + 30)
    
    pygame.display.flip()

def show_difficulty_select():
    """Permite seleccionar la dificultad mediante botones clicables."""
    global difficulty_rects
    screen.fill(WHITE)
    
    draw_text("SELECCIONA DIFICULTAD", font_big, BLUE, WIDTH//2, HEIGHT//4)
    
    button_width = 150
    button_height = 50
    gap = 20
    total_width = 3 * button_width + 2 * gap
    start_x = (WIDTH - total_width) // 2
    y_start = HEIGHT//2
    
    difficulty_rects.clear()
    
    for i, (key, settings) in enumerate(DIFFICULTY_SETTINGS.items()):
        rect_x = start_x + i * (button_width + gap)
        rect_y = y_start
        rect = pygame.Rect(rect_x, rect_y, button_width, button_height)
        difficulty_rects[key] = rect
        
        # Dibujar botón
        color = GREEN if key == 'EASY' else (YELLOW if key == 'NORMAL' else RED)
        pygame.draw.rect(screen, color, rect, border_radius=10)
        pygame.draw.rect(screen, DARK_GRAY, rect, 3, border_radius=10)
        
        # Texto del botón
        draw_text(settings['label'], font_medium, BLACK, rect.centerx, rect.centery)
        
    # Botón de Puntuaciones
    hof_button_rect = pygame.Rect(WIDTH//2 - 125, HEIGHT - 80, 250, 40)
    difficulty_rects['HALL_OF_FAME'] = hof_button_rect
    pygame.draw.rect(screen, ORANGE, hof_button_rect, border_radius=10)
    draw_text("MEJORES PUNTUACIONES", font_small, WHITE, hof_button_rect.centerx, hof_button_rect.centery)

    pygame.display.flip()

def show_level_transition():
    """Muestra la pantalla de transición de nivel (feedback positivo)."""
    screen.fill(LIGHT_BLUE)
    
    draw_text("¡NIVEL SUPERADO!", font_big, GREEN, WIDTH//2, HEIGHT//3)
    draw_text(f"Puntos ganados: {10 * (level - 1)}", font_medium, BLACK, WIDTH//2, HEIGHT//2)
    draw_text(f"Nuevo Nivel: {level}", font_medium, BLUE, WIDTH//2, HEIGHT//2 + 40)
    
    pygame.display.flip()
    time.sleep(1.5) 

def show_high_scores():
    """Muestra la tabla de las mejores puntuaciones, filtrada por dificultad, con botones de navegación."""
    global hof_nav_buttons
    screen.fill(WHITE)
    
    current_key = DIFFICULTY_KEYS[current_hof_difficulty_index]
    current_label = DIFFICULTY_SETTINGS[current_key]['label']
    
    draw_text("MEJORES PUNTUACIONES", font_big, YELLOW, WIDTH//2, 50)
    
    # Título de la tabla actual
    draw_text(f"Dificultad: {current_label}", font_medium, BLACK, WIDTH//2, 100)
    
    scores_data = load_scores()
    
    # 1. Filtrar por dificultad
    filtered_scores = [entry for entry in scores_data if entry.get('difficulty', 'NORMAL') == current_key]
    
    # 2. Ordenar las puntuaciones filtradas
    top_scores = sorted(filtered_scores, key=lambda x: (x['score'], x['level']), reverse=True)[:10]
    
    y_start = 150
    
    if not top_scores:
        draw_text("No hay puntuaciones registradas en esta dificultad.", font_small, GRAY, WIDTH//2, y_start)
    else:
        # Encabezados
        draw_text("POS.", font_small, BLACK, 50, y_start, center=False)
        draw_text("NOMBRE", font_small, BLACK, 120, y_start, center=False)
        draw_text("PUNTOS", font_small, BLACK, 250, y_start, center=False)
        draw_text("NIVEL", font_small, BLACK, 350, y_start, center=False)
        
        y_start += 30
        
        for i, entry in enumerate(top_scores):
            rank = i + 1
            name = entry.get("name", "Anónimo")
            score_val = entry.get("score", 0)
            level_val = entry.get("level", 1)
            
            draw_text(f"{rank}.", font_small, DARK_GRAY, 50, y_start, center=False)
            draw_text(name, font_small, BLUE, 120, y_start, center=False)
            draw_text(f"{score_val}", font_small, BLACK, 250, y_start, center=False)
            draw_text(f"{level_val}", font_small, BLACK, 350, y_start, center=False)
            
            y_start += 30
    
    # --- Botones de Navegación de Dificultad ---
    btn_size = 40
    btn_y = 90
    
    # Botón Izquierda
    left_rect = pygame.Rect(10, btn_y, btn_size, btn_size)
    hof_nav_buttons['LEFT'] = left_rect
    
    if current_hof_difficulty_index > 0:
        pygame.draw.rect(screen, BLUE, left_rect, border_radius=5)
        draw_text("←", font_medium, WHITE, left_rect.centerx, left_rect.centery)
    else:
        pygame.draw.rect(screen, GRAY, left_rect, border_radius=5)
        
    # Botón Derecha
    right_rect = pygame.Rect(WIDTH - 10 - btn_size, btn_y, btn_size, btn_size)
    hof_nav_buttons['RIGHT'] = right_rect
    
    if current_hof_difficulty_index < len(DIFFICULTY_KEYS) - 1:
        pygame.draw.rect(screen, BLUE, right_rect, border_radius=5)
        draw_text("→", font_medium, WHITE, right_rect.centerx, right_rect.centery)
    else:
        pygame.draw.rect(screen, GRAY, right_rect, border_radius=5)
        
    draw_text("Presiona ESC para volver | Clic para cambiar dificultad", font_small, GRAY, WIDTH//2, HEIGHT - 50)
    pygame.display.flip()

# --- Bucle principal ---
running = True
while running:
    
    # --- Actualización del Temporizador ---
    dt = clock.tick(30) / 1000.0
    
    if game_state == PLAYER_INPUT:
        time_remaining -= dt
        if time_remaining <= 0:
            time_remaining = 0
            # Castigo por tiempo agotado
            lives -= 1
            if lives <= 0:
                game_state = GET_NAME
            else:
                generate_sequence() 
                game_state = SHOW_SEQUENCE

    # --- Gestión de Estados ---
    if game_state == MENU:
        game_state = DIFFICULTY_SELECT 
    
    if game_state == DIFFICULTY_SELECT:
        show_difficulty_select()

    if game_state == SHOW_SEQUENCE:
        show_sequence_and_transition(sequence)
        player_input_count = 0 
        game_state = PLAYER_INPUT
        
    if game_state == LEVEL_TRANSITION:
        show_level_transition()
        generate_sequence() 
        game_state = SHOW_SEQUENCE
        
    if game_state == HALL_OF_FAME:
        show_high_scores()
        
    if game_state == GAME_OVER:
        show_game_over()
    
    if game_state == GET_NAME:
        get_player_name_screen(player_name)
        
    # --- Gestión de Eventos (Input) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif game_state == DIFFICULTY_SELECT:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                
                selected_diff = None
                
                for key, rect in difficulty_rects.items():
                    if rect.collidepoint(pos):
                        if key == 'HALL_OF_FAME':
                            game_state = HALL_OF_FAME
                            # Asegura que el índice de dificultad se inicialice en un valor válido, e.g., 'NORMAL' (índice 1)
                            current_hof_difficulty_index = 1 
                            break
                        else:
                            selected_diff = key
                            break
                
                if selected_diff:
                    # Inicialización de partida
                    difficulty_mode = selected_diff
                    level = 1
                    score = 0
                    lives = 3
                    player_name = ""
                    score_saved = False 
                    generate_sequence(set_new_timer=True)
                    game_state = SHOW_SEQUENCE
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                game_state = HALL_OF_FAME
                current_hof_difficulty_index = 1

        elif game_state == PLAYER_INPUT:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                
                clicked_idx = -1
                for idx, b in enumerate(buttons):
                    if b['rect'].collidepoint(pos):
                        clicked_idx = idx
                        break
                
                if clicked_idx != -1:
                    expected_number = player_input_count + 1 
                    
                    correct_idx = -1
                    if 1 <= expected_number <= level:
                        _, _, correct_idx = sequence[expected_number - 1] 

                    # Animación de clic 
                    screen.fill(WHITE)
                    draw_buttons(highlight_idx=clicked_idx, empty_mode=True) 
                    show_game_info()
                    draw_text(f"Marca la posición del: {expected_number}", font_medium, BLACK, WIDTH//2, 130)
                    pygame.display.flip()
                    time.sleep(0.15) 
                    
                    if clicked_idx == correct_idx:
                        player_input_count += 1
                        
                        time_remaining = max_time_per_level
                        
                        if player_input_count == level:
                            score += 10 * level
                            level += 1
                            
                            game_state = LEVEL_TRANSITION 

                    else:
                        lives -= 1
                        
                        # Muestra la posición correcta y el error
                        screen.fill(WHITE)
                        draw_buttons(highlight_idx=correct_idx, empty_mode=True) 
                        draw_text("¡Incorrecto!", font_medium, RED, WIDTH//2, 130)
                        show_game_info()
                        pygame.display.flip()
                        time.sleep(1.0) 

                        if lives <= 0:
                            game_state = GET_NAME 
                        else:
                            generate_sequence()
                            game_state = SHOW_SEQUENCE 

        elif game_state == GET_NAME:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    save_score(player_name, score, level, difficulty_mode)
                    game_state = GAME_OVER
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    if len(player_name) < 10 and event.unicode.isalnum():
                        player_name += event.unicode.upper() 

        elif game_state == GAME_OVER:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_state = DIFFICULTY_SELECT
                elif event.key == pygame.K_ESCAPE:
                    running = False
        
        elif game_state == HALL_OF_FAME:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state = DIFFICULTY_SELECT
                # Las teclas de flecha siguen funcionando como alternativa
                elif event.key == pygame.K_RIGHT:
                    if current_hof_difficulty_index < len(DIFFICULTY_KEYS) - 1:
                        current_hof_difficulty_index += 1
                elif event.key == pygame.K_LEFT:
                    if current_hof_difficulty_index > 0:
                        current_hof_difficulty_index -= 1
            
            # Manejo de clics de los nuevos botones de navegación
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                
                if 'LEFT' in hof_nav_buttons and hof_nav_buttons['LEFT'].collidepoint(pos):
                    if current_hof_difficulty_index > 0:
                        current_hof_difficulty_index -= 1
                
                elif 'RIGHT' in hof_nav_buttons and hof_nav_buttons['RIGHT'].collidepoint(pos):
                    if current_hof_difficulty_index < len(DIFFICULTY_KEYS) - 1:
                        current_hof_difficulty_index += 1

    
    if game_state not in [MENU, DIFFICULTY_SELECT, HALL_OF_FAME, GAME_OVER, GET_NAME]:
        show_input_screen()
    
    clock.tick(30)

pygame.quit()
sys.exit()