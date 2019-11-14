# eight_puzzle

### To run use command python3 eightpuzzle.py

## About
This is a command line interface of the game eight puzzle. The program lets the user input the configurations of the game tiles or choose from a list of default configurations. 

## Algorithms
The program is solvable using three different algorithms:

# Uniform Cost Search
The uniform cost search algorithm is essentially the A* algorithm with h(n), the heuristic, set to 0. This algorithm simply expands nodes that is the cheapest.

# A* with Misplaced Tile Heuristic
The A* with misplaced tile heuristic calculates h(n) by how many tiles are out of place when comparing the current state to the solution state. Each out of place tile increases h(n) by 1, up to a value of 9 if all are misplaced. 

# A* with Manhattan Distance Heuristic
The A* with Manhattan distance heuristic also calculates h(n), but in a different way than misplaced tile heuristic. This algorithm checks how far off each misplaced tile is from its intended position when checked against the solution state. By calculating the off-distance for each individual tile, the heuristic is the total of all the off-distance of each tile.
