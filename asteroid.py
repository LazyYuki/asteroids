from constants import *

class Asteroid:
    def __init__(self):
        self.pos = Vector(randint(0, WIDTH), randint(0, HEIGHT))
        self.vel = Vector(0, 0).random(-3, 3)
        self.r = randint(15, 75)
        self.total = randint(5, 15)
        self.offset = []

        self.calcOffset()

        ## # DEBUG:
        self.debugRad = False

    def calcOffset(self):
        self.offset = []
        for i in range(self.total):
            self.offset.append(uniform(-self.r*0.5, self.r*0.5) + self.r)

    def update(self):
        self.pos.add(self.vel)

    def edges(self):
        if self.pos.x > WIDTH + self.r:
            self.pos.x = -self.r
        elif self.pos.x < -self.r:
            self.pos.x = WIDTH + self.r

        if self.pos.y > HEIGHT + self.r:
            self.pos.y = -self.r
        elif self.pos.y < -self.r:
            self.pos.y = HEIGHT + self.r
