from graphics import *
import numpy as np
from time import sleep
from ant_class import Ant

'''
problema com o grid, na class mudei para 3 dimensões o array
aq o grid tem apenas 2
'''

####
width = 600
height = 600
prop = 3
####
gridSize = int(width/prop)
####

def drawChangedPixel(grid, screen, ant1, ant2):
    state1 = grid[ant1.antx][ant1.anty]
    state2 = grid[ant2.antx][ant2.anty]
    
    #ant 1
    point1 = Point(ant1.antx * prop, ant1.anty * prop)
    point2 = Point(ant1.antx * prop + prop, ant1.anty* prop + prop)
    rect = Rectangle(point1, point2)
    if state1 == 0:
        rect.setFill('white')
    elif state1 == 1:
        rect.setFill('black')

    #rect.setWidth(0)
    rect.draw(screen)
    
    #ant 2
    point1 = Point(ant2.antx * prop, ant2.anty * prop)
    point2 = Point(ant2.antx * prop + prop, ant2.anty* prop + prop)
    rect = Rectangle(point1, point2)
    if state2 == 0:
        rect.setFill('white')
    elif state2 == 1:
        rect.setFill('black')

    rect.setWidth(0)
    rect.draw(screen)
    
    
def main():
    win = GraphWin('Ant', width, height)

    ####
    grid = np.zeros((gridSize, gridSize), dtype=int)
    ant1 = Ant(60, 60)
    ant2 = Ant(160, 160, 3)
    win.setBackground('white')
    while True:
        ant1.changeGrid(grid)
        ant2.changeGrid(grid)
        drawChangedPixel(grid, win, ant1, ant2)
        #print(grid)
    ####
    
    win.getMouse()
    win.close()
    
if __name__ == '__main__':
    main()
