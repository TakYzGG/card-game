# Clase para crear un objeto PokerCard

# Clase PokerCard
class PokerCard(object):
    # Atributos de clase
    __list_suit = ("Picas", "Corazones", "Treboles", "Diamantes")
    __list_category = ("As", "King", "Queen", "Joker", "10", "9",
                        "8", "7", "6", "5", "4", "3", "2")

    # inicializador de la clase
    def __init__(self, suit, category):
        
        # Atributos de clase
        self.__suit = None
        self.__category = None
        self.__points = None

        self.suit = suit
        self.category = category

    # Getters y setters
    # suit
    @property
    def suit(self):
        return self.__suit

    @suit.setter
    def suit(self, suit):
        if suit.capitalize() in self.__list_suit:
            self.__suit = suit.capitalize()
        else:
            return f"'suit' tiene que ser una de estas: {self.list_suit}"

    # category
    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        if category.capitalize() in self.__list_category:
            self.__category = category.capitalize()

            # Establecer los puntos a la carta
            if category.capitalize() == "As":
                self.points = 11
            elif category.capitalize() in ("King", "Queen", "Joker"):
                self.points = 10
            else:
                self.points = int(category)
        else:
            return f"'category' tiene que ser una de estas: {self.list_category}"

    # Metodos
    # obtener suit y category desde otra clase sin declarar un objecto
    @classmethod
    def obtener_cartas(cls):
        return cls.__list_suit, cls.__list_category

# Test
if __name__ == "__main__":
    a = PokerCard("PICAS", "KING")
    print(PokerCard.obtener_cartas())
