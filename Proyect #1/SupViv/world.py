import pygame
import constants
import random
import os
from game_resources import *
from character import *
import camera


class WorldChunk:

    # Representa un segmento del mundo con sus propios elementos"
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    # Crea una semilla unica basada en as coordinadas del chunk
        chunk_seed = hash(f"{x},{y}")
    # Guarda el estado actual del random
        old_state = random.getstate()
    # Establece la semilla para el random
        random.seed(chunk_seed)
    # Restaura el estado anterior del random
        random.setstate(old_state)
    # Genera elementos del chunk

        #Lista de arboles
        self.trees = [
            Tree(self.x + random.randint(0, self.width - constants.Tree),
                  self.y + random.randint(0, self.height - constants.Tree))
                  for _ in range(6)
        ]

        #Lista de arboles2
        self.trees2 = [
            Tree2(self.x + random.randint(0, self.width - constants.Tree2),
                   self.y + random.randint(0, self.height - constants.Tree2))
                   for _ in range(6)
        ]
        #Lista de carne
        self.meats = [
            Meet(self.x + random.randint(0, self.width - constants.Meat),
                 self.y + random.randint(0, self.height - constants.Meat))
                 for _ in range(4)
        ]
        #Lista de piedras
        self.stones = [
            Stones(self.x + random.randint(0, self.width - constants.Stone),
                  self.y + random.randint(0, self.height - constants.Stone))
                  for _ in range(10)
        ]
        # Restaura el estado anterior del random
        random.setstate(old_state)
    
    def draw(self, screen, grass_image, camera_x, camera_y):
        # dibujar el pasto en este chunk con ofset de camara

        chunk_screen_x = self.x + camera_x
        chunk_screen_y = self.y + camera_y

        #calcula el rango de tiles de pasto visibles con un tile extra para evitar lineas
        start_x = max(0, camera_x + self.x - constants.Grass// constants.Grass)
        end_x = min(self.width // constants.Grass +1,
                    (camera_x + constants.width - self.x + constants.Grass) // constants.Grass +1)
        start_y = max(0, camera_y + self.x - constants.Grass// constants.Grass)
        end_y = min(self.height // constants.Grass +1,
                    (camera_y + constants.height - self.y + constants.Grass) // constants.Grass +1)

        for y in range(int(start_y), int(end_y)):
            for x in range(int(start_x), int(end_x)):
                screen_x = self.x + x * constants.Grass - camera_x
                screen_y = self.y + y * constants.Grass - camera_y
                screen.blit(grass_image, (screen_x, screen_y))
        # Dibujar elementos solo si estan en pantalla
        for tree in self.trees + self.trees2:
            tree_screen_x = tree.x - camera_x
            tree_screen_y = tree.y - camera_y
            if(tree_screen_x + tree.size >= 0 and tree_screen_x <= constants.width and
               tree_screen_y + tree.size >= 0 and tree_screen_y <= constants.height):
                tree.draw(screen, camera_x, camera_y)


class World:
    def __init__(self, width, height):

        self.chunk_size = constants.width # Tamaño de cada chunk (tamaño de la pantalla)
        self.active_chunks = {}  # Chunks activos en el mapa
        self.view_width = width
        self.view_height = height

        grass_path = os.path.join("SupViv", "assets", "objects", "Grass.png")
        self.grass_image = pygame.image.load(grass_path).convert()
        self.grass_image = pygame.transform.scale(self.grass_image,(constants.Grass, constants.Grass))
        self.trees = []
        #Generar chunk inicial adyacentes
        self.generate_chunks(0,0)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                self.generate_chunks(dx,dy)

    def get_chunk_key(self, x, y):

        # Devuelve la clave del chunk basado en las coordenadas x, y
        chunk_x = x // self.chunk_size
        chunk_y = y // self.chunk_size
        return (chunk_x, chunk_y)
    
    def generate_chunks(self, chunk_x, chunk_y):
        key = (chunk_x, chunk_y)
        if key not in self.active_chunks:
            x = chunk_x * self.chunk_size
            y = chunk_y * self.chunk_size
            self.active_chunks[key] = WorldChunk(x, y, self.chunk_size, self.chunk_size)
        
        return self.active_chunks[key]
        # Devuelve los chunks activos en la pantalla basados en la posición de la cámara.

    def update_chunks(self, character_x, character_y):
        #Actualiza los chunks activos en función de la posición del personaje.
        current_chunk = self.get_chunk_key(character_x, character_y)
    # Generar los chunks alrededor del personaje
        for dx in range(-2, 3):  # Rango de -2 a 2 (incluye -2, -1, 0, 1, 2)
            for dy in range(-2, 3):
                chunk_x = current_chunk[0] + dx
                chunk_y = current_chunk[1] + dy
                self.generate_chunks(chunk_x, chunk_y)
    # Eliminar chunks que no están cerca del personaje
        chunk_to_remove = []
        for chunk_key in self.active_chunks:
            distance_x = abs(chunk_key[0] - current_chunk[0])
            distance_y = abs(chunk_key[1] - current_chunk[1])
            if distance_x > 2 or distance_y > 2:
                chunk_to_remove.append(chunk_key)

        for chunk_key in chunk_to_remove:
            del self.active_chunks[chunk_key]

    def draw(self, screen, camera_x, camera_y):
        """
        Dibuja los chunks activos en la pantalla, desplazados por la cámara.
        """
        # Iterar sobre los chunks activos
        for chunk_key, chunk in self.active_chunks.items():
            # Dibujar cada chunk
            chunk.draw(screen, self.grass_image, camera_x, camera_y)


    def get_all_trees(self):  # Renamed method to avoid conflict
        all_trees = []
        for chunk in self.active_chunks.values():
            all_trees.extend(chunk.trees + chunk.trees2)
        return all_trees
        # Return all trees from active chunks 