import pygame
pygame.init()

WIDTH = 500
HEIGHT = 650
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

main_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graphic primitives")

#draw a rectangle
pygame.draw.rect(main_window, WHITE, (10, 10, 60, 60))
# draw a rectangle without filling
pygame.draw.rect(main_window, RED, (80, 10, 60, 60), 3)
# simple line
pygame.draw.line(main_window, BLUE, (10,80), (140, 80), 4)
# smoothed line
pygame.draw.aaline(main_window, BLUE, (10,100), (140, 100))
#closed line
pygame.draw.lines(main_window, BLUE, True, [(10,120), (80, 120), (80, 180)], 2)
# smoothed closed line
pygame.draw.aalines(main_window, BLUE, True, [(10,220), (80, 220), (80, 300)], 2)
# polygon
pygame.draw.polygon(main_window, WHITE, [[50,340], [180,360], [180,460], [30,430]])
# filled poligon
pygame.draw.polygon(main_window, WHITE, [[250,340], [380,360], [380,460], [230,430]], 2)
# circle
pygame.draw.circle(main_window, RED, (300, 80), 50)
# ellipse
pygame.draw.ellipse(main_window, RED, (300, 180, 120, 100 ), 5)


# update the client side
pygame.display.update()

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
