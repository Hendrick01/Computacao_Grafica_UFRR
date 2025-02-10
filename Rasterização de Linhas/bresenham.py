import pygame
import sys

# Configuração da janela
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Rasterização de Linhas - Algoritmo de Bresenham")

# Função para rasterizar uma linha usando o algoritmo de Bresenham
def draw_line_bresenham(x1, y1, x2, y2):
  dx = abs(x2 - x1)
  dy = abs(y2 - y1)
  p = 2 * dy - dx
  two_dy = 2 * dy
  two_dy_minus_dx = 2 * (dy - dx)

  if x1 > x2:
    x1, x2 = x2, x1
    y1, y2 = y2, y1

  x, y = x1, y1

  pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)

  while x < x2:
    x += 1
    if p < 0:
      p += two_dy
    else:
      y += 1 if y1 < y2 else -1
      p += two_dy_minus_dx

    pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)

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
  draw_line_bresenham(x1, y1, x2, y2)
  pygame.display.flip()

pygame.quit()
sys.exit()