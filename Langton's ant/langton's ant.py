from graphics import *
import numpy as np
from time import sleep

####
width = 700
height = 700
prop = 2
####
gridSize = int(width/prop)
####

'''
#draw one by one(not efficiente)
def drawGrid(grid, screen):
    for i in range(gridSize):
        for j in range(gridSize):
            point1 = Point(i * prop, j * prop)
            point2 = Point(i * prop + prop, j* prop + prop)
            rect = Rectangle(point1, point2)
            if grid[i][j] == 0:
                rect.setFill('white')
            else:
                rect.setFill('black')
            rect.draw(screen)
'''

def changeGrid(grid):
    global antx, anty
    state = grid[antx][anty]
    if state == 0:
        moveRight()
        grid[antx][anty] = 1
    elif state == 1:
        moveLeft()
        grid[antx][anty] = 0
    moveFoward()

############################################
antx = int(gridSize*0.5)
anty = int(gridSize*0.5)
antup = 0
antright = 1
antdown = 2
antleft = 3
direction = antup 

def moveFoward():
    global antx, anty
    global antup, antright, antdown, antleft
    
    if direction == antup:
        antx -= 1
    elif direction == antright:
        anty += 1
    elif direction == antdown:
        antx += 1
    elif direction == antleft:
        anty -= 1

    if antx > gridSize - 1:
        antx = 0
    elif antx < 0:
        antx = gridSize - 1
    if anty > gridSize - 1:
        anty = 0
    elif anty < 0:
        anty = gridSize - 1
        
def moveLeft():
    global direction
    global antup, antleft
    
    direction -= 1
    if direction < antup:
        direction = antleft
        
def moveRight():
    global direction
    global antup, antleft
    
    direction += 1
    if direction > antleft:
        direction = antup
############################################

def drawChangedPixel(grid, screen):
    global antx, anty
    state = grid[antx][anty]

    point1 = Point(antx * prop, anty * prop)
    point2 = Point(antx * prop + prop, anty* prop + prop)
    rect = Rectangle(point1, point2)
    if state == 0:
        rect.setFill('white')
    elif state == 1:
        rect.setFill('black')
    rect.setWidth(0)
    rect.draw(screen)
    
def main():
    win = GraphWin('Ant', width, height)

    ####
    grid = np.zeros((gridSize, gridSize), dtype=int)
    win.setBackground('white')
    while True:
        changeGrid(grid)
        drawChangedPixel(grid, win)
    ####
    
    win.getMouse()
    win.close()
    
#if __name__ == '__name__':
main()
