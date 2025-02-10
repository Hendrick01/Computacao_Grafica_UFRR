import pygame
import sys
from collections import deque  # Importa a estrutura de fila

# Configurações para o preenchimento no pygame
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (0, 0, 0)  # Fundo preto
FILL_COLOR = (255, 0, 0)      # Preenchimento vermelho
LINE_COLOR = (255, 255, 255)  # Linha branca
LINE_WIDTH = 2

# Função de preenchimento usando análise geométrica e fila (FIFO)
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

# Função para calcular o centro geométrico de um retângulo
def calculate_centroid(rect):
    x, y, width, height = rect
    centroid_x = x + width // 2
    centroid_y = y + height // 2
    return (centroid_x, centroid_y)

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Preenchimento Retangulo")

# Desenhe o retângulo original
rect = (50, 100, 300, 200)  # (x, y, largura, altura)
screen.fill(BACKGROUND_COLOR)
pygame.draw.rect(screen, LINE_COLOR, rect, LINE_WIDTH)
pygame.display.update()

# Calcule o centro geométrico do retângulo
centroid = calculate_centroid(rect)

# Aguarde um momento antes de iniciar o preenchimento
pygame.time.delay(1000)

# Execute o preenchimento a partir do centro do retângulo
scanline_fill(screen, centroid[0], centroid[1], FILL_COLOR)

# Mantenha a janela aberta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
