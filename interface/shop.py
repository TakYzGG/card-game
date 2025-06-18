# Clase para crear la interfaz de latienda

# Importaciones
import pygame, sys
from pygame.locals import *
from interface import Scene

# Clase ShopScene
class ShopScene(Scene):
    def __init__(self, date=None):
        super().__init__()
        _, self.player, self.shop = date
        self.w, self.h = self.get_wh()
        self.bg = pygame.image.load("assets/main_menu/bg.jpg").convert()
        self.bg_scale = pygame.transform.scale(self.bg, (self.w, self.h))
        self.lista_botones_jokers = []

    # Metodos
    # crear botones para los jokers
    def jokers_buttons(self, screen):
        self.lista_botones_jokers = []
        x = 100
        y = 100
        for joker in self.shop.items["jokers"]:
            rect = pygame.Rect(x, y, 40, 60)
            icon = pygame.image.load(joker.ruta_icon)
            icon_scale = pygame.transform.scale(icon, (40, 60))

            pygame.draw.rect(screen, self.amarillo, rect)
            screen.blit(icon_scale, rect.topleft)

            self.lista_botones_jokers.append((rect, joker))
            x += 45

    # manejar eventos
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN: pass
            # Rescalar fondo
            elif event.type == pygame.VIDEORESIZE:
                self.bg_scale = pygame.transform.scale(self.bg, event.size)
                self.w, self.h = event.size

    # dibujar en la pantalla
    def draw(self, screen):
        screen.blit(self.bg_scale, (0, 0))
        self.jokers_buttons(screen)
