# Prueba de interfaz en pygame

# Importaciones
import pygame, sys
from pygame.locals import *

# Clase Interfaze
class Interfaze(object):
    def __init__(self, game, player):
        # Inicializar pygame
        pygame.init()

        # Atributos de clase
        self.w = 600
        self.h = 400
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.game = game
        self.player = player

        # Listas para almacenar (rect, obj)
        self.lista_botones_cartas = []
        self.lista_botones_jokers = []

        # Configuracion de la ventana
        pygame.display.set_caption("Balatro en python")
        self.background = pygame.image.load("assets/bg.jpg").convert()
        
        # Control de FPS
        self.fps = 60
        self.reloj = pygame.time.Clock()

        # Colores
        self.negro = (40, 40, 40)
        self.rojo = (204, 36, 29)
        self.verde = (152, 151, 26)
        self.azul = (69, 133, 136)
        self.amarillo = (215, 153, 33)

        # Fuente
        self.font = pygame.font.SysFont("Ubuntu Mono", 16, "bold")

        # Informacion de la partida

        # Botones de juego
        self.play_button = pygame.Rect(215, 350, 85, 40)
        self.discart_button = pygame.Rect(485, 350, 85, 40)
        self.order_category_button = pygame.Rect(395, 350, 85, 40)
        self.order_suit_button = pygame.Rect(305, 350, 85, 40)
    
    # Metodos
    # Actualizar la informacion de la pantalla
    def update_info(self):

        self.blind_name = self.font.render(f"{self.game.actual_blind.name}",
                                           True, self.negro)

        self.blind_points = self.font.render(f"{self.game.actual_blind.points}",
                                             True, self.negro)

        self.blind_reward = self.font.render(f"${self.game.actual_blind.reward}",
                                             True, self.amarillo)

        self.actual_score = self.font.render(f"{self.game.actual_score}",
                                             True, self.negro)

        # FIXMI: mostrar solo el nombre de la mano seleccionada
        self.hand_poker = self.font.render(f"{self.game.obtain_hand()[0]}",
                                           True, self.negro)

        self.poker_hand_points = self.font.render(f"{self.game.obtain_hand()[2][0]}",
                                                  True, self.azul)

        self.poker_hand_multi = self.font.render(f"{self.game.obtain_hand()[2][1]}",
                                                 True, self.rojo)

        self.hands_play = self.font.render(f"Manos: {self.game.player_hands}",
                                           True, self.negro)

        self.discarts = self.font.render(f"Descartes: {self.game.player_discarts}",
                                         True, self.negro)

        self.money = self.font.render(f"${self.player.money}", True, self.amarillo)

        self.floor = self.font.render(f"Piso: {self.game.floor}", True, self.negro)

        self.round = self.font.render(f"Ronda: {self.game.round}", True, self.negro)

    # Dubujar un marco para la informacion de la partida
    def draw_frame(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (10, 10, 180, 380))

    # Dibujar la informacion de la partida
    def draw_info(self):
        self.screen.blit(self.blind_name, (20, 20))
        self.screen.blit(self.blind_points, (20, 40))
        self.screen.blit(self.blind_reward, (20, 60))
        self.screen.blit(self.actual_score, (20, 80))
        self.screen.blit(self.hand_poker, (20, 100))
        self.screen.blit(self.poker_hand_points, (20, 120))
        self.screen.blit(self.poker_hand_multi, (40, 120))
        self.screen.blit(self.hands_play, (20, 140))
        self.screen.blit(self.discarts, (20, 160))
        self.screen.blit(self.money, (20, 180))
        self.screen.blit(self.floor, (20, 200))
        self.screen.blit(self.round, (20, 220))

    # Dibujar las cartas
    def draw_cards(self):
        self.lista_botones_cartas = [] # Limpiar los rectangulos
        x = 215 
        y = 285
        color = (0, 255, 0)
        for carta in self.player.hand:
            rect = pygame.Rect(x, y, 40, 60)

            if carta in self.player.selected_cards: # Pintar cartas seleccionda
                pygame.draw.rect(self.screen, self.azul, rect)
            else: # Pintar cartas no seleccionadas
                pygame.draw.rect(self.screen, color, rect)

            suit = self.font.render(f"{carta.suit}", True, self.negro)

            category = self.font.render(f"{carta.category}", True, self.negro)

            self.screen.blit(suit, (x, y))
            self.screen.blit(category, (x, y+12))

            self.lista_botones_cartas.append((rect, carta))
            x += 45

    # Dibujal la descripcion de las cartas
    def draw_card_description(self, pos):
        for rect, card in self.lista_botones_cartas:
            if rect.collidepoint(pos):
                pygame.draw.rect(self.screen, self.rojo, (305, 220, 175, 60))

    # Dibujar los jokers
    def draw_jokers(self):
        self.lista_botones_jokers = [] # Limpiar lista
        x = 215 
        y = 10
        color = (0, 255, 0)
        for joker in self.player.jokers:
            rect = pygame.Rect(x, y, 40, 60)
            icon = pygame.image.load(joker.ruta_icon)

            pygame.draw.rect(self.screen, self.amarillo, rect)
            self.screen.blit(icon, rect.topleft)

            self.lista_botones_jokers.append((rect, joker))
            x += 45

    # Dibujal la descripcion de las cartas
    def draw_joker_description(self, pos):
        for rect, joker in self.lista_botones_jokers:
            if rect.collidepoint(pos):
                pygame.draw.rect(self.screen, self.rojo, (305, 80, 175, 60))
                description = self.font.render(f"Descripcion: {joker.description}",
                                               True, self.negro)
                self.screen.blit(description, (305, 80))

    # Dibujar boton de jugar mano
    def draw_buttons(self):
        pygame.draw.rect(self.screen, self.azul, self.play_button)
        pygame.draw.rect(self.screen, self.rojo, self.discart_button)
        pygame.draw.rect(self.screen, self.amarillo, self.order_category_button)
        pygame.draw.rect(self.screen, self.amarillo, self.order_suit_button)

    # Presionar rectangulos
    def press_cards(self, pos):
        for rect, card in self.lista_botones_cartas:
            if rect.collidepoint(pos):
                self.player.manipulate_card(card)

    # Boton para jugar la mano de cartas
    def play_hand(self, pos):
        if self.play_button.collidepoint(pos):
            self.game.play_hand()

    # Boton para descartar la mano de cartas
    def discart_hand(self, pos):
        if self.discart_button.collidepoint(pos):
            self.game.discart_hand()

    # Boton para ordenar la mano de cartas por categoria
    def order_category(self, pos):
        if self.order_category_button.collidepoint(pos):
            self.player.manipulate_card(None, True)
            self.player.order_category()

    # Boton para ordenar la mano de cartas por el palo
    def order_suit(self, pos):
        if self.order_suit_button.collidepoint(pos):
            self.player.manipulate_card(None, True)
            self.player.order_suit()

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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    self.press_cards(pos)
                    self.play_hand(pos)
                    self.discart_hand(pos)
                    self.order_category(pos)
                    self.order_suit(pos)

            # Actualizar la info de la partida
            self.update_info()
            
            # Obtener coords del cursor
            pos = pygame.mouse.get_pos()

            # Dibujar en la pantalla
            self.screen.blit(self.background, (0, 0))
            self.draw_frame()
            self.draw_info()
            self.draw_cards()
            self.draw_jokers()
            self.draw_buttons()
            self.draw_card_description(pos)
            self.draw_joker_description(pos)
            self.update_screen()
