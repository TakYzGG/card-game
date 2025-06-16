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
    def player(self, player):
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
            self.__jokers = jokers

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

    @items.setter
    def items(self, dicc):
        if isinstance(dicc, dict):
            self.__items = dicc

    # Metodos
    # Elegir los jokers de la tienda aleatoriamente
    def select_jokers(self):
        for _ in range(self.slots):
            joker = choice(self.jokers)
            self.__items["jokers"].append(joker)

    # Comprar un joker de la tienda
    def buy_joker(self, joker):
        if self.player.money >= joker.price:
            self.player.jokers.append(joker)
            self.player.money -= joker.price
            self.items["jokers"].remove(joker)

# Test
if __name__ == "__main__":
    a = Shop("test")
    print(a.items)
