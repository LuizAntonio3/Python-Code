import pygame, sys
import numpy as np
import random
from classes.population import Population
from classes.target import Target
from classes.obstacle import Obstacle

pygame.init()

w = 600
h = 400
lifeSpan = 200 #ciclos
mutationRate = 0.05
amountOfRockets = 200
targetPosition = pygame.math.Vector2(w/2, 20)
obsPosition1 = (pygame.math.Vector2(100, 225), pygame.math.Vector2(500, 250))
obsPosition2 = (pygame.math.Vector2(0, 150), pygame.math.Vector2(100, 175))
obsPosition3 = (pygame.math.Vector2(w - 100, 150), pygame.math.Vector2(w, 175))

size = (w, h)
        
def main():
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Smart Rocket')

    obs = np.empty(3, dtype=object)
    obs[0] = Obstacle(obsPosition1[0], obsPosition1[1])
    obs[1] = Obstacle(obsPosition2[0], obsPosition2[1])
    obs[2] = Obstacle(obsPosition3[0], obsPosition3[1])
    target = Target(targetPosition)
    pop = Population(screen, amountOfRockets, lifeSpan, mutationRate, target)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
        ## evolving code
        pop.run(obs, target)
        obs[0].draw(screen)
        obs[1].draw(screen)
        obs[2].draw(screen)
        target.draw(screen)
        ##
                
        pygame.display.update()
        screen.fill((0, 0, 0))

if __name__ == '__main__':
    main()
