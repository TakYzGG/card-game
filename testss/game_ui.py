# Prueba de interfaz en pygame

# Importaciones
import pygame, sys
from pygame.locals import *

# Clase Interfaze
class Interfaze(object):
    def __init__(self, game, player):
        # Atributos de clase
        self.w = 600
        self.h = 400
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.game = game
        self.player = player

        # 
        self.lista_botones_cartas = []
        
        # Configuracion de la ventana
        pygame.display.set_caption("Balatro en python")
        
        # Control de FPS
        self.fps = 60
        self.reloj = pygame.time.Clock()

        # Colores
        self.azul = (0, 0, 255)

        # Botones de juego
        self.play_button = pygame.Rect(150, 350, 85, 40)
        self.discart_button = pygame.Rect(420, 350, 85, 40)
        self.order_category_button = pygame.Rect(330, 350, 85, 40)
        self.order_suit_button = pygame.Rect(240, 350, 85, 40)
    
    # Metodos
    # Dibujar las cartas
    def draw_cards(self):
        self.lista_botones_cartas = [] # Limpiar los rectangulos
        x = self.w // 4
        y = self.h / 1.5
        color = (0, 255, 0)
        for carta in self.player.hand:
            rect = pygame.Rect(x, y, 40, 60)

            if carta in self.player.selected_cards: # Pintar cartas seleccionda
                pygame.draw.rect(self.screen, self.azul, rect)
            else: # Pintar cartas no seleccionadas
                pygame.draw.rect(self.screen, color, rect)

            self.lista_botones_cartas.append((rect, carta))
            x += 45

    # Dibujar boton de jugar mano
    def draw_buttons(self):
        pygame.draw.rect(self.screen, (150, 150, 150), self.play_button)
        pygame.draw.rect(self.screen, (255, 0, 255), self.discart_button)
        pygame.draw.rect(self.screen, (0, 155, 155), self.order_category_button)
        pygame.draw.rect(self.screen, (155, 0, 155), self.order_suit_button)

    # Presionar rectangulos
    def press_cards(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for rect, card in self.lista_botones_cartas:
                if rect.collidepoint(pos):
                    self.player.manipulate_card(card)

    # Boton para jugar la mano de cartas
    def play_hand(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if self.play_button.collidepoint(pos):
                self.game.play_hand()

    # Boton para descartar la mano de cartas
    def discart_hand(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if self.discart_button.collidepoint(pos):
                self.game.discart_hand()

    # Boton para ordenar la mano de cartas por categoria
    def order_category(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if self.order_category_button.collidepoint(pos):
                self.player.manipulate_card(None, True)
                self.player.order_category()
                self.player.hand_view()

    # Boton para ordenar la mano de cartas por el palo
    def order_suit(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if self.order_suit_button.collidepoint(pos):
                self.player.manipulate_card(None, True)
                self.player.order_suit()
                print(self.player.hand_view())

    # Actualizar la ventana
    def update_screen(self):
        pygame.display.update()
        self.reloj.tick(self.fps)

    # Bucle principal de la ventana
    def ejecutar(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # Comprobar eventos
                self.press_cards(event)
                self.play_hand(event)
                self.discart_hand(event)
                self.order_category(event)
                self.order_suit(event)

            # Dibujar en la pantalla
            self.draw_cards()
            self.draw_buttons()
            self.update_screen()
