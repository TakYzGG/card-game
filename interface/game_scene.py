# Clase para la interfaz del juego

# Importaciones
import pygame, sys
from pygame.locals import *
from interface import Scene
import interface

# Clase GameScene
class GameScene(Scene):
    def __init__(self, data=None):
        super().__init__()

        self.game, self.player, _ = data
        self.actual_blind = self.game.actual_blind

        self.w, self.h = self.get_wh()

        # Listas para almacenar (rect, obj)
        self.lista_botones_cartas = []
        self.lista_botones_jokers = []

        self.bg = pygame.image.load("assets/bg.png")
        self.bg_scale = pygame.transform.scale(self.bg, (self.w, self.h))

    # Metodos
    # actualizar la informacion de la partida
    def update_info(self):

        self.blind_name = self.font.render(f"{self.game.actual_blind.name}",
                                           True, self.blanco)

        self.blind_points = self.font.render(f"{self.game.actual_blind.points}",
                                             True, self.blanco)

        self.blind_reward = self.font.render(f"${self.game.actual_blind.reward}",
                                             True, self.amarillo)

        self.actual_score = self.font.render(f"{self.game.actual_score}",
                                             True, self.blanco)

        self.hand_poker = self.font.render(f"{self.game.obtain_hand()[0]}",
                                           True, self.blanco)

        self.poker_hand_points = self.font.render(f"{self.game.obtain_hand()[2][0]}",
                                                  True, self.azul)

        self.poker_hand_multi = self.font.render(f"{self.game.obtain_hand()[2][1]}",
                                                 True, self.rojo)

        self.hands_play = self.font.render(f"Manos: {self.game.player_hands}",
                                           True, self.blanco)

        self.discarts = self.font.render(f"Descartes: {self.game.player_discarts}",
                                         True, self.blanco)

        self.money = self.font.render(f"${self.player.money}", True, self.amarillo)

        self.floor = self.font.render(f"Piso: {self.game.floor}", True, self.blanco)

        self.round = self.font.render(f"Ronda: {self.game.round}", True, self.blanco)

    # Dubujar un marco para la informacion de la partida
    def draw_frame(self, screen):
        pygame.draw.rect(screen, self.negro, ((self.w * 1.1) // 100, 
                                                   (self.h * 2) // 100,
                                                   (self.w * 30) // 100,
                                                   self.h - 2 * ((self.h * 2) // 100)))

    # Dibujar la informacion de la partida
    def draw_info(self, screen):
        # FIXMI: hacer que se acomode el texto en el marco
        screen.blit(self.blind_name, (20, 20))
        screen.blit(self.blind_points, (20, 40))
        screen.blit(self.blind_reward, (20, 60))
        screen.blit(self.actual_score, (20, 80))
        screen.blit(self.hand_poker, (20, 100))
        screen.blit(self.poker_hand_points, (20, 120))
        screen.blit(self.poker_hand_multi, (40, 120))
        screen.blit(self.hands_play, (20, 140))
        screen.blit(self.discarts, (20, 160))
        screen.blit(self.money, (20, 180))
        screen.blit(self.floor, (20, 200))
        screen.blit(self.round, (20, 220))

    # Dibujar las cartas
    def draw_cards(self, screen):
        self.lista_botones_cartas = [] # Limpiar los rectangulos
        x = self.w // 2.8 
        y = self.h // 1.4
        color = (0, 255, 0)
        for carta in self.player.hand:
            rect = pygame.Rect(x, y, 40, 60)

            if carta in self.player.selected_cards: # Pintar cartas seleccionda
                pygame.draw.rect(screen, self.azul, rect)
            else: # Pintar cartas no seleccionadas
                pygame.draw.rect(screen, color, rect)

            suit = self.font.render(f"{carta.suit}", True, self.negro)

            category = self.font.render(f"{carta.category}", True, self.negro)

            screen.blit(suit, (x, y))
            screen.blit(category, (x, y+12))

            self.lista_botones_cartas.append((rect, carta))
            x += 45

    # Dibujal la descripcion de las cartas
    def draw_card_description(self, screen, pos):
        for rect, card in self.lista_botones_cartas:
            if rect.collidepoint(pos):
                pygame.draw.rect(screen, self.rojo, (305, 220, 175, 60))

    # Dibujar los jokers
    def draw_jokers(self, screen):
        self.lista_botones_jokers = [] # Limpiar lista
        x = 215 
        y = 10
        color = (0, 255, 0)
        for joker in self.player.jokers:
            rect = pygame.Rect(x, y, 40, 60)
            icon = pygame.image.load(joker.ruta_icon)

            pygame.draw.rect(screen, self.amarillo, rect)
            screen.blit(icon, rect.topleft)

            self.lista_botones_jokers.append((rect, joker))
            x += 45

    # Dibujal la descripcion de las cartas
    def draw_joker_description(self, screen, pos):
        for rect, joker in self.lista_botones_jokers:
            if rect.collidepoint(pos):
                pygame.draw.rect(screen, self.rojo, (305, 80, 175, 60))
                description = self.font.render(f"Descripcion: {joker.description}",
                                               True, self.negro)
                screen.blit(description, (305, 80))

    # Dibujar boton de jugar mano
    def draw_buttons(self, screen):
        w = self.w // 2.8
        h = self.h // 1.14

        self.play_button = pygame.Rect(w, h, 85, 40)
        self.discart_button = pygame.Rect(w + 270, h, 85, 40)
        self.order_category_button = pygame.Rect(w + 90, h, 85, 40)
        self.order_suit_button = pygame.Rect(w + 180, h, 85, 40)

        pygame.draw.rect(screen, self.azul, self.play_button)
        pygame.draw.rect(screen, self.rojo, self.discart_button)
        pygame.draw.rect(screen, self.amarillo, self.order_category_button)
        pygame.draw.rect(screen, self.amarillo, self.order_suit_button)

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

    # verificar si cambio la ciega
    def change_blind(self):
        if self.actual_blind != self.game.actual_blind:
            self.next_scene = interface.ShopScene

    # manejar eventos
    def handle_events(self, events):
        for event in events:
            # Comprobar eventos
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                self.press_cards(pos)
                self.play_hand(pos)
                self.discart_hand(pos)
                self.order_category(pos)
                self.order_suit(pos)

            # Rescalar fondo
            elif event.type == pygame.VIDEORESIZE:
                self.bg_scale = pygame.transform.scale(self.bg, event.size)
                self.w, self.h = event.size

            # Comprobar si cambio la ciega actual
            self.change_blind()

    # dibujar en la pantalla
    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        screen.blit(self.bg_scale, (0, 0))
        self.update_info()
        self.draw_frame(screen)
        self.draw_info(screen)
        self.draw_cards(screen)
        self.draw_jokers(screen)
        self.draw_buttons(screen)
        self.draw_card_description(screen, pos)
        self.draw_joker_description(screen, pos)
