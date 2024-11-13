import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash Clone")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)

# Variables del jugador
player_size = 40
player_x = 50
player_y = HEIGHT - player_size
player_velocity_y = 0
jump = False
gravity = 0.8

# Configuración de obstáculos
obstacle_width = 30
obstacle_height = 60
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height
obstacle_velocity = 5

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Bucle principal del juego
while True:
    window.fill(WHITE)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jump:
                jump = True
                player_velocity_y = -15  # Velocidad de salto

    # Movimiento del jugador (gravedad y salto)
    if jump:
        player_y += player_velocity_y
        player_velocity_y += gravity
        if player_y >= HEIGHT - player_size:
            player_y = HEIGHT - player_size
            jump = False

    # Movimiento del obstáculo
    obstacle_x -= obstacle_velocity
    if obstacle_x < -obstacle_width:
        obstacle_x = WIDTH

    # Dibujar jugador y obstáculo
    pygame.draw.rect(window, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(window, BLUE, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Detectar colisiones
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    if player_rect.colliderect(obstacle_rect):
        print("¡Has perdido!")
        pygame.quit()
        sys.exit()

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(30)  # FPS del juego
       