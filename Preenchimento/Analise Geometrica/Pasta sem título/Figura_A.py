import pygame
import sys

# Configurações para o preenchimento no pygame
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (0, 0, 0)  # Fundo preto
FILL_COLOR = (255, 0, 0)      # Preenchimento vermelho
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

# Função para calcular o centro geométrico de um polígono
def calculate_centroid(points):
    x_sum = sum(point[0] for point in points)
    y_sum = sum(point[1] for point in points)
    centroid_x = x_sum // len(points)
    centroid_y = y_sum // len(points)
    return (centroid_x, centroid_y)

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Preenchimento Figura A")

# Desenhe a figura original
screen.fill(BACKGROUND_COLOR)
points = [(160, 260), (140, 300), (300, 280), (310, 250), (210, 180), (100, 220)]
pygame.draw.polygon(screen, LINE_COLOR, points, LINE_WIDTH)
pygame.display.update()

# Calcule o centro geométrico da figura
centroid = calculate_centroid(points)

# Aguarde um momento antes de iniciar o preenchimento
pygame.time.delay(1000)

# Execute o preenchimento a partir do centro da figura
scanline_fill(screen, centroid[0], centroid[1], FILL_COLOR)

# Mantenha a janela aberta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
