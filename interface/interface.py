# Archivo para ejecutar la interfaz

# Importaciones
import pygame, sys
from pygame.locals import *

# Clase Interface
class Interface(object):
    def __init__(self):
        # Inicializar pygame
        pygame.init()

        self.info = pygame.display.Info()
        self.w = self.info.current_w
        self.h = self.info.current_h
        self.screen = pygame.display.set_mode((self.w, self.h), pygame.RESIZABLE)

        # Control de FPS
        self.fps = 60
        self.reloj = pygame.time.Clock()

    def ejecutar(self, escena, data):
        escena_actual = escena(data)
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if escena_actual.get_next_scene() != escena_actual:
                    escena_actual = escena_actual.get_next_scene()(data)

            escena_actual.handle_events(events)
            escena_actual.draw(self.screen)

            pygame.display.update()
            self.reloj.tick(self.fps)
