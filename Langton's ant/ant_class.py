class Ant:
    def __init__(self, initial_x, initial_y, initial_direction=1):
        self.antx = initial_x
        self.anty = initial_y
        self.direction = initial_direction
        
        self.antup = 0
        self.antright = 1
        self.antdown = 2
        self.antleft = 3

    def moveFoward(self, whereSize):        
        if self.direction == self.antup:
            self.antx -= 1
        elif self.direction == self.antright:
            self.anty += 1
        elif self.direction == self.antdown:
            self.antx += 1
        elif self.direction == self.antleft:
            self.anty -= 1

        if self.antx > whereSize - 1:
            self.antx = 0
        elif self.antx < 0:
            self.antx = whereSize - 1
        if self.anty > whereSize - 1:
            self.anty = 0
        elif self.anty < 0:
            self.anty = whereSize - 1
        
    def moveLeft(self):     
        self.direction -= 1
        if self.direction < self.antup:
            self.direction = self.antleft
            
    def moveRight(self):
        self.direction += 1
        if self.direction > self.antleft:
            self.direction = self.antup

    def changeGrid(self, grid):
        state = grid[self.antx, self.anty, 0]
        if state == 0:
            self.moveRight()
            grid[self.antx, self.anty, :] = 255
            #print('ok ---- #####')
        elif state == 255:
            self.moveLeft()
            grid[self.antx, self.anty, :] = 0
            #print('ok ---- *****')
        self.moveFoward(len(grid))
