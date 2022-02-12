from constants import *

class Laser:
    def __init__(self, spos, sangle, sr):
        self.pos = spos.copy().rotate(sr, sangle)
        self.vel = Vector(0, 0).rotate(1, sangle)
        self.vel.mult(10)

    def update(self):
        self.pos.add(self.vel)

    def hits(self, asteroid):
         d = self.pos.dist(asteroid.pos)

         return d < asteroid.r
