import pygame

size = width, height = 852, 480
green = 25, 255, 25
black = 0, 0, 0
ground = 153, 77, 0
path = 153, 102, 0

screen = pygame.display.set_mode(size)

def paths(design):
    if design == "y":
        pygame.draw.rect(screen, path, [width / 2 - 500, height / 2 - 30, 1000, 80])
        pygame.draw.rect(screen, path, [width / 2 - 30, 0, 60, 220])