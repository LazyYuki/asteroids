import pgzrun, math, time
from random import randint, uniform

TITLE = "ASTROIDS IN PG ZERO"

WIDTH = 800
HEIGHT = 800

WHITE =     (255, 255, 255)
BLACK =     (000, 000, 000)
RED =       (255, 000, 000)
GREEN =     (000, 255, 000)
BLUE =      (000, 000, 255)

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

    def mult(self, value):
        self.x *= value
        self.y *= value

    def toList(self):
        return [self.x, self.y]

    def random(self, min, max):
        self.x = randint(min, max)
        self.y = randint(min, max)

        return self

    def copy(self):
        return Vector(self.x, self.y)

    def dist(self, vec):
        a = self.x - vec.x
        b = self.y - vec.y

        return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

    def rotate(self, radius: int, angle: int):
        angle -= 90
        if angle < 0:
            angle += 360

        rad = angle * (math.pi / 180)

        x = self.x + math.cos(rad) * radius
        y = self.y + math.sin(rad) * radius

        return Vector(x,y)
