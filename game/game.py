# Clase para crear un objeto Game
# Tiene la ronda y el piso actual, la ciega, etc

# Importaciones
from jokers import *
from blinds import *

# Clase Game
class Game(object):
    def __init__(self, player, poker_hands):

        # Atributos de la clase
        self.__player = player
        self.__player_hands = self.player.hands_play
        self.__player_discarts = self.player.discarts

        self.__poker_hands = poker_hands
        self.__floor = 1
        self.__round = 1

        self.__count = 1
        self.__actual_blind = None
        self.__actual_blind = self.select_blind()

        self.__actual_score = 0 # se tiene que reiniciar despues de cada ronda
        self.__points = 0
        self.__multi = 0

        self.player.add_joker(WhySoSerious())

    # Getters y setters 
    # poker_hands
    @property
    def poker_hands(self):
        return self.__poker_hands

    @poker_hands.setter
    def poker_hands(self, poker_hands):
        if isinstance(poker_hands, PokerHands):
            self.__poker_hands = poker_hands

    # player
    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self.__player = player
        else:
            return f"'player' tiene que ser un objecto de la clase Player"

    # player_hands
    @property
    def player_hands(self):
        return self.__player_hands

    @player_hands.setter
    def player_hands(self, n):
        if isinstance(n, int) and n >= 0:
            self.__player_hands = n

    # player_discarts
    @property
    def player_discarts(self):
        return self.__player_discarts

    @player_discarts.setter
    def player_discarts(self, n):
        if isinstance(n, int) and n >= 0:
            self.__player_discarts = n

    # floor
    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, n):
        if isinstance(n, int) and n > 0:
            self.__floor = n
        else:
            return f"'n' tiene que ser un int mayor a 0"

    # round
    @property
    def round(self):
        return self.__round

    @round.setter
    def round(self, n):
        if isinstance(n, int) and n > 0:
            self.__round = n
        else:
            return f"'n' tiene que ser un int mayor a 0"

    # count
    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, n):
        if isinstance(n, int) and n >= 1:
            self.__count = n

    # actual_blind
    @property
    def actual_blind(self):
        return self.__actual_blind

    @actual_blind.setter
    def actual_blind(self, blind):
        if isinstance(blind, (SmallBlind, BigBlind, BossBlind)):
            self.__actual_blind = blind

    # actual_score
    @property
    def actual_score(self):
        return self.__actual_score

    @actual_score.setter
    def actual_score(self, score):
        if isinstance(score, int) and score >= 0:
            self.__actual_score = score
        else:
            return f"'score' tine que sur un int mayor a 0"

    # points
    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, n):
        if isinstance(n, int) and n >= 0:
            self.__points = n

    # multi
    @property
    def multi(self):
        return self.__multi

    @multi.setter
    def multi(self, n):
        if isinstance(n, int) and n >= 0:
            self.__multi = n

    # Metodos
    # elegir la ciega a enfrentar
    def select_blind(self):
        if self.actual_blind is None or isinstance(self.actual_blind, BossBlind):
            self.actual_blind = SmallBlind(self.floor, self.round)

        elif isinstance(self.actual_blind, SmallBlind):
            self.actual_blind = BigBlind(self.floor, self.round)

        elif isinstance(self.actual_blind, BigBlind):
            self.actual_blind = BossBlind(self.floor, self.round)

        else:
            print("NO FUNCIONA")

        return self.actual_blind

    # obtener la mano de cartas seleccionadas
    def obtain_hand(self):
        return self.poker_hands.play_poker_hand(self.player)

    # sumar la puntuacion de las cartas
    def add_score(self, cartas, puntos, retorno=False):
        self.points, self.multi = puntos

        # retornar los puntos y el multi en caso de necesitarse
        if retorno:
            return self.points, self.multi

        if len(self.player.jokers) > 0:
            for joker in self.player.jokers:
                self.points += joker.points
                self.multi += joker.add_multipler
        # sumar los puntos de todas las cartas jugadas
        for carta in cartas:
            self.points += carta.points

        self.actual_score += self.points * self.multi

    # verificar si hay que pasar de ronda/piso
    def pass_round_floor(self):
        # Pasar de ronda/piso
        if self.actual_score >= self.actual_blind.points:
            self.round += 1 # sumar +1 a la ronda
            self.actual_score = 0 # settear los puntos a 0
            self.player.money += self.actual_blind.reward + self.player_hands # sumar el dinero al jgdr
            self.player_hands = self.player.hands_play # restablecer las manos
            self.player_discarts = self.player.discarts # restablecer los dscts
            self.player.copy_deck = self.player.deck # copiar el mazo original
            self.player.hand = self.player.generate_hand() # restablecer la mano

            if isinstance(self.actual_blind, BossBlind):
                self.floor += 1

            self.select_blind() # elegir una nueva ciega

            return True

    # jugar las cartas seleccionadas
    def play_hand(self):
        if self.player_hands > 0 and len(self.player.selected_cards) > 0:
            mano_jugada, cartas, puntos = self.poker_hands.play_poker_hand(self.player)

            self.player_hands -= 1 # restar -1 mano al jugador

            self.add_score(cartas, puntos) # sumar puntos

            self.player.add_hand_cards() # agregar cartas faltantes a la mano
            self.player.remove_selected_cards() # remover las cartas seleccionadas
            self.pass_round_floor()
            return mano_jugada

    # descartar las cartas seleccionadas
    def discart_hand(self):
        if self.player_discarts > 0 and len(self.player.selected_cards) > 0:
            self.player_discarts -= 1 # restar -1 a los descartes
            self.player.add_hand_cards() # agregar cartas faltantes a la mano
            self.player.remove_selected_cards() # remover las cartas seleccionadas
            return True

    # atajos para test
    def agregar_puntos(self):
        self.actual_score = 999999

# Test
if __name__ == "__main__":
    a = Game()
    print(a.actual_blind.name)
    a.select_blind()
    print(a.actual_blind.name)
