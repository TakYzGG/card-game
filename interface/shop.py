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
        self.lista_botones = []
        self.buy = False
        self.buy_button = pygame.Rect(0,0,0,0)

    # Metodos
    # crear botones para los jokers
    def jokers_buttons(self, screen):
        self.lista_botones = []
        x_size = (self.w * 7) // 100
        y_size = (self.h * 15) // 100
        x = (self.w * 80) // 100
        y = (self.h * 50) // 100
        for joker in self.shop.items["jokers"]:
            rect = pygame.Rect(x, y, x_size, y_size)
            icon = pygame.image.load(joker.ruta_icon)
            icon_scale = pygame.transform.scale(icon, (x_size, y_size))

            pygame.draw.rect(screen, self.amarillo, rect)
            screen.blit(icon_scale, rect.topleft)

            self.lista_botones.append((rect, joker))
            x += x_size + 5

    # dibujar boton para comprar
    def draw_buy_button(self, screen):
        if self.buy:
            self.buy_button = pygame.Rect(50, 50, 60, 60)
            pygame.draw.rect(screen, self.rojo, self.buy_button)

    # Boton para activar_desactivar el boton de comprar
    def activate_buy_button(self, pos):
        for rect, obj in self.lista_botones:
            if rect.collidepoint(pos):
                self.item = obj
                if self.buy:
                    self.buy = False
                else:
                    self.buy = True

    # Funcion para le boton de compra
    def use_buy_button(self, pos):
        if self.buy_button.collidepoint(pos):
            self.shop.buy_joker(self.item)

    # manejar eventos
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.activate_buy_button(pos)
                self.use_buy_button(pos)
            # Rescalar fondo
            elif event.type == pygame.VIDEORESIZE:
                self.bg_scale = pygame.transform.scale(self.bg, event.size)
                self.w, self.h = event.size

    # dibujar en la pantalla
    def draw(self, screen):
        screen.blit(self.bg_scale, (0, 0))
        self.jokers_buttons(screen)
        self.draw_buy_button(screen)
