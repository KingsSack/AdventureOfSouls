import pygame

BACKGROUND_SIZE = (48, 48)
ICON_SIZE = (36, 36)

def load_and_blit_image(screen, file_path, scale_size, position):
    image = pygame.image.load(file_path)
    image = pygame.transform.scale(image, scale_size)
    screen.blit(image, position)

SPELL_IMAGES = {
    "fireball": "menu/Firebomb.png",
    "thunder": "menu/Bolt.png",
    "empty": "menu/Lock.png"
}