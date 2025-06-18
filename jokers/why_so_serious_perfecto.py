# Clase para crear un objeto WhySoSeriousPerfecto

# Importaciones
from jokers import Joker

# Clase WhySoSerious
class WhySoSeriousPerfecto(Joker):
    def __init__(self):
        super().__init__(name="Why So Serious? (Perfecto)",
                         description="Porque tan serio? (ahora perfeccionado)",
                         price=12,
                         rarity="Legendario",
                         ruta_icon="assets/jokers/why_so_serious_perfecto.png",
                         add_multipler=6,
                         multi_multipler=20,
                         points=100000)

