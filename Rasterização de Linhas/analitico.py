import pygame
import sys

# Função para rasterização analítica
def rasterizacao_analitica(x1, y1, x2, y2):
    pontos = []
    if x1 == x2:
        # Linha vertical
        for y in range(min(y1, y2), max(y1, y2) + 1):
            pontos.append((x1, y))
    else:
        # Calcula a inclinação da reta
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        for x in range(min(x1, x2), max(x1, x2) + 1):
            y = int(m * x + b)
            pontos.append((x, y))
    return pontos

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Rasterização de Linhas - Algoritmo Analítico")
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Função para desenhar pontos na tela
def desenhar_pontos(pontos, cor):
    for ponto in pontos:
        pygame.draw.circle(tela, cor, ponto, 1)

# Função principal
def main():
    # Pontos de exemplo
    x1, y1 = 100, 100
    x2, y2 = 300, 500

    # Rasterização usando o algoritmo analítico
    pontos_analitico = rasterizacao_analitica(x1, y1, x2, y2)

    # Loop principal
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Limpa a tela
        tela.fill(PRETO)

        # Desenha os pontos gerados pelo algoritmo analítico
        desenhar_pontos(pontos_analitico, VERMELHO)

        # Atualiza a tela
        pygame.display.flip()

if __name__ == "__main__":
    main()
