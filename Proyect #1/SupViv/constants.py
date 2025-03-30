import pygame

# Description: Constants for the game
# Tamaño de la pantalla
width = 800
height = 600
# Tamaño del Personaje y objetos
Personaje = 20
Grass = 64
Tree = 64
Tree2 = 64
Stone = 32
Meat = 16

# Colores para la barra de estado

Energy_color = (255, 255, 0)
Food_color =  (255, 165, 0)
Thirst_color = (0, 191, 255)
Bar_Backgrownd = (100, 100, 100)

# Intervalo de tiempo

Status_update_interval = 1000

#sistema dia/noche
Day_length = 2400000
Dawn_time = 600000
Morning_time = 800000
Dusk_time = 1800000
Mindnight = 2400000
Max_darknes = 210

# Colores para la iluminacion
Nigth_color = (20, 20, 50)  #Color azul para la noche
day_color = (255, 255, 255) # Color blanco para el dia
Dawn_dusk_color = (255, 193, 137) # Color anaranjado para el amanecer/atardecer

# Velocidades de disminucion de estados
Fod_decrease_rate = 0.01
Thirst_decrease_rate = 0.02
Energy_decrease_rate = 0.005
Energy_increase_rate = 0.001
Movement_energy_cost = 0.001

#Colores
white = (255, 255, 255) #Blanco
black = (0, 0, 0) #Negro
red = (255, 0, 0) #Rojo
green = (0, 255, 0) #Verde
blue = (0, 0, 255)  #Azul
yellow = (255, 255, 0) #Amarillo
cyan = (0, 255, 255) #Cyan
magenta = (255, 0, 255) #Magenta
orange = (255, 165, 0) #Naranja
purple = (128, 0, 128)
gray = (128, 128, 128)
lightgray = (200, 200, 200)
darkgray = (100, 100, 100)
brown = (139, 69, 19)
lightblue = (173, 216, 230)
lightgreen = (144, 238, 144)
lightyellow = (255, 255, 224)
lightred = (255, 160, 122)
lightorange = (255, 218, 185)
lightpurple = (221, 160, 221)
lightcyan = (224, 255, 255)
lightmagenta = (255, 224, 255)
