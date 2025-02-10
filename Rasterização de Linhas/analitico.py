import pygame

def analytical_line(x1, y1, x2, y2):
    points = []
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            points.append((x1, y))
    else:
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        for x in range(min(x1, x2), max(x1, x2) + 1):
            y = m * x + b
            points.append((x, round(y)))
    return points

def draw_line(screen, x1, y1, x2, y2, color, pixel_size=3):
    points = analytical_line(x1, y1, x2, y2)
    for point in points:
        pygame.draw.rect(screen, color, (point[0] * pixel_size, point[1] * pixel_size, pixel_size, pixel_size))

def main():
    pygame.init()
    pixel_size = 20  
    screen_size = 500
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Rasterização de Linha Analítica")
    screen.fill((0, 0, 0))
    
    draw_line(screen, 0, 0, 5, 2, (255, 0, 0), pixel_size)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
