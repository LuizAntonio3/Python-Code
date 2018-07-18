import numpy as np
import random

def char():
    table = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ,'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's' ,'t', 'u', 'v', 'w', 'x', 'y', 'z', ' '])
    return table[random.randint(0, len(table) - 1)]

class Dna:
    def __init__(self, size):
        self.genotype = np.empty(size, dtype=str)
        self.size = size
        self.fitness = 0
        
        for i in range(size):
            self.genotype[i] = char()

    def crossover(self, partner):
        child = Dna(self.size)
        midpoint = random.randint(0, self.size - 1)
        
        for i in range(self.size):
            if i < midpoint:
                child.genotype[i] = self.genotype[i]
            else:
                child.genotype[i] = partner.genotype[i]

        return child
    
    def mutate(self, mutationRate):
        for i in range(self.size):
            if random.random() < mutationRate:
                self.genotype[i] = char()

    def calcFitness(self, target):
        score = 0
        for i in range(self.size):
            if self.genotype[i] == target[i]:
                score += 1
        self.fitness = (score / len(target)) + 0.01
