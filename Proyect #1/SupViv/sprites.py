import os
from PIL import Image
import pygame

def pil_image_to_pygame_surface(pil_image):
    """
    Convierte una imagen de Pillow (PIL.Image) a una superficie de Pygame (pygame.Surface).
    """
    mode = pil_image.mode
    size = pil_image.size
    data = pil_image.tobytes()
    pygame_surface = pygame.image.fromstring(data, size, mode)
    return pygame_surface

def load_sprites_from_folder(folder_path):
    """
    Carga todos los frames individuales de las subcarpetas dentro de 'Walk'.
    """
    sprites = {}
    for direction_folder in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, direction_folder)):
            direction = direction_folder.replace("frames_Walk_", "").lower()
            sprites[direction] = []
            direction_path = os.path.join(folder_path, direction_folder)
            for file_name in sorted(os.listdir(direction_path)):
                if file_name.startswith("frame_") and file_name.endswith(".png"):
                    sprite_path = os.path.join(direction_path, file_name)
                    pil_image = Image.open(sprite_path).convert("RGBA")
                    pygame_surface = pil_image_to_pygame_surface(pil_image)
                    sprites[direction].append(pygame_surface)
                    print(f"Cargando sprites para la dirección: {direction}")  # Depuración
            if not sprites[direction]:
                print(f"Advertencia: No se encontraron sprites en la carpeta '{direction_folder}'.")
    return sprites