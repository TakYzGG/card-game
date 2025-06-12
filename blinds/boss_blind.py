# Clase para crear un objeto BossBlind

# Importaciones
from blinds import Blind
from random import choice

# Clase BossBlind
class BossBlind(Blind):
    # Atributos de clase
    # Nombre, (descripcion, puntos base)
    __bosses = {"Boss 1": ("Test del boss", 800),
                "Boss 2": ("Test del boss", 900)} 

    def __init__(self, floor, ronda):
        # Atributos de la clase
        self.floor = floor
        self.round = ronda
        self.boss = self.setter_boss()
        super().__init__(name=self.boss,
                         description=self.obtener_bosses()[self.boss][0],
                         floor=self.floor,
                         ronda=self.round,
                         points=self.setter_points(),
                         reward=5)

    # Metodos
    # retornar todos los bosses
    @classmethod
    def obtener_bosses(cls):
        return cls.__bosses

    # elegir el boss
    def setter_boss(self):
        boss = choice(list(self.obtener_bosses().keys()))
        return boss

    def setter_points(self):
        if self.floor <= 4:
            return self.obtener_bosses()[self.boss][1] * self.floor
        else:
            return self.obtener_bosses()[self.boss][1] * self.floor * self.round

# Test
if __name__ == "__main__":
    boss = BossBlind(1, 1)
    print(boss.boss)
    print(boss.name)
    print(boss.points)
