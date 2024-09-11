import pygame
import game
import sys


def exit():
    pygame.quit()
    sys.exit()


def main():
    size = 852, 480
    max_frame_rate = 60
    title = "Adventure of Souls"

    pygame.init()

    flags = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
    screen = pygame.display.set_mode(size, flags)
 
    pygame.display.set_caption(title)

    clock = pygame.time.Clock()

    game_manager = game.GameManager(screen)
    print(game_manager.savedata.data)

    while game_manager.running:
        mouse = pygame.mouse.get_pos()
        events = pygame.event.get()
        pressed_keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.QUIT:
                game_manager.running = False

        game_manager.update(mouse, events, pressed_keys)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(max_frame_rate)

    exit()

if __name__ == "__main__":
    main()
