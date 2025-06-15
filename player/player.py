# Clase para crear un objecto Player

# Importaciones
from cards.poker import PokerCard
from random import choice
from collections import defaultdict
from copy import deepcopy

# Clase Player
class Player(object):
    def __init__(self):

        # Atributos de clase
        self.__deck = self.generate_deck()
        self.__copy_deck = deepcopy(self.deck)

        self.__hand_size = 8

        self.__hand = self.generate_hand()

        self.__hands_play = 4
        self.__discarts = 3

        self.__selected_cards = []

        self.__jokers = []

        self.__money = 4 # money siempre va a ser un int

    # Getters y setters
    # deck
    @property
    def deck(self):
        return self.__deck

    # copy_deck
    @property
    def copy_deck(self):
        return self.__copy_deck

    @copy_deck.setter
    def copy_deck(self, deck):
        if deck == self.deck:
            self.__copy_deck = deepcopy(self.deck)
        else:
            return f"etqm"

    # hand
    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self, cartas):
        if isinstance(cartas, list):
            self.__hand = cartas

    # hand_size
    @property
    def hand_size(self):
        return self.__hand_size

    @hand_size.setter
    def hand_size(self, size):
        if isinstance(size, int) and size > 0:
            self.__hand_size = size
        else:
            return f"'size' tiene que ser un int mayor a 0"
    
    # hands_play
    @property
    def hands_play(self):
        return self.__hands_play

    @hands_play.setter
    def hands_play(self, n):
        if isinstance(n, int) and n >= 0:
            self.__hands_play = n
        else:
            return f"'n' tiene que ser un int mayor a 0"

    # discarts
    @property
    def discarts(self):
        return self.__discarts
    
    @discarts.setter
    def discarts(self, n):
        if isinstance(n, int) and n >= 0:
            self.__discarts = n
        else:
            return f"'n' tiene que ser un int mayor a 0"

    # selected_cards
    @property
    def selected_cards(self):
        return self.__selected_cards

    # jokers
    @property
    def jokers(self):
        return self.__jokers

    # money
    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        if isinstance(money, int) and money >= 0:
            self.__money = money
        else:
            return f"'money' tiene que ser un int pero es: {type(money)}"

    # Metodos
    # generar el mazo de cardas
    def generate_deck(self):
        suit, category = PokerCard.obtener_cartas()
        deck = {x:[PokerCard(x, y) for y in category] for x in suit}
        self.__deck = deck
        return self.__deck

    # agregra cardas al mazo
    def add_card(self, card):
        if isinstance(card, PokerCard):
            self.__deck[card.suit].append(card)
        else:
            return f"'card' tiene que ser de la clase PokerCard"

    # eliminar cardas del mazo
    def remove_card(self, card):
        if isinstance(card, PokerCard):
            self.__deck.remove(card)
        else:
            return f"'card' tiene que ser de la clase PokerCard"

    # mostrar el mazo de cardas
    def deck_view(self):
        deck = {x:[y.category for y in self.deck[x]] for x in self.deck.keys()}
        return deck

    # generar la mano de cartas
    def generate_hand(self):
        self.__hand = []
        current_cards = [(x,y) for x in self.copy_deck.keys() for y in self.copy_deck[x]]
        for _ in range(self.hand_size):
            card = choice(current_cards)
            self.__hand.append(card[1])
            current_cards.remove(card)
            self.copy_deck[card[0]].remove(card[1])
        self.order_suit()
        return self.__hand

    # eliminar cartas seleccionadas de la mano
    def remove_selected_cards(self):
        for carta in self.selected_cards:
            self.hand.remove(carta)
        self.__selected_cards = []

    # agregar cartas nuevas a la mano
    def add_hand_cards(self):
        self.__hand = self.hand
        current_cards = [(x,y) for x in self.copy_deck.keys() for y in self.copy_deck[x]]
        for _ in range(len(self.selected_cards)):
            card = choice(current_cards)
            self.__hand.append(card[1])
            current_cards.remove(card)
            self.copy_deck[card[0]].remove(card[1])
        return self.__hand

    # mostrar la mano de cardas
    def hand_view(self):
        hand = [(x.suit, x.category) for x in self.hand]
        return hand

    # seleccionar cardas
    def select_card(self, card):
        if card not in self.selected_cards:
            if len(self.selected_cards) < 5:
                self.selected_cards.append(card)
                return True

    # deseleccionar cardas
    def deselect_card(self, card):
        if card in self.selected_cards:
            self.selected_cards.remove(card)
            return True

    # manipular cartas
    def manipulate_card(self, card, clear=False):
        if clear:
            self.selected_cards.clear()
        elif self.select_card(card): pass
        elif self.deselect_card(card): pass

    # ordenar la mano de cartas por la categoria
    def order_category(self):
        self.hand_view()
        self.hand = sorted(self.hand, key=lambda x: x.points, reverse=True)

    # ordenar la mano de cartas por el palo
    def order_suit(self):
        self.hand_view()
        self.order_category()

        cartas = defaultdict(list)
        for carta in self.hand:
            cartas[carta.suit].append(carta)

        self.hand = [y for x in cartas.values() for y in x]

    # agregar un joker nuevo
    # FIXMI: no puede funcionar porque no tiene todas las clases de jokers
    def add_joker(self, joker):
        self.__jokers.append(joker)
        #if isinstance(joker, joker):
        #    pass
        #else:
        #    return f"'joker' tiene que ser un Joker pero es: {type(joker)}"

    # eliminar un joker
    def remove_joker(self, joker):
        if joker in self.jokers:
            self.__jokers.remove(joker)
        else:
            return f"'joker' no esta en los jokers del jugador"

# Test
if __name__ == "__main__":
    jugador1 = Player()
    print(jugador1.deck)
    print(id(jugador1.deck))
    print(id(jugador1.copy_deck))
    jugador1.deck["Picas"].pop()
    print(len(jugador1.deck["Picas"]))
    print(len(jugador1.copy_deck["Picas"]))
