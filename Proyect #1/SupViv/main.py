

import pygame
import sys
import constants
from character import Character
from world import World
from camera import Camera


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.width, constants.height))
    pygame.display.set_caption("SupViv")

    clock = pygame.time.Clock()
    world = World(constants.width, constants.height)
    character = Character(constants.width // 2, constants.height // 2)
    camera = Camera(constants.width, constants.height)

    while True:
        # Calcular el tiempo transcurrido
        dt = clock.tick(60) / 1000.0

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Actualizar lógica del juego
        character.update(dt, world)
        camera.update(character.x, character.y)
        world.update_chunks(character.x, character.y)

        # Dibujar en pantalla
        screen.fill(constants.black)  # Fondo negro
        world.draw(screen, camera.x, camera.y)
        character.draw(screen, camera)
        pygame.display.flip()

if __name__ == "__main__":
    main()