import pygame

def plot_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r  # Inicialização do parâmetro de decisão
    points = []
    
    def plot_symmetric_points(xc, yc, x, y):
        symmetric_points = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]
        points.extend(symmetric_points)
    
    plot_symmetric_points(xc, yc, x, y)
    
    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        plot_symmetric_points(xc, yc, x, y)
    
    return points

def draw_circle(screen, xc, yc, r):
    points = plot_circle(xc, yc, r)
    for point in points:
        screen.set_at(point, (255, 255, 255))

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Rasterização de Circunferência")
    screen.fill((0, 0, 0))
    
    draw_circle(screen, 400, 400, 400)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()

