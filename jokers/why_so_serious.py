# Clase para crear un objeto WhySoSerious

# Importaciones
from jokers import Joker

# Clase WhySoSerious
class WhySoSerious(Joker):
    def __init__(self):
        super().__init__(name="Why so serious?",
                         description="Porque tan serio?",
                         price=9,
                         rarity="Epico",
                         ruta_icon="assets/jokers/whysoserious.jpg",
                         add_multipler=6,
                         points=500)

# Test
if __name__ == "__main__":
    a = WhySoSerious()
    print(a.name)
