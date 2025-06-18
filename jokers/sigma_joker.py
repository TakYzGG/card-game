# Clase para crear un objecto SigmaJoker

# Importaciones
from jokers import Joker

# Clase SigmaJoker
class SigmaJoker(Joker):
    def __init__(self):
        super().__init__(name="SigmaJoker",
                         description="Cuando se juega un rey agrega +10 a la puntuacion",
                         price=3,
                         rarity="Comun",
                         ruta_icon="assets/jokers/sigma_joker",
                         points=10,
                         category="King")
