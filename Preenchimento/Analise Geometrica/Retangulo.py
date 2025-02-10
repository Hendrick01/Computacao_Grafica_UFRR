import pygame
import sys

# Configurações para o preenchimento no pygame
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (0, 0, 0)  # Fundo preto
FILL_COLOR = (255, 0, 0)      # Preenchimento vermelho
LINE_COLOR = (255, 255, 255)  # Linha branca
LINE_WIDTH = 2

# Função de preenchimento de baixo para cima
def bottom_to_top_fill(screen, fill_color, rect):
    x_start, y_start, width, height = rect
    for y in range(y_start + height - 1, y_start - 1, -1):  
        for x in range(x_start, x_start + width):
            current_color = screen.get_at((x, y))
            if current_color != LINE_COLOR and current_color != fill_color:
                screen.set_at((x, y), fill_color)
        pygame.display.update()
        pygame.time.delay(20) 

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Preenchimento Retângulo")

# Desenhe a figura
screen.fill(BACKGROUND_COLOR)
rect = (50, 100, 300, 200)
pygame.draw.rect(screen, LINE_COLOR, rect, LINE_WIDTH)
pygame.display.update()

# Aguarde um momento antes de iniciar o preenchimento
pygame.time.delay(1000)

# Execute o preenchimento de baixo para cima
bottom_to_top_fill(screen, FILL_COLOR, rect)

# Mantenha a janela aberta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()

