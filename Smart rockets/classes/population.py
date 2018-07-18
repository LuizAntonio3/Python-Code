from classes.dna import Dna
from classes.rocket import Rocket
import random
import numpy as np
import pygame

class Population:
    def __init__(self, whereWillLive, size, lifeSpan, mutationRate, target):
        self.popSize = size
        self.lifeSpan = lifeSpan
        self.lifeCount = 0
        self.generation = 1
        
        self.population = np.empty(size, dtype=object)
        self.where = whereWillLive
        for i in range(size):
            self.population[i] = Rocket(self.where, self.lifeSpan, target)

        self.mutationRate = mutationRate
        self.best = self.population[0]
        self.mate = np.empty(int(self.popSize), dtype=object)
        self.target = target
        self.font = pygame.font.SysFont('Arial', 15)
        self.gen = self.font.render('Generation: {} Best: {}'.format(str(self.generation), str(int(self.best.fitness*1000))) , False, (255, 255, 255))
        
    def calculateFitness(self):
        for i in range(self.popSize):
            self.population[i].calcFitness(self.target)
            if self.population[i].fitness > self.best.fitness:
                self.best = self.population[i]

    def acceptReject(self):
        maxFitness = 1.0 * 2
        self.mate[0:int(len(self.mate)/4)] = self.best
        for i in range(int(len(self.mate)/4), len(self.mate)):
            while True:
                r1 = random.randint(0, len(self.mate)-1)
                r2 = random.randint(0, maxFitness * 100) / 100
                if r2 < self.population[r1].fitness:
                    self.mate[i] = self.population[r1]
                    break

    def run(self, obstacles, target=None):
        self.where.blit(self.gen, (5 ,self.where.get_height()-20))
        
        allDead = True
        if target == None:
            target = self.target
        else:
            self.target = target
        
        for i in range(self.popSize):
            if self.population[i].crashed == False:
                allDead = False
        if self.lifeCount > self.lifeSpan or allDead:
            self.calculateFitness()
            self.evolve()
            self.lifeCount = 0
            self.generation += 1
            self.gen = self.font.render('Generation: {} Best: {}'.format(str(self.generation), str(int(self.best.fitness*1000))) , False, (255, 255, 255))
        else:
            for i in range(self.popSize):
                self.population[i].update(obstacles)
            self.lifeCount += 1
    
    def evolve(self):
        self.acceptReject()
        for i in range(self.popSize):
            a = random.randint(0, len(self.mate)-1)
            b = random.randint(0, len(self.mate)-1)
            child = self.mate[a].dna.crossover(self.mate[b])
            child.mutate(self.mutationRate)

            self.population[i] = Rocket(self.where, self.lifeSpan, self.target, child)
        #self.best = self.population[0]
    
