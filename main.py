import pgzrun, math, time, ship, asteroid, laser
from constants import *

#render muss hier sein weil pygame zero schlecht ist ;(

class Laser(laser.Laser):
    def render(self):
        screen.draw.circle(self.pos.toList(), 1, WHITE)

class Asteroid(asteroid.Asteroid):
    def render(self):
        if self.debugRad:
            screen.draw.circle(self.pos.toList(), self.r, RED)
        s = shape()
        for i in range(self.total):
            angle = 360/self.total * i
            s.addVertex(self.pos.rotate(self.offset[i], angle))
        s.render()


    def breakTo(self, amount):
        newA = []

        for i in range(amount):
            a = Asteroid()

            a.pos = self.pos.copy()
            a.r = self.r/amount

            a.calcOffset()

            newA.append(a)

        return newA

class Ship(ship.Ship):
    def render(self):
        #triangle
        p1 = self.pos.rotate(self.r, self.angle).toList()
        p2 = self.pos.rotate(self.r, self.angle+135).toList()
        p3 = self.pos.rotate(self.r, self.angle-135).toList()

        if self.debugRot:
            screen.draw.circle(p1, 5, RED)
            screen.draw.circle(p2, 5, GREEN)
            screen.draw.circle(p3, 5, BLUE)

            screen.draw.circle(self.pos.toList(), 5, WHITE)

            screen.draw.circle(self.pos.toList(), self.r, WHITE)

        screen.draw.line(p1, p2, self.color)
        screen.draw.line(p2, p3, self.color)
        screen.draw.line(p3, p1, self.color)

class shape():
    def __init__(self):
        self.vertexes = []

    def addVertex(self, vec: Vector):
        self.vertexes.append(vec)

    def render(self):
        if len(self.vertexes) > 0:
            start = self.vertexes[0].toList()

            for i in range(1, len(self.vertexes)):
                end = self.vertexes[i].toList()
                screen.draw.line(start, end, WHITE)
                start = end

            screen.draw.line(start, self.vertexes[0].toList(), WHITE)

ship = None
asteroids = []
lasers = []

dead = False
score = 0

def setup():
    global ship, asteroids

    ship = Ship()

    asteroids = []
    for i in range(10):
        asteroids.append(Asteroid())

    lasers = []

def Death():
    global dead
    dead = False

    #setup()

def draw():
    screen.fill(BLACK)
    ship.render()

    for a in asteroids:
        a.render()

    for l in lasers:
        l.render()

    screen.draw.text(f"Score: {score}", (0,0), color=GREEN, fontsize=30)

    if dead:
        screen.draw.text(f"YOU DIED", (0, 0), color=RED, fontsize=100, centerx = WIDTH/2, centery = HEIGHT/2)

def update():
    global asteroids, lasers, ship, score, dead

    #ship
    ship.update()
    ship.edges()
    ship.turn()

    #astroids
    for a in asteroids:
        a.update()
        a.edges()

    #lasers
    for lI in range(len(lasers)-1, -1, -1):
        lasers[lI].update()

        for aI in range(len(asteroids)-1, -1, -1):
            if lasers[lI].hits(asteroids[aI]):
                if asteroids[aI].r > 15:
                    newAsteroids = asteroids[aI].breakTo(3)
                    asteroids += newAsteroids
                else:
                    score += 1

                asteroids.pop(aI)
                lasers.pop(lI)
                break

    #die
    for a in asteroids:
        if ship.hits(a):
            score = 0
            dead = True
            clock.schedule(Death, 1.0)

    time.sleep(1/60)

def on_key_down(key):
    if key == keys.SPACE:
        lasers.append(Laser(ship.pos, ship.angle, ship.r))
    elif key == keys.RIGHT:
        ship.setRotation(6)
    elif key == keys.LEFT:
        ship.setRotation(-6)
    elif key == key.UP:
        ship.boosting(True)

def on_key_up(key):
    if key == keys.RIGHT or key == key.LEFT:
        ship.setRotation(0)
    if key == key.UP:
        ship.boosting(False)

setup()
pgzrun.go()
