from Puzzle import Puzzle

solution = [['1','2','3'],['4','5','6'],['7','8','0']] #solution state, used as reference

#prints out puzzle in a readable format
def puzzlePrinter(userPuzzle,nodeCount=0):
    if nodeCount == 0:
        print('Initial State')
        for row in userPuzzle.state:
            for col in row:
                print(col, end = '')
            print('')
        return
    if userPuzzle.state != solution:
        print('Expanding node number',nodeCount,'with best state of g(n) =' , userPuzzle.g, 'and h(n) =', userPuzzle.h)
    for row in userPuzzle.state:
        for col in row:
            print(col, end = '')
        print('')

#solves puzzle using general algorithm
def puzzleSolver(userPuzzle):
        #base case: initial state is already solution
        puzzlePrinter(userPuzzle)
        if userPuzzle.state == solution:
            print('Solution has been found')
            print('To solve this problem the search algorithm expanded a total of',0)
            print('Max number of nodes in queue at any one time was', 1)
            print('Depth of goal node is', 0)
            return
        
        agenda = [userPuzzle]
        repeated = []
        nodeCount = 0
        maxQueueSize = 1
        #loop through agenda while there's still nodes to be expanded
        while len(agenda) is not 0:
            cheapestNode = agenda[0]
            popIndex = 0
            #checks for node with the smallest f(n) in agenda
            for i, a in enumerate(agenda):
                if cheapestNode.f > a.f:
                    cheapestNode = a
                    popIndex = i
            agenda.pop(popIndex)
            repeated.append(cheapestNode.state)
            nodeCount += 1
            puzzlePrinter(cheapestNode,nodeCount)
            cheapestNode.generate_states()
            for direction in cheapestNode.directions:
                if cheapestNode.childrenDict[direction] is not None:
                    if cheapestNode.childrenDict[direction].state == solution:
                        print('Solution has been found!')
                        puzzlePrinter(cheapestNode.childrenDict[direction],nodeCount)
                        print('To solve this problem the search algorithm expanded a total of',nodeCount)
                        print('Max number of nodes in queue at any one time was', maxQueueSize)
                        print('Depth of goal node is',cheapestNode.childrenDict[direction].g - 1)
                        return
                    elif cheapestNode.childrenDict[direction].state not in repeated:
                        agenda.append(cheapestNode.childrenDict[direction])
                        maxQueueSize = max(maxQueueSize, len(agenda))
            
            
        print('No solution')
        print('To solve this problem the search algorithm expanded a total of',nodeCount)
        print('Max number of nodes in queue at any one time was', maxQueueSize)

#main driver, used primarily for user interface and calls the puzzler_solver function
def main():
    tempPuzzle = [[],[],[]] #empty puzzle for future potential puzzle

    #hardcoded test cases
    trivial = [['1','2','3'],['4','5','6'],['7','8','0']]
    veryEasy = [['1','2','3'],['4','5','6'],['7','0','8']]
    easy = [['1','2','0'],['4','5','3'],['7','8','6']]
    doable = [['0','1','2'],['4','5','3'],['7','8','6']]
    ohBoy = [['8','7','1'],['6','0','2'],['5','4','3']]
    impossible = [['1','2','3'],['4','5','6'],['8','7','0']] #unsolvable, program bugged if solved
    print('Welcome to Bailey Yu\'s 8-Puzzle solver.')

    # user choose default puzzle or make their own
    userInput = None
    while userInput != '1' and userInput != '2':

        userInput = input('Type "1" to use a default puzzle, or "2" to enter your own puzzle: ')
        if userInput != '1' and userInput != '2':
            print('Invalid input, please try again')
    print('')

    #let user choose from a selection of default puzzles
    if userInput == '1':
        print('You have chosen to choose a default puzzle')
        puzzleArray = [trivial,veryEasy,easy,doable,ohBoy,impossible]
        difficultyDict = {'1': 'trivial', '2': 'very easy', '3': 'easy', '4': 'doable', '5': 'oh boy', '6':'impossible'}
        userDifficulty = input('Please pick a difficulty between 1-6: ')
        print('You have selected a difficulty of ' + userDifficulty + ', puzzle: ' + difficultyDict[userDifficulty])
        print('')
        tempPuzzle = puzzleArray[int(userDifficulty) - 1]

    #let user set their own puzzle
    elif userInput == '2':
        print('Enter your puzzle, use a zero to represent the blank')
        rowOne = input('Enter the first row, use space or tabs between numbers: ').strip().replace(' ', '')
        rowTwo = input('Enter the second row, use space or tabs between numbers: ').strip().replace(' ' , '')
        rowThree = input('Enter the third row, use space or tabs between numbers: ').strip().replace(' ', '')
        print('')
        
        for i in range(3):
            tempPuzzle[0].append(rowOne[i])
            tempPuzzle[1].append(rowTwo[i])
            tempPuzzle[2].append(rowThree[i])

    #let user choose between three available algorithms
    algorithmChoices = {'1': 'Uniform Cost Search', '2': 'A* with the Misplaced Tile heuristic', '3': 'A* with the Manhattan distance heuristic' }
    print('Enter your choice of algorithm')
    print('1.', algorithmChoices['1'])
    print('2.', algorithmChoices['2'])
    print('3.', algorithmChoices['3'])
    algorithmChoice = input()
    print('You have chosen option ' + algorithmChoice + '. ' + algorithmChoices[algorithmChoice])
    print('')
    userPuzzle = Puzzle(tempPuzzle,algorithmChoice) #creates the initial state, tells Puzzle what heuristic to use

    #puzzle solving function call
    puzzleSolver(userPuzzle)
    

if __name__ == '__main__':
    main()