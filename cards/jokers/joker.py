# Clase para crear un objeto Joker

# Importaciones
from cards.poker.poker import PokerCard

# Clase Joker
class Joker(object):
    def __init__(self, name, description,
                 add_multipler = False, # Agregar multiplicador
                 multi_multipler = False, # Multiplica el multiplicador
                 points = False, # Agregar puntos al final de la ronda
                 suit = False, # Aplicar efectos a un palo
                 category = False, # Aplicar efectos a una categoria
                 ):

        # Atributos de clase
        self.__name = None
        self.__description = None
        self.__add_multipler = None
        self.__multi_multipler = None
        self.__points = None
        self.__suit = None
        self.__category = None

        self.name = name
        self.description = description
        self.add_multipler = add_multipler
        self.multi_multipler = multi_multipler
        self.points = points
        self.suit = suit
        self.category = category

    # Getters y setters
    # name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            return "'name' tiene que ser un str"

    # description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self.__description = description
        else:
            return "'description' tiene que ser un str"

    # add_multipler
    @property
    def add_multipler(self):
        return self.__add_multipler

    @add_multipler
    def add_multipler(self, multi):
        if isinstance(multi, (int, float)):
            self.__add_multipler = multi
        elif isinstance(multi, False):
            pass
        else:
            return "'multi' tiene que ser un int/float"

    # multi_multipler
    @property
    def multi_multipler(self):
        return self.__multi_multipler

    @multi_multipler.setter
    def multi_multipler(self, multi):
        if isinstance(multi, (int, float)):
            self.__multi_multipler = multi
        elif isinstance(multi, False):
            pass
        else:
            return "'multi' tiene que ser un int/float"

    # points
    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        if isinstance(points, (int, float)):
            self.__points = pointns
        elif isinstance(points, False):
            pass
        else:
            return "'points' tiene que ser un int/float"


    # suit
    @property
    def suit(self):
        return self.__suit

    @suit.setter
    def suit(self, suit):
        palo, categoria = PokerCard.obtener_cartas()
        if suit.capitalize() in palo:
            self.__suit = suit
        elif isinstance(suit, False):
            pass
        else:
            return f"'suit' tiene que ser una de estas: {palo}"

    # category
    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        palo, categoria = PokerCard.obtener_cartas()
        if category.capitalize() in categoria:
            self.__category = category
        elif isinstance(category, False):
            pass
        else:
            return f"'category' tiene que ser una de estas: {palo}"

# Test
if __name__ == "__main__":
    pass
