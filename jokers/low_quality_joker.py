# Clase para crear un objeto LowQualityJoker

# Importaciones
from jokers import Joker

# Clase
class LowQualityJoker(Joker):
    def __init__(self):
        super().__init__(name="Low Quality Joker",
                         description="Si juegas un 1, 2, 3 o 4 puntua 2 veces",
                         price=6,
                         rarity="Raro",
                         ruta_icon="assets/jokers/low_quality_joker", # falta extencion
                         category=("1" ,"2" ,"3", "4"))
# Todavia no funciona, falta programar la logica para repetir la mano jugada
