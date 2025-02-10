import pygame
import sys

# Configurações para o preenchimento no pygame
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (0, 0, 0)  # Fundo preto
FILL_COLOR = (255, 0, 0)      # Preenchimento vermelho
LINE_COLOR = (255, 255, 255)  # Linha branca
LINE_WIDTH = 2

# Função para criar uma máscara do polígono
def create_polygon_mask(points):
    mask_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.polygon(mask_surface, (255, 255, 255, 255), points)
    return pygame.mask.from_surface(mask_surface)

# Função de preenchimento de baixo para cima dentro da figura
def bottom_to_top_fill(screen, fill_color, mask):
    for y in range(HEIGHT - 1, -1, -1):  # De baixo para cima
        for x in range(WIDTH):
            if mask.get_at((x, y)):
                current_color = screen.get_at((x, y))
                if current_color != LINE_COLOR and current_color != fill_color:
                    screen.set_at((x, y), fill_color)
        pygame.display.update()
        pygame.time.delay(20)  

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Preenchimento Figura A")

# Desenhe a figura original
screen.fill(BACKGROUND_COLOR)
points = [(160, 260), (140, 300), (300, 280), (310, 250), (210, 180), (100, 220)]
pygame.draw.polygon(screen, LINE_COLOR, points, LINE_WIDTH)
pygame.display.update()

# Criar máscara do polígono
polygon_mask = create_polygon_mask(points)

# Aguarde um momento antes de iniciar o preenchimento
pygame.time.delay(1000)

# Execute o preenchimento de baixo para cima dentro da figura
bottom_to_top_fill(screen, FILL_COLOR, polygon_mask)

# Mantenha a janela aberta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()

