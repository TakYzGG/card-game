# Clase para crear el menu del juego

# Importaciones
import pygame, sys
from pygame.locals import *
from interface import Scene, GameScene

# Clase MainMenu
class MainMenu(Scene):
    def __init__(self, data=None):
        super().__init__()
        self.w, self.h = self.get_wh()
        self.bg = pygame.image.load("assets/main_menu/bg.jpg").convert()
        self.bg_scale = pygame.transform.scale(self.bg, (self.w, self.h))
        self.play_button = None

    # Metodos
    # boton para jugar
    def play_button_draw(self, screen):
        x_size = (self.w * 20) // 100
        y_size = (self.h * 10) // 100
        x = self.w // 2 - (x_size // 2)
        y = self.h - 2 * ((self.h * 10) // 100)
        rect = pygame.Rect(x, y, x_size, y_size)
        pygame.draw.rect(screen, self.azul, rect)
        self.play_button = rect

    def play_button_press(self, pos):
        if self.play_button.collidepoint(pos):
            self.next_scene = GameScene

    # manejar evetos
    def handle_events(self, events):
        for event in events:
            # Comprobar eventos
            # Precionar boton del mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # click izquierdo
                    pos = event.pos
                    self.play_button_press(pos)
            # Rescalar fondo
            if event.type == pygame.VIDEORESIZE:
                self.bg_scale = pygame.transform.scale(self.bg, event.size)
                self.w, self.h = event.size

    # dibujar en la pantalla
    def draw(self, screen):
        screen.blit(self.bg_scale, (0, 0))
        self.play_button_draw(screen)
