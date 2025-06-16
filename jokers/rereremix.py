# Clase para crear un objeto ReReRemix

# Importaciones
from jokers import Joker

# Clase ReReRemix
class ReReRemix(Joker):
    def __init__(self):
        super().__init__(name="ReReRemix",
                         description="Repite toda la mano jugada 1 veces",
                         price=9,
                         rarity="Epico",
                         ruta_icon="assets/jokers/rereremix",
                         # Falta logica para repetir la mano jugada
                        )
