# Clase para crear un objeto SmallBlind

# Importaciones
from blinds import Blind

# Clase SmallBlind
class SmallBlind(Blind):
    def __init__(self, floor, ronda):
        # Atributos de la clase
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
        if self.floor <= 4:
            return 300 * self.floor
        else:
            return 300 * self.floor * self.round

# Test
if __name__ == "__main__":
    a = SmallBlind(1)
    #print(a.name)
