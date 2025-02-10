import pygame
import sys

# Configurações para o preenchimento no pygame
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (0, 0, 0)  # Fundo preto
FILL_COLOR = (255, 0, 0)      # Preenchimento vermelho
LINE_COLOR = (255, 255, 255)  # Linha branca
LINE_WIDTH = 2

# Função para verificar se um ponto está dentro do círculo
def is_inside_circle(x, y, center_x, center_y, radius):
    return (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2

# Função de preenchimento de baixo para cima dentro do círculo
def bottom_to_top_fill(screen, fill_color, center_x, center_y, radius):
    for y in range(center_y + radius, center_y - radius, -1):  # De baixo para cima
        for x in range(center_x - radius, center_x + radius):
            if is_inside_circle(x, y, center_x, center_y, radius):
                current_color = screen.get_at((x, y))
                if current_color != LINE_COLOR and current_color != fill_color:
                    screen.set_at((x, y), fill_color)
        pygame.display.update()
        pygame.time.delay(20)  


# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Círculo de preenchimento")

# Desenhe o círculo original
screen.fill(BACKGROUND_COLOR)
center_x, center_y, radius = 200, 200, 100
pygame.draw.circle(screen, LINE_COLOR, (center_x, center_y), radius, LINE_WIDTH)
pygame.display.update()

# Aguarde um momento antes de iniciar o preenchimento
pygame.time.delay(1000)

# Execute o preenchimento de baixo para cima dentro do círculo
bottom_to_top_fill(screen, FILL_COLOR, center_x, center_y, radius)

# Mantenha a janela aberta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()

