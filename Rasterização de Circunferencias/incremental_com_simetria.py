import pygame
import numpy as np

def incremental_symmetry_circle(radius, center=(0, 0)):
    teta = 1 / radius
    cos = np.cos(teta)
    sin = np.sin(teta)
    x = radius
    y = 0
    points = []
    
    while x >= y:
        points.append((center[0] + int(x), center[1] + int(y)))
        points.append((center[0] + int(y), center[1] + int(x)))
        points.append((center[0] - int(x), center[1] + int(y)))
        points.append((center[0] - int(y), center[1] + int(x)))
        points.append((center[0] + int(x), center[1] - int(y)))
        points.append((center[0] + int(y), center[1] - int(x)))
        points.append((center[0] - int(x), center[1] - int(y)))
        points.append((center[0] - int(y), center[1] - int(x)))
        
        t = x * cos - y * sin
        y = x * sin + y * cos
        x = t
    
    return points

def draw_circle(screen, xc, yc, r):
    points = incremental_symmetry_circle(r, (xc, yc))
    for point in points:
        screen.set_at(point, (255, 255, 255))

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Rasterização de Circunferência")
    screen.fill((0, 0, 0))
    
    draw_circle(screen, 400, 400, 200)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()

