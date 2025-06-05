# Este archivo contiene la interfaz para el juego
# ronda, cartas, ciega, dinero, etc

# Importaciones
import tkinter as tk

# Clase GameUi
class GameUi(object):
    def __init__(self, root, game, player):

        # Atributos de clase
        self.root = root
        self.game = game
        self.player = player
        self.lista_botones = []

        # fuente y colores
        self.font = ("Ubuntu Mono", 12, "bold")
        self.violeta = "#8414b8"
        self.celeste = "#14b8b8"
        self.rojo = "#d1001c"
        self.amarillo = "#ffaa1d"
        
        # Config de la ventana
        self.root.resizable(0,0)
        self.root.config(bg="#6C757D")

        # frames para dividir la pantalla
        self.info = tk.Frame(self.root, bg=self.violeta, bd=2)
        self.info.grid(row=0, column=0, sticky="w")

        self.jokers = tk.Frame(self.root, bg="Red", bd=2)
        self.jokers.grid(row=0, column=1, sticky="n")

        self.hand = tk.Frame(self.root, bg="Yellow", bd=2)
        self.hand.grid(row=0, column=1, sticky="s")

        self.hand_buttons = tk.Frame(self.root, bg="Black", bd=2)
        self.hand_buttons.grid(row=1, column=1, sticky="n")

        # ------ INFO DE LA PARTIDA ------
        # mostrar la ciega actual
        self.blind_name =tk.Label(self.info,
                                  text=f"{self.game.obtener_ciega()[0]}",
                                  font=self.font,
                                  bg=self.violeta)

        self.blind_name.grid(row=0, column=0, columnspan=2)

        # puntos para ganar
        self.blind_points = tk.Label(self.info,
                                     text=f"{self.game.obtener_ciega()[1]}",
                                     font=self.font,
                                     bg=self.violeta)

        self.blind_points.grid(row=1, column=0, columnspan=2)

        # recompensa por ganar
        self.blind_reward = tk.Label(self.info,
                                     text=f"{self.game.obtener_ciega()[2]}",
                                     font=self.font,
                                     bg=self.violeta)

        self.blind_reward.grid(row=2, column=0, columnspan=2)

        # mostrar los puntos actuales
        self.actual_score = tk.Label(self.info,
                                     text=f"Puntos: {self.game.actual_score}",
                                     font=self.font,
                                     bg=self.violeta)

        self.actual_score.grid(row=3, column=0, columnspan=2)

        # mostrar la mano de poker seleccionada (ejemplo: color)
        self.hand_poker = tk.Label(self.info, text="",
                                   font=self.font,
                                   bg=self.violeta)

        self.hand_poker.grid(row=4, column=0, columnspan=2)

        # mostrar puntos | multi de la mano de poker
        self.poker_hand_points = tk.Label(self.info,
                                          text="0",
                                          font=self.font,
                                          bg=self.celeste,
                                          width=7)

        self.poker_hand_points.grid(row=5, column=0)

        self.poker_hand_multi = tk.Label(self.info,
                                         text="0",
                                         font=self.font,
                                         bg=self.rojo,
                                         width=7)

        self.poker_hand_multi.grid(row=5, column=1)

        # mostrar las manos por jugar restantes
        self.hands_play = tk.Label(self.info,
                                   text=f"Manos: {self.game.player_hands}",
                                   font=self.font,
                                   bg=self.violeta)

        self.hands_play.grid(row=6, column=0)

        # mostrar los descartes restantes
        self.discarts = tk.Label(self.info,
                                 text=f"Descartes: {self.game.player_discarts}",
                                 font=self.font,
                                 bg=self.violeta)

        self.discarts.grid(row=6, column=1)

        # mostrar el dinero actual del jugador
        self.money = tk.Label(self.info,
                              text=f"${self.player.money}",
                              font=self.font,
                              bg=self.violeta,
                              fg=self.amarillo)

        self.money.grid(row=7, column=0, columnspan=2)

        # mostrar el piso actual
        self.floor = tk.Label(self.info,
                              text=f"Piso: {self.game.floor}",
                              font=self.font,
                              bg=self.violeta)
        self.floor.grid(row=8, column=0)

        # mostrar la ronda actual
        self.round = tk.Label(self.info,
                              text=f"Ronda: {self.game.round}",
                              font=self.font,
                              bg=self.violeta)

        self.round.grid(row=8, column=1)

        # ------ JOKERS ------
        # Test
        tk.Label(self.jokers, text="joker1, joker2, joker3, joker4, joker5").pack()

        # -- BOTONES --
        # boton para jugar la mano actual
        self.jugar_btn = tk.Button(self.hand_buttons, text="Jugar",
                                   font=self.font,
                                   bg=self.celeste,
                                   command=self.play_hand)
        self.jugar_btn.grid(row=1, column=0)

        # boton para descartar la mano actual
        self.descartar_btn = tk.Button(self.hand_buttons, text="Descartar",
                                       font=self.font,
                                       bg=self.rojo,
                                       command=self.discart_hand)
        self.descartar_btn.grid(row=1, column=3)

        # boton para ordenar las cartas por categoria
        self.categoria_btn = tk.Button(self.hand_buttons, text="Categoria",
                                       font=self.font,
                                       bg=self.amarillo,
                                       command=self.order_category)
        self.categoria_btn.grid(row=1, column=1)

        # boton para ordenar las cartas por palo
        self.palo_btn = tk.Button(self.hand_buttons, text="Palo",
                                  font=self.font,
                                  bg=self.amarillo,
                                  command=self.order_suit)
        self.palo_btn.grid(row=1, column=2)

        # ------ MANO DE CARTAS ------
        # mostrar la mano de cartas
        self.hand_view()

    # Metodos
    # mostrar las cartas de la mano
    def hand_view(self):
        self.destruct_buttons()
        for x, card in enumerate(self.player.hand):
            btn = tk.Button(self.hand,
                            bg="Green",
                            text=f"{card.suit}\n{card.category}")
            btn.config(command=lambda b=btn, c=card: self.select_card(b, c))
            btn.grid(row=0, column=x)
            self.lista_botones.append(btn)

    # seleccionar una carta
    def select_card(self, btn, card):
        if self.player.select_card(card):
            btn.config(bg="Pink",
                       command=lambda b=btn, c=card: self.deselect_card(b, c))

            # mostrar la mano de poker actual
            mano, cartas, puntos_mano = self.game.obtain_hand()
            self.hand_poker.config(text=mano)

            # mostrar los puntos y el multi de la mano de poker actual
            puntos, multi = self.game.add_score(cartas, puntos_mano, True)
            self.poker_hand_points.config(text=f"{puntos}")
            self.poker_hand_multi.config(text=multi)

    # deseleccionar una carta
    def deselect_card(self, btn, card):
        if self.player.deselect_card(card):
            btn.config(bg="Green",
                       command=lambda b=btn, c=card: self.select_card(b, c))

            if len(self.player.selected_cards) == 0:
                self.hand_poker.config(text="")
                self.poker_hand_points.config(text="0")
                self.poker_hand_multi.config(text="0")

            else:
                # mostrar la mano de poker actual
                mano, cartas, puntos_mano = self.game.obtain_hand()
                self.hand_poker.config(text=mano)

                # mostcac los puntos de la mano de poker actual
                puntos, multi = self.game.add_score(cartas, puntos_mano, True)
                self.poker_hand_points.config(text=f"{puntos}")
                self.poker_hand_multi.config(text=multi)

    # jugar la mano de cartas
    def play_hand(self):
        if self.game.play_hand():
            self.actual_score.config(text=f"Puntos: {self.game.actual_score}")
            self.hands_play.config(text=f"Manos: {self.game.player_hands}")
            self.hand_poker.config(text="")
            self.poker_hand_points.config(text="0")
            self.poker_hand_multi.config(text="0")
            self.discarts.config(text=f"Descartes: {self.game.player_discarts}")

            if self.game.pass_round_floor():
                self.blind_name.config(text=f"{self.game.obtener_ciega()[0]}")
                self.blind_points.config(text=f"{self.game.obtener_ciega()[1]}")
                self.blind_reward.config(text=f"{self.game.obtener_ciega()[2]}")
                self.actual_score.config(text=f"Puntos: {self.game.actual_score}")
                self.hands_play.config(text=f"Manos: {self.game.player_hands}")
                self.discarts.config(text=f"Descartes: {self.game.player_discarts}")
                self.money.config(text=f"${self.player.money}")
                self.round.config(text=f"{self.game.round}")
                self.floor.config(text=f"{self.game.floor}")

            self.hand_view()
        else:
            self.root.destroy()

    # descartar la mano de cartas
    def discart_hand(self):
        if self.game.discart_hand():
            self.discarts.config(text=f"Descartes: {self.game.player_discarts}")
            self.hand_view()

    # ordenar la mano de cartas por categoria
    def order_category(self):
        self.player.deselect_card(None, True)
        self.destruct_buttons()
        self.player.order_category()
        self.hand_view()

    # ordenar la mano de cartas por palo
    def order_suit(self):
        self.player.deselect_card(None, True)
        self.destruct_buttons()
        self.player.order_suit()
        self.hand_view()

    # destruir botones
    def destruct_buttons(self):
        for boton in self.lista_botones:
            boton.destroy()

    # ejecutar la ventana principal
    def execute(self):
        self.root.mainloop()

# Test
if __name__ == "__main__":
    screen = tk.Tk()
    a = Game(screen)
    a.execute()
