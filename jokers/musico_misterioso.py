# Clase para crear un objeto MusicoMisterioso

# Importaciones
from jokers import Joker

# Clase MusicoMisterioso
class MusicoMisterioso(Joker):
    def __init__(self):
        super().__init__(name="Musico Misterioso",
                         description="No le preguntes por su musica",
                         price=6,
                         rarity="Raro",
                         ruta_icon="assets/jokers/musico_misterioso",
                         # Falta agregar una mano al jugador
                         points=100)
