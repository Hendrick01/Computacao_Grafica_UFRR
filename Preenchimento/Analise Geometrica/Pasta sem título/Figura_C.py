import pygame
import sys

# Configurações para o preenchimento no pygame
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (0, 0, 0)  # Fundo preto
FILL_COLOR = (255, 0, 0)      # Preenchimento azul
LINE_COLOR = (255, 255, 255)  # Linha branca
LINE_WIDTH = 2


# Função de preenchimento usando análise geométrica
from collections import deque  # Importa a estrutura de fila

def scanline_fill(screen, x, y, fill_color):
    queue = deque([(x, y)])  # Usa uma fila em vez de uma pilha
    while queue:
        x, y = queue.popleft()  # Remove o primeiro elemento da fila
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            continue
        current_color = screen.get_at((x, y))
        if current_color != LINE_COLOR and current_color != fill_color:
            left_x = x
            right_x = x
            while left_x >= 0 and screen.get_at((left_x, y)) != LINE_COLOR:
                left_x -= 1
            while right_x < WIDTH and screen.get_at((right_x, y)) != LINE_COLOR:
                right_x += 1
            for i in range(left_x + 1, right_x):
                screen.set_at((i, y), fill_color)
                if y - 1 >= 0 and screen.get_at((i, y - 1)) != LINE_COLOR:
                    queue.append((i, y - 1))  # Adiciona à fila
                if y + 1 < HEIGHT and screen.get_at((i, y + 1)) != LINE_COLOR:
                    queue.append((i, y + 1))  # Adiciona à fila
                pygame.display.update()

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Preenchimento Figura C")

# Desenhe a figura
screen.fill(BACKGROUND_COLOR)
points = [(230, 150), (200, 170), (170, 150), (100, 150), (100, 200), (200, 270), (300, 200), (300, 150)]
pygame.draw.polygon(screen, LINE_COLOR, points, LINE_WIDTH)
pygame.display.update()

# Aguarde um momento antes de iniciar o preenchimento
pygame.time.delay(1000)

# Execute o preenchimento a partir do centro da figura usando análise geométrica
scanline_fill(screen, 200, 200, FILL_COLOR)

# Mantenha a janela aberta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
