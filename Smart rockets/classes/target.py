import pygame

class Target:
    def __init__(self, position):
        self.position = position

    def x(self):
        return self.position.x

    def y(self):
        return self.position.y

    def changeLocation(x, y):
        self.position.x = x
        self.position.y = y

    def distBetween(self, obj):
        x = (self.position.x - obj.x)**2
        y = (self.position.y - obj.y)**2
        sqr = (x+y)**(1/2)

        return sqr

    def draw(self, where):
        pygame.draw.circle(where, (0, 0, 255), (int(self.position.x), int(self.position.y)), 10, 0)
