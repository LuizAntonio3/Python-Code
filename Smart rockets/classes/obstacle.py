from pygame.math import Vector2
import pygame

class Obstacle:
    def __init__(self, firstPoint, secondPoint):
        self.firstPoint = firstPoint
        self.secondPoint = secondPoint
        self.width = 0
        self.height = 0
        self.calcSizes()
    
    def draw(self, screen):
        obs = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        obs.fill((255, 255, 255))

        points = (self.firstPoint.x, self.firstPoint.y, self.width, self.height)
        rectObs = pygame.Rect(points)
        screen.blit(obs, rectObs)
    
    def calcSizes(self):
        self.width = abs(self.secondPoint.x - self.firstPoint.x)
        self.height = abs(self.secondPoint.y - self.firstPoint.y)
        
