import pygame
pygame.init()

WIDTH = 500
HEIGHT = 650
FPS = 1

main_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_window("My first program on pygame")
clock = pygame.time.Clock()

flRunning = True
while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
    clock.tick(FPS)


print("The program has terminated")
