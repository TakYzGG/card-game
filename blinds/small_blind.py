# Clase para crear un objeto SmallBlind

# Importaciones
from blinds.blind import Blind

# Clase SmallBlind
class SmallBlind(Blind):
    # Atributos de la clase
    def __init__(self, floor, ronda):
        self.floor = floor
        self.round = ronda
        super().__init__(name="Small blind",
                         description="Ciega pequena, recompenza pequena",
                         floor=self.floor,
                         ronda=self.round,
                         points=self.setter_points(),
                         reward=3)

    # Metodos
    def setter_points(self):
        return 300 * self.floor * self.round

# Test
if __name__ == "__main__":
    a = SmallBlind(1)
    #print(a.name)
