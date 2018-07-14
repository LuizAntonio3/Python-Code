import sys, pygame
from random import randint
import numpy as np
from ant_class import Ant
from random import randint

pygame.init()

w = 400
h = 400
quant_ants = 10

size = [w, h]

def main():
    grid = np.zeros((w, h, 3))
    grid.fill(255)
    screen = pygame.display.set_mode(size)

    count = 0

    ants = np.empty(quant_ants, dtype=object)
    for i in range(quant_ants):
        ants[i] = Ant(randint(0, w - 1), randint(0, h - 1), randint(0, 3))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
        ####

        ## task === create a destruction ant that destroy the things on the grid
        ## is capable of killing another ants
        for j in range(500):
            for i in range(quant_ants):
                ants[i].changeGrid(grid)
        ####
                
        screen.fill((0, 0, 0, 0))
        pygame.surfarray.blit_array(screen, grid)
        pygame.display.update()

if __name__ == '__main__':
    main()
