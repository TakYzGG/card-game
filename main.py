# Archivo princial del proyecto y desde donde se ejecuta el mismo

# Importaciones
from player import Player
from cards.poker import PokerHands
from game import Game
from testss.game_ui import Interfaze

# aa
jugador = Player()
manos_poker = PokerHands()
game = Game(jugador, manos_poker)
juego = Interfaze(game, jugador)
juego.ejecutar()
