# Archivo princial del proyecto y desde donde se ejecuta el mismo

# Importaciones
import tkinter as tk
from player.player import Player
from cards.poker.poker_hands import PokerHands
from game.game import Game
from interface.game_ui import GameUi

# aa
jugador = Player()
manos_poker = PokerHands()
game = Game(jugador, manos_poker)
screen = tk.Tk()
game_ui = GameUi(screen, game, jugador)
game_ui.execute()
