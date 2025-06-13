# Este archivo contiene todas las manos de poker que se pueden jugar

# Importaciones
from cards.poker import PokerCard
from collections import defaultdict

# Clase PokerHands
class PokerHands(object):
    def __init__(self):
        pass

    # Metodos
    # jugar la mano actual
    def play_poker_hand(self, player):
        if player.selected_cards:
            manos = (self.color, self.two_pair, self.parejas, self.highcard)
            for mano in manos:
                resultado = mano(*player.selected_cards)
                if resultado:
                    return resultado
        else:
            return " ", " ", ("0", "0")

    # mano: highcard
    def highcard(self, *args):
        if len(args) > 0:
           return "Highcard", [max(args, key=lambda x: x.points)], (5, 1)

    # mano: pair, three of kind, four of kind
    def parejas(self, *args):
        for carta in args:
            cartas = [x for x in args if x.category == carta.category]

            if len(cartas) == 2:
                return "Pair", tuple(cartas), (10, 2)

            elif len(cartas) == 3:
                return "Three of kind", tuple(cartas), (30, 3)

            elif len(cartas) == 4:
                return "Four of kind", tuple(cartas), (60, 7)

    # mano: two pair
    def two_pair(self, *args):

        if len(args) >= 4:
            # Contar cuántas cartas hay por categoría
            por_categoria = defaultdict(list)
            for carta in args:
                por_categoria[carta.category].append(carta)
        
            # Buscar categorías con exactamente dos cartas (pares)
            pares = [cartas for cartas in por_categoria.values() if len(cartas) == 2]
        
            if len(pares) >= 2:
                par1, par2 = pares
                # Si hay al menos dos pares, devolver resultado
                return "Two pair", tuple(par1 + par2), (20, 4)

    # mano: color
    def color(self, *args):
        for carta in args:
            cartas = [x for x in args if x.suit == carta.suit]
            if len(cartas) == 5:
                return "Color", tuple(cartas), (35, 4)

# Test
if __name__ == "__main__":
    carta1 = PokerCard("diamantes", "as")
    carta2 = PokerCard("treboles", "8")
    carta3 = PokerCard("picas", "5")
    carta4 = PokerCard("corazones", "8")
    carta5 = PokerCard("diamantes", "8")
    hands = PokerHands()
    cartas = [carta1, carta2, carta3, carta4, carta5]
    print("AAA")
