import pygame
import constants
import os
from camera import *


#Arboles del mundo



class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wood = 5
        self.inventory = {"wood": 5}
        tree_path = os.path.join("SupViv", "assets", "objects", "Tree.png")
        self.image = pygame.image.load(tree_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constants.Tree, constants.Tree))
        self.size = self.image.get_width()
        self.mask = pygame.mask.from_surface(self.image)


    def get_mask(self):
        # Devuelve la máscara del objeto
        return self.mask
    def check_collision(self, obj):
    # Calcula el desplazamiento entre el jugador y el objeto
        offset_x = int(obj.x - self.x)
        offset_y = int(obj.y - self.y)
    def draw(self, screen, camera_x, camera_y):
        # Calcular posicion en pantalla relativa a la camara
        screen_x = self.x - camera_x
        screen_y = self.y - camera_y
        # Solo dibujamos si esta en la pantalla
        if (screen_x + self.size >= 0 and screen_x <= constants.width and
                screen_y + self.size >= 0 and screen_y <= constants.height):
            screen.blit(self.image,(screen_x, screen_y))


class Tree2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wood = 5
        self.inventory = {"wood": 5}
        tree_path = os.path.join("SupViv", "assets", "objects", "Tree2.png")
        self.image = pygame.image.load(tree_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constants.Tree2, constants.Tree2))
        self.size = self.image.get_width()  # Tamaño original
        self.mask = pygame.mask.from_surface(self.image)
    
    def get_mask(self):
        # Devuelve la máscara del objeto
        return self.mask
    def check_collision(self, obj):
    # Calcula el desplazamiento entre el jugador y el objeto
        offset_x = int(obj.x - self.x)
        offset_y = int(obj.y - self.y)
    def draw(self, screen, camera_x, camera_y):
        # Calcular posicion en pantalla relativa a la camara
        screen_x = self.x - camera_x
        screen_y = self.y - camera_y
        # Solo dibujamos si esta en la pantalla
        if (screen_x + self.size >= 0 and screen_x <= constants.width and
                screen_y + self.size >= 0 and screen_y <= constants.height):
            screen.blit(self.image,(screen_x, screen_y))
        
        
#Piedras del mundo
class Stones:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.stone = 5
        self.inventory = {"stone": 6}
        
    def draw(self, screen):
        pygame.draw.rect(screen, constants.gray, (self.x, self.y, self.size, self.size))

class Meet:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.size = 10
        self.meat = 5
        self.inventory = {"meat": 5}

    def draw(self, screen):
        pygame.draw.rect(screen, constants.red, (self.x, self.y, self.size, self.size))

class Smoll_Stone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.stone = 1
        self.inventory = {"stone": 1}

    def draw(self, screen):
        pygame.draw.rect(screen, constants.gray, (self.x, self.y, self.size, self.size))