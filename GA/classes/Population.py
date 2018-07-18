from classes.dna import Dna
import random
import numpy as np

class Population:
    def __init__(self, populationSize, mutationRate, target):
        self.population = np.empty(populationSize, dtype=object)
        self.popSize = populationSize
        self.targ = target
        for i in range(populationSize):
            self.population[i] = Dna(len(target))
        self.mutationRate = mutationRate
        self.best = None
        self.mate = np.empty(int(self.popSize), dtype=object)
        self.calculateFitness()

    def calculateFitness(self):
        self.best = self.population[0]
        for i in range(self.popSize):
            self.population[i].calcFitness(self.targ)
            if self.population[i].fitness > self.best.fitness:
                self.best = self.population[i]

    def acceptReject(self):
        maxFitness = 1.01
        for i in range(len(self.mate)):
            while True:
                r1 = random.randint(0, len(self.mate)-1)
                r2 = random.randint(0, maxFitness * 100) / 100
                if r2 < self.population[r1].fitness:
                    self.mate[i] = self.population[r1]
                    break
            #print()
            #print(self.mate[i].genotype)
            #print(self.mate[i].fitness)
        
    def evolve(self):
        self.acceptReject()
        for i in range(self.popSize):
            a = random.randint(0, len(self.mate)-1)
            b = random.randint(0, len(self.mate)-1)
            child = self.mate[a].crossover(self.mate[b])
            child.mutate(self.mutationRate)

            self.population[i] = child

    def getBestGenotype(self):
        return ''.join(self.best.genotype)
