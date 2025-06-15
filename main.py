# Archivo princial del proyecto y desde donde se ejecuta el mismo

# Importaciones
from player import Player
from cards.poker import PokerHands
from game import Game
from interface import MainMenu, Interface

# aa
jugador = Player()
manos_poker = PokerHands()
game = Game(jugador, manos_poker)
interfaz = Interface()
interfaz.ejecutar(MainMenu, (game, jugador))
