# Clase para crear un objeto Joker

# Importaciones
from cards import PokerCard

# Clase Joker
class Joker(object):
                      # rareza, probabilidad
    __list_raritys = {"Legendario": 0.05,
                      "Epico": 0.15,
                      "Raro": 0.30,
                      "Comun": 0.50}

    def __init__(self,
                 name,
                 description,
                 price,
                 rarity,
                 ruta_icon,
                 add_multipler = False, # Agregar multiplicador
                 multi_multipler = False, # Multiplica el multiplicador
                 points = False, # Agregar puntos al final de la ronda
                 suit = False, # Aplicar efectos a un palo
                 category = False, # Aplicar efectos a una categoria
                 ):

        # Atributos de clase
        self.__name = None
        self.__description = None
        self.__price = None
        self.__rarity = None
        self.__ruta_icon = None
        self.__add_multipler = None
        self.__multi_multipler = None
        self.__points = None
        self.__suit = None
        self.__category = None

        self.name = name
        self.description = description
        self.price = price
        self.rarity = rarity
        self.ruta_icon = ruta_icon
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

    # price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, int):
            self.__price = price
        else:
            return "El precio tiene que ser un int"

    # rarity
    @property
    def rarity(self):
        return self.__rarity

    @rarity.setter
    def rarity(self, rarity):
        if rarity.capitalize() in self.__list_raritys.keys():
            self.__rarity = rarity
        else:
            return "Rareza no existente"

    # ruta_icon
    @property
    def ruta_icon(self):
        return self.__ruta_icon

    @ruta_icon.setter
    def ruta_icon(self, ruta_icon):
        if isinstance(ruta_icon, str):
            self.__ruta_icon = ruta_icon
        else:
            return "'ruta_icon' tiene que ser un str"

    # add_multipler
    @property
    def add_multipler(self):
        return self.__add_multipler

    @add_multipler.setter
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
            self.__points = points
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
        if not suit: pass
        elif suit.capitalize() in palo:
            self.__suit = suit
        else:
            return f"'suit' tiene que ser una de estas: {palo}"

    # category
    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        palo, categoria = PokerCard.obtener_cartas()
        if not category: pass
        elif isinstance(category, tuple):
            for i in category:
                if i.capitalize in categoria:
                    self.__category = category
        elif category.capitalize() in categoria:
            self.__category = category
        else:
            return f"'category' tiene que ser una de estas: {palo}"

    # Metodos
    # obtener la lista de rarezas
    @classmethod
    def obtener_rarezas(cls):
        return cls.__list_raritys

# Test
if __name__ == "__main__":
    pass
