from constants import *

class Ship():
    def __init__(self):
        self.pos = Vector(WIDTH/2, HEIGHT/2)
        self.r = 30
        self.angle = 0
        self.rotation = 0
        self.vel = Vector(0, 0)
        self.isBoosting = False;

        ## Beauty:
        self.strokeWidth = 10   #no width in pyg zero??????? wtf
        self.color = WHITE

        ## DEBUG:
        self.debugRot = False

    def update(self):
        if self.isBoosting:
            self.boost()

        self.pos.add(self.vel)
        self.vel.mult(0.99)

    def boost(self):
        force = Vector(0,0).rotate(1, self.angle)
        force.mult(0.15)
        self.vel.add(force)

    def turn(self):
        self.angle += self.rotation

        #for memory overload
        if self.angle > 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360

    def setRotation(self, a):
        self.rotation = a

    def boosting(self, b):
        self.isBoosting = b

    def edges(self):
        if self.pos.x > WIDTH + self.r:
            self.pos.x = -self.r
        elif self.pos.x < -self.r:
            self.pos.x = WIDTH + self.r

        if self.pos.y > HEIGHT + self.r:
            self.pos.y = -self.r
        elif self.pos.y < -self.r:
            self.pos.y = HEIGHT + self.r

    def hits(self, asteroid):
         d = self.pos.dist(asteroid.pos)

         return d < asteroid.r+self.r
