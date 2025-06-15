# Clase para crear un objeto Blind 

# Importaciones
from abc import ABC, abstractmethod

# Clase Blind
class Blind(ABC):
    def __init__(self, name, description, floor, ronda, points, reward):
        # Atributos de la clase
        self.__name = None
        self.__description = None
        self.__floor = None
        self.__round = None
        self.__points = None
        self.__reward = None

        self.name = name
        self.description = description
        self.floor = floor
        self.ronda = ronda
        self.points = points
        self.reward = reward

    # Getters y setters
    # name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    # description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self.__description = description

    # floor
    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, floor):
        if isinstance(floor, int) and floor > 0:
            self.__floor = floor

    # ronda
    @property
    def round(self):
        return self.__round

    @round.setter
    def round(self, ronda):
        if isinstance(ronda, int) and ronda > 0:
            self.__round = ronda

    # points
    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        if isinstance(points, int) and points > 0:
            self.__points = points

    # reward
    @property
    def reward(self):
        return self.__reward

    @reward.setter
    def reward(self, reward):
        if isinstance(reward, int) and reward > 0:
            self.__reward = reward

    # Metodos
    # settear los puntos de la ciega dependiendo el piso actual
    @abstractmethod
    def setter_points(self):
        pass
