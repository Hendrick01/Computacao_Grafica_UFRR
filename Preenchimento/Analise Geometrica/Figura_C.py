import pygame
import sys

# Configurações para o preenchimento no pygame
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (0, 0, 0)  # Fundo preto
FILL_COLOR = (255, 0, 0)      # Preenchimento vermelho
LINE_COLOR = (255, 255, 255)  # Linha branca
LINE_WIDTH = 2

# Função para verificar se um ponto está dentro do polígono
def is_inside_polygon(x, y, points):
    surface = pygame.Surface((WIDTH, HEIGHT))
    surface.fill((0, 0, 0))
    pygame.draw.polygon(surface, (255, 255, 255), points)
    return surface.get_at((x, y)) == (255, 255, 255, 255)

# Função de preenchimento de baixo para cima
def bottom_to_top_fill(screen, fill_color, points):
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    for y in range(max_y, min_y, -1): 
        for x in range(min_x, max_x):
            if is_inside_polygon(x, y, points):
                current_color = screen.get_at((x, y))
                if current_color != LINE_COLOR and current_color != fill_color:
                    screen.set_at((x, y), fill_color)
        pygame.display.update()
        pygame.time.delay(20)  

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

# Execute o preenchimento de baixo para cima
bottom_to_top_fill(screen, FILL_COLOR, points)

# Mantenha a janela aberta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()

