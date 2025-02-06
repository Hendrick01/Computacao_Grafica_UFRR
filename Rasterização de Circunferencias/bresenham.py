import pygame

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da janela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rasterização de Circunferências")

# Função para rasterizar uma circunferência usando o algoritmo de Bresenham
def draw_circle_bresenham(center_x, center_y, radius):
    x, y = 0, radius
    d = 3 - 2 * radius
    while x <= y:
        screen.set_at((center_x + x, center_y + y), (255, 255, 255))
        screen.set_at((center_x - x, center_y + y), (255, 255, 255))
        screen.set_at((center_x + x, center_y - y), (255, 255, 255))
        screen.set_at((center_x - x, center_y - y), (255, 255, 255))
        screen.set_at((center_x + y, center_y + x), (255, 255, 255))
        screen.set_at((center_x - y, center_y + x), (255, 255, 255))
        screen.set_at((center_x + y, center_y - x), (255, 255, 255))
        screen.set_at((center_x - y, center_y - x), (255, 255, 255))
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1

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
    draw_circle_bresenham(center_x, center_y, radius)
    pygame.display.flip()

pygame.quit()