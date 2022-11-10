import pygame

size = width, height = 852, 480
green = 25, 255, 25
black = 0, 0, 0
ground = 153, 77, 0
path = 153, 102, 0
special_path = 125, 80, 40

screen = pygame.display.set_mode(size)

def paths(design):
    if design == "y":
        pygame.draw.rect(screen, path, [width / 2 - 500, height / 2 - 30, 1000, 80])
        pygame.draw.rect(screen, path, [width / 2 - 30, 0, 60, 220])
    
    if design == "spell1":
        pygame.draw.rect(screen, path, [width / 2 - 500, height / 2 - 25, 1000, 80])
        pygame.draw.rect(screen, path, [width / 2 - 30, height / 2 + 20, 60, 220])
        pygame.draw.rect(screen, special_path, [width / 2 - 60, height / 2 - 36, 120, 120], 0, 46)
    
    if design == "horizantal":
        pygame.draw.rect(screen, path, [width / 2 - 500, height / 2 - 25, 1000, 80])
        