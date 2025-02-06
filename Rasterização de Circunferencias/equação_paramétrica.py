import pygame
import math

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da janela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rasterização de Circunferências")

# Função para rasterizar uma circunferência usando a equação paramétrica
def draw_circle_parametric(center_x, center_y, radius):
    for angle in range(0, 360):
        x = int(center_x + radius * math.cos(math.radians(angle)))
        y = int(center_y + radius * math.sin(math.radians(angle)))
        screen.set_at((x, y), (255, 255, 255))  # Define a cor do pixel

# Parâmetros da circunferência
center_x, center_y = width // 2, height // 2
radius = 100

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Limpa a tela
    draw_circle_parametric(center_x, center_y, radius)
    pygame.display.flip()

pygame.quit()