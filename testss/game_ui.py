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

        # Inicializar pygame
        pygame.init()

        # 
        self.lista_botones_cartas = []
        
        # Configuracion de la ventana
        pygame.display.set_caption("Balatro en python")
        
        # Control de FPS
        self.fps = 60
        self.reloj = pygame.time.Clock()

        # Colores
        self.azul = (0, 0, 255)

        # Fuente
        self.font = pygame.font.SysFont("Ubuntu Mono", 16)

        # Informacion de la partida

        # Botones de juego
        self.play_button = pygame.Rect(150, 350, 85, 40)
        self.discart_button = pygame.Rect(420, 350, 85, 40)
        self.order_category_button = pygame.Rect(330, 350, 85, 40)
        self.order_suit_button = pygame.Rect(240, 350, 85, 40)
    
    # Metodos
    # Actualizar la informacion de la pantalla
    def update_info(self):

        self.blind_name = self.font.render(f"{self.game.actual_blind.name}",
                                           True, self.azul)

        self.blind_points = self.font.render(f"{self.game.actual_blind.points}",
                                             True, self.azul)

        self.blind_reward = self.font.render(f"{self.game.actual_blind.reward}",
                                             True, self.azul)

        self.actual_score = self.font.render(f"{self.game.actual_score}",
                                             True, self.azul)

        # FIXMI: mostrar solo el nombre de la mano seleccionada
        self.hand_poker = self.font.render(f"{self.game.obtain_hand()}", True, self.azul)

        self.poker_hand_points = self.font.render("0", True, self.azul)

        self.poker_hand_multi = self.font.render("0",True, self.azul)

        self.hands_play = self.font.render(f"Manos: {self.game.player_hands}",
                                           True, self.azul)

        self.discarts = self.font.render(f"Descartes: {self.game.player_discarts}",
                                         True, self.azul)

        self.money = self.font.render(f"{self.player.money}", True, self.azul)

        self.floor = self.font.render(f"Piso: {self.game.floor}", True, self.azul)

        self.round = self.font.render(f"Ronda: {self.game.round}", True, self.azul)

    # Dibujar la informacion de la partida
    def draw_info(self):
        self.screen.blit(self.blind_name, (0, 0))
        self.screen.blit(self.blind_points, (0, 20))
        self.screen.blit(self.blind_reward, (0, 40))
        self.screen.blit(self.actual_score, (0, 60))
        self.screen.blit(self.hand_poker, (0, 80))
        self.screen.blit(self.poker_hand_points, (0, 100))
        self.screen.blit(self.poker_hand_multi, (20, 100))
        self.screen.blit(self.hands_play, (0, 120))
        self.screen.blit(self.discarts, (0, 140))
        self.screen.blit(self.money, (0, 160))
        self.screen.blit(self.floor, (0, 180))
        self.screen.blit(self.round, (0, 200))

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

            suit = self.font.render(f"{carta.suit}", True, (0, 0, 0))

            category = self.font.render(f"{carta.category}", True, (0, 0, 0))

            self.screen.blit(suit, (x, y))
            self.screen.blit(category, (x, y+12))

            self.lista_botones_cartas.append((rect, carta))
            x += 45

    # Dibujar boton de jugar mano
    def draw_buttons(self):
        pygame.draw.rect(self.screen, (150, 150, 150), self.play_button)
        pygame.draw.rect(self.screen, (255, 0, 255), self.discart_button)
        pygame.draw.rect(self.screen, (0, 155, 155), self.order_category_button)
        pygame.draw.rect(self.screen, (155, 0, 155), self.order_suit_button)

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
            self.player.hand_view()

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

            # Dibujar en la pantalla
            self.screen.fill((0,0,0))  # o el color de fondo que uses
            self.update_info()
            self.draw_info()
            self.draw_cards()
            self.draw_buttons()
            self.update_screen()
