import constants
import pygame

class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0

    def update(self, target_x, target_y):
        """
        Actualiza la posición de la cámara para seguir al objetivo (personaje).
        """
        self.x = target_x - constants.width // 2
        self.y = target_y - constants.height // 2

        # Limitar la cámara dentro del mapa
        self.x = max(0, min(self.x, constants.width * 10 - constants.width))
        self.y = max(0, min(self.y, constants.height * 10 - constants.height))