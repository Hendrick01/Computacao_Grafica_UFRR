import pygame
import sys

# Configurações para o preenchimento no pygame
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (0, 0, 0)  # Fundo preto
FILL_COLOR = (255, 0, 0)      # Preenchimento vermelho
LINE_COLOR = (255, 255, 255)  # Linha branca
LINE_WIDTH = 2

# Função de preenchimento usando análise geométrica
def scanline_fill(screen, x, y, fill_color):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
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
                    stack.append((i, y - 1))
                if y + 1 < HEIGHT and screen.get_at((i, y + 1)) != LINE_COLOR:
                    stack.append((i, y + 1))
                pygame.display.update()

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retangulo de Preenchimento")

# Desenhe a figura original
screen.fill(BACKGROUND_COLOR)
pygame.draw.rect(screen, LINE_COLOR, (50, 100, 300, 200), LINE_WIDTH)
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
