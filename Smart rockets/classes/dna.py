import numpy as np
import random
from pygame.math import Vector2

class Dna:
    def __init__(self, size):
        self.genotype = np.empty(size, dtype=object)
        self.size = size
        self.fitness = 0
        
        for i in range(size):
            self.genotype[i] = Vector2(random.randint(-1, 1), random.randint(-1, 1))

    def crossover(self, partner):
        child = Dna(self.size)
        midpoint = random.randint(0, self.size - 1)
        
        for i in range(self.size):
            if i < midpoint:
                child.genotype[i] = self.genotype[i]
            else:
                child.genotype[i] = partner.dna.genotype[i]

        return child
    
    def mutate(self, mutationRate):
        for i in range(self.size):
            if random.random() < mutationRate:
                self.genotype[i] = Vector2(random.randint(-1, 1), random.randint(-1, 1)) * 1.3
    
