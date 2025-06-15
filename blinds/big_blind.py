# Clase para crear un objeto BigBlind

# Importaciones
from blinds import Blind

# Clase BigBlind
class BigBlind(Blind):
    def __init__(self, floor, ronda):
        # Atributos de la clase
        self.floor = floor
        self.round = ronda
        super().__init__(name="Big blind",
                         description="Ciega grande, recompenza grande",
                         floor=self.floor,
                         ronda=self.round,
                         points=self.setter_points(),
                         reward=4)

    # Metodos
    def setter_points(self):
        if self.floor <= 4:
            return 450 * self.floor
        else:
            return 450 * self.floor * self.round
