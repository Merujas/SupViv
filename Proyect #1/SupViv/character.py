import pygame
import constants
import os
from world import Tree
from game_resources import *
from sprites import load_sprites_from_folder

# Mecánicas de Personajes
class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.inventory = {"wood": 0, "stone": 0, "meat": 0}

        # Cargar sprites desde la carpeta
        sprite_folder = os.path.join("SupViv", "assets", "character", "sprites", "Walk")
        self.sprites = load_sprites_from_folder(sprite_folder)

        print(self.sprites)  # Imprimir los sprites cargados para depuración

        # Inicializar claves de dirección si no están presentes
        directions = ["down", "up", "left", "right", "down_left", "down_right", "up_left", "up_right"]
        for direction in directions:
            if direction not in self.sprites or not self.sprites[direction]:
                self.sprites[direction] = []  # Asegurar que todas las direcciones existen

        # Configuración inicial de animación
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_delay = 0.1  # Retraso entre frames (en segundos)
        self.direction = "down"  # Dirección inicial

        # Verificar si los sprites para la dirección inicial están disponibles
        if self.direction not in self.sprites or not self.sprites[self.direction]:
            print(f"Advertencia: No se encontraron sprites para la dirección '{self.direction}'.")
            self.image = pygame.Surface((32, 32))  # Imagen predeterminada (un rectángulo vacío)
            self.image.fill((255, 0, 0))  # Color rojo para indicar error
        else:
            self.image = self.sprites[self.direction][self.current_frame]  # Sprite actual

    def get_mask(self):
        return pygame.mask.from_surface(self.image)

    def draw(self, screen, camera):
        screen_x = self.x - camera.x
        screen_y = self.y - camera.y
        screen.blit(self.image, (screen_x, screen_y))

    def check_collision(self, obj, new_x, new_y):
        character_rect = pygame.Rect(new_x, new_y, self.image.get_width(), self.image.get_height())
        offset_x = int(obj.x - new_x)
        offset_y = int(obj.y - new_y)
        return self.get_mask().overlap(obj.get_mask(), (offset_x, offset_y)) is not None

    def move(self, dx, dy, world):
        new_x = self.x + dx * self.speed
        can_move_x = True
        for tree in world.trees: 
            if self.check_collision(tree, new_x, self.y):
                can_move_x = False
                break
        if can_move_x:
            self.x = new_x

        new_y = self.y + dy * self.speed
        can_move_y = True
        for tree in world.trees:
            if self.check_collision(tree, self.x, new_y):
                can_move_y = False
                break
        if can_move_y:
            self.y = new_y

    def update(self, dt, world):
    # Obtener teclas presionadas
        keys = pygame.key.get_pressed()

    # Determinar la dirección del movimiento (priorizando diagonales)
        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            self.direction = "up_left"
            self.move(-1, -1, world)
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            self.direction = "up_right"
            self.move(1, -1, world)
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.direction = "down_left"
            self.move(-1, 1, world)
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self.direction = "down_right"
            self.move(1, 1, world)
        elif keys[pygame.K_UP]:
            self.direction = "up"
            self.move(0, -1, world)
        elif keys[pygame.K_DOWN]:
            self.direction = "down"
            self.move(0, 1, world)
        elif keys[pygame.K_LEFT]:
            self.direction = "left"
            self.move(-1, 0, world)
        elif keys[pygame.K_RIGHT]:
            self.direction = "right"
            self.move(1, 0, world)
        else:
        # Si no se presiona ninguna tecla, restablecer al primer frame
            self.current_frame = 0

    # Actualizar animación solo si hay sprites disponibles para la dirección
        if self.direction in self.sprites and self.sprites[self.direction]:
            current_time = pygame.time.get_ticks() / 1000  # Tiempo en segundos
            if any(keys):  # Solo actualizar si alguna tecla está presionada
                if current_time - self.animation_timer >= self.animation_delay:
                    self.current_frame = (self.current_frame + 1) % len(self.sprites[self.direction])
                    self.animation_timer = current_time
            else:
            # Si no se presiona ninguna tecla, restablecer al primer frame
                self.current_frame = 0

        # Actualizar el sprite actual
            self.image = self.sprites[self.direction][self.current_frame]
        else:
            print(f"Advertencia: No hay sprites cargados para la dirección '{self.direction}'.")
            self.image = pygame.Surface((32, 32))  # Imagen predeterminada (un rectángulo vacío)
            self.image.fill((255, 0, 0))  # Color rojo para indicar error
