# Escena base para crear todas las otras

# Importaciones
import pygame, sys
from pygame.locals import *
from abc import ABC, abstractmethod

# Clase Scene
class Scene(ABC):
    def __init__(self):
        self.next_scene = self

        # Colores
        self.negro = (40, 40, 40)
        self.blanco = (235, 219, 178)
        self.rojo = (204, 36, 29)
        self.verde = (152, 151, 26)
        self.azul = (69, 133, 136)
        self.amarillo = (215, 153, 33)

        # Fuente
        self.font = pygame.font.SysFont("Ubuntu Mono", 16, "bold")

    # Metodos
    # manejar eventos
    @abstractmethod
    def handle_events(self):
        pass

    # dibujar en la pantalla
    @abstractmethod
    def draw(self, screen):
        pass

    # get width_height
    def get_wh(self):
        info = pygame.display.Info()
        return info.current_w, info.current_h
    
    # cambiar a la siguiente escena
    def get_next_scene(self):
        return self.next_scene
