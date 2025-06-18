# Archivo princial del proyecto y desde donde se ejecuta el mismo

# Importaciones
from player import Player
from cards import PokerHands
from game import Game
from interface import MainMenu, Interface
from shop import Shop

# aa
jugador = Player()
manos_poker = PokerHands()
game = Game(jugador, manos_poker)
shop = Shop(jugador)
interfaz = Interface()
interfaz.ejecutar(MainMenu, (game, jugador, shop))
