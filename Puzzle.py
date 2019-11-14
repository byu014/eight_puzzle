import numpy as np
from copy import deepcopy

#Puzzle class used as node
#retains information such as total cost, cost per node, heuristic
#handles children generation of potential moves from current state
#applies heuristic values based on algorithm chosen by user
class Puzzle:
    def __init__(self,state,algorithm,parent=None):
        self.parent = parent
        self.state = state
        self.algorithm = algorithm
        self.directions = ['up','down','left','right']
        self.childrenDict = {'up': None, 'down': None, 'left': None, 'right': None}
        self.zero_pos = (np.where(np.array(self.state) == '0')[0][0],np.where(np.array(self.state) == '0')[1][0]) # finds coordinates of 0
        
        #setup for calculating g(n), h(n), f(n)
        self.g = self.calculate_g() 
        if self.algorithm == '1':
            self.h = 0
        elif self.algorithm == '2':
            self.h = self.calculate_Misplaced_Tile()
        elif self.algorithm == '3':
            self.h = self.calculate_Manhattan_Distance()
        self.f = self.g + self.h

    #generates puzzle when 0 is moved up
    def move_up(self):
        row,col = self.zero_pos
        newState = deepcopy(self.state)
        newState[row][col], newState[row - 1][col] = newState[row-1][col], newState[row][col]
        upPuzzle = Puzzle(newState,self.algorithm,self)
        return upPuzzle
    
    #generates puzzle when 0 is moved down
    def move_down(self):
        row,col = self.zero_pos
        newState = deepcopy(self.state)
        newState[row][col], newState[row + 1][col] = newState[row + 1][col], newState[row][col]
        downPuzzle = Puzzle(newState,self.algorithm,self)
        return downPuzzle
    
    #generates puzzle when 0 is moved left
    def move_left(self):
        row,col = self.zero_pos
        newState = deepcopy(self.state)
        newState[row][col], newState[row][col - 1] = newState[row][col - 1], newState[row][col]
        leftPuzzle = Puzzle(newState,self.algorithm,self)
        return leftPuzzle
    
    #generates puzzle when 0 is moved right
    def move_right(self):
        row,col = self.zero_pos
        newState = deepcopy(self.state)
        newState[row][col], newState[row][col + 1] = newState[row][col + 1], newState[row][col]
        rightPuzzle = Puzzle(newState,self.algorithm,self)
        return rightPuzzle
    
    #generates potential states based on where 0 is
    def generate_states(self):
        row, col = self.zero_pos

        if row != 0:
            self.childrenDict['up'] = self.move_up()
        if row != 2:
            self.childrenDict['down'] = self.move_down()
        if col != 0:
            self.childrenDict['left'] = self.move_left()
        if col != 2:
            self.childrenDict['right'] = self.move_right()
    
    #calculates Misplaced Tile Heuristic
    #using mod math as a counter to compare with each tile
    def calculate_Misplaced_Tile(self):
        currentNum = 1
        h = 0
        for row in self.state:
            for tile in row:
                if str(currentNum % 9) != tile:
                    h += 1
                currentNum += 1
        return h
    
    #calculates Manhattan Distance Heuristic
    #finds distance through combination of row and col difference
    def calculate_Manhattan_Distance(self):
        h = 0
        solutionDict = {'1':(0,0),
                        '2':(0,1),
                        '3':(0,2),
                        '4':(1,0),
                        '5':(1,1),
                        '6':(1,2),
                        '7':(2,0),
                        '8':(2,1),
                        '0':(2,2)
                        }

        for i,row in enumerate(self.state):
            for j,tile in enumerate(row):
                if solutionDict[tile] != (i,j):
                    h += abs(solutionDict[tile][0] - i) + abs(solutionDict[tile][1] - j)
        return h

    #calculates g(n), incrementing by 1 per depth
    def calculate_g(self):
        g = 0
        if self.parent is not None:
            g = self.parent.g + 1
        else:
            g = 1
        return g