import pygame
from pygame.math import Vector2
import random
import numpy as np
from classes.dna import Dna

class Rocket:
    def __init__(self, screen, life, target, d=None):
        self.screen = screen
        self.life = life
        self.lifeCount = 0
        self.fitness = 0
        self.mult = 1

        self.position = Vector2(screen.get_width()/2, screen.get_height() - 40)
        self.velocity = Vector2(0, 0)
        self.acelaration = Vector2(0, 0)
        #self.maxVel = 1

        self.length = 8
        self.height = 14
        self.color = (255, 255, 255)

        self.crashed = False
        self.completed = False
        self.lastTarget = target

        if d == None:
            self.dna = Dna(life)
        else:
            self.dna = d
    
    def draw(self):
        length = self.length/2
        height = self.height/2
        
        body = pygame.Surface((self.length, self.height), pygame.SRCALPHA)
        body.fill(self.color)
        
        points = (self.position.x - length, self.position.y - height, length * 2, height * 2)
        bodyRect = pygame.Rect(points)
        angle = self.velocity.angle_to(Vector2(1, 0))
        body = pygame.transform.rotate(body, angle + 90)

        self.screen.blit(body, bodyRect)
    
    def update(self, obstacles):
        self.isCrashedOrCompleted(obstacles)
        
        if not self.crashed and self.lifeCount < self.life and not self.completed:
            self.addForce(self.dna.genotype[self.lifeCount])
            self.velocity += self.acelaration
            self.position += self.velocity
            self.acelaration *= 0
            self.lifeCount += 1

        self.draw()
    
    def addForce(self, force):
        self.acelaration += force

    def calcFitness(self, target):
        self.lastTarget = target
        dist = target.distBetween(self.position) + 0.01
        score = 1.0/dist
        self.fitness = score * self.mult

    def isCrashedOrCompleted(self, obstacles):
        if self.position.x <= 0 or self.position.x >= self.screen.get_width():
            self.crashed = True
            self.color = (255, 0, 0)
            self.mult = 0.01
        
        if self.position.y <= 0 or self.position.y >= self.screen.get_height():
            self.crashed = True
            self.color = (255, 0, 0)
            self.mult = 0.01

        for i in range(len(obstacles)):
            if self.position.x >= obstacles[i].firstPoint.x and self.position.x <= obstacles[i].secondPoint.x and self.position.y >= obstacles[i].firstPoint.y and self.position.y <= obstacles[i].secondPoint.y:
                self.crashed = True
                self.color = (255, 0, 0)
                self.mult = 0.01
        
        if self.position.x >= self.lastTarget.x()-10 and self.position.x <= self.lastTarget.x()+10 and self.position.y >= self.lastTarget.y()-10 and self.position.y <= self.lastTarget.y()+10:
            self.completed = True
            self.color = (0, 255, 0)
            self.mult = 2
