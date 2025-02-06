import pygame
import sys

# Configuração da janela
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Rasterização de Linhas - Algoritmo Analítico")

# Função para rasterizar uma linha usando o algoritmo analítico
def draw_line_analytic(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1

    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) >= abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    x_increment = dx / steps
    y_increment = dy / steps

    x, y = x1, y1
    for _ in range(int(steps) + 1):
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 1)
        x += x_increment
        y += y_increment

    pygame.display.flip()

# Ponto de partida e destino da linha
x1, y1 = 100, 100
x2, y2 = 300, 300

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_line_analytic(x1, y1, x2, y2)
    pygame.display.flip()

pygame.quit()
sys.exit()
