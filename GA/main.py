from classes.Population import Population
import numpy as np
import sys
import time
import random

populationSize = 400
mutationRate = 0.015
ntarget = 'felipe eh viado'

def makePhrase(string):
    s = np.empty(len(string), dtype=str)
    for i in range(len(string)):
        s[i] = string[i]

    return np.copy(s)

def main():
    #initialize
    global ntarget
    random.seed(time.clock())
    target = makePhrase(ntarget)
    population = Population(populationSize, mutationRate, target)
    
    generation = 1
    
    while True:
        print('generation: ' + str(generation))

        #natural evolution     
        population.evolve()
        population.calculateFitness()
        print(population.getBestGenotype())
        print(population.best.fitness)
        
        generation += 1
        
        if ''.join(target) == ''.join(population.best.genotype):
            print('found')
            break

if __name__ == '__main__':
    main()
    o = 0
