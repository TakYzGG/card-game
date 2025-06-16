# Clase para crear la tienda

# Importaciones
from jokers import get_jokers
from random import choice

# Clase Shop
class Shop(object):
    def __init__(self, player):
        self.__player = player
        self.__jokers = None
        self.__slots = None
        self.__items = None

        self.jokers = get_jokers()
        self.__slots = 2
        self.items = {"jokers": [],
                      #"cards": [],
                      #"vales": []
                      }

        self.select_items()

    # Getters y setters
    # player
    @property
    def player(self):
        return self.__player

    @player.setter
    def player(player, player):
        if isinstance(player, Player):
            self.__player = player
        else:
            return "player tiene que ser un objeto Player"

    # jokers
    @property
    def jokers(self):
        return self.__jokers

    @jokers.setter
    def jokers(self, jokers):
        if isinstance(jokers, tuple):
            self.jokers = jokers

    # slots
    @property
    def slots(self):
        return self.__slots

    @slots.setter
    def slots(self, n):
        if isinstance(n, int):
            self.__slots = 2

    # items
    @property
    def items(self):
        return self.__items

    # Metodos
    def select_items(self):
        for _ in range(self.slots):
            joker = choice(self.jokers)
            self.__items["jokers"].append(joker)

    def buy_items(self, item):
        if self.player.money >= item.price:
            pass
