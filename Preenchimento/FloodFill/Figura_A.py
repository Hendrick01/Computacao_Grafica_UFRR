import pygame
import sys

# Configurações para o preenchimento no pygame
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (0, 0, 0)  # Fundo preto
FILL_COLOR = (255, 0, 0)      # Preenchimento vermelho
LINE_COLOR = (255, 255, 255)  # Linha branca
LINE_WIDTH = 2

# Função de preenchimento usando FloodFill
def flood_fill(screen, x, y, target_color, fill_color):
    to_fill = [(x, y)]
    while to_fill:
        x, y = to_fill.pop()
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            continue
        current_color = screen.get_at((x, y))
        if current_color == target_color:
            screen.set_at((x, y), fill_color)
            to_fill.append((x + 1, y))
            to_fill.append((x, y + 1))
            to_fill.append((x - 1, y))
            to_fill.append((x, y - 1))
        pygame.display.update()

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flood Fill Figura A")

# Desenhe o polígono original
screen.fill(BACKGROUND_COLOR)
points = [(160, 260), (140, 300), (300, 280), (310, 250), (210, 180), (100, 220)]
pygame.draw.polygon(screen, LINE_COLOR, points, LINE_WIDTH)
pygame.display.update()

# Aguarde um momento antes de iniciar o preenchimento
pygame.time.delay(1000)

# Execute o preenchimento a partir do ponto (225, 225) dentro do polígono
flood_fill(screen, 225, 225, BACKGROUND_COLOR, FILL_COLOR)

# Mantenha a janela aberta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
