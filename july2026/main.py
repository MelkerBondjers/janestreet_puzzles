# Solving the Jane Street Puzzle for July 2026
# The puzzle instructions can be found at https://www.janestreet.com/puzzles/ 
# Puzzle name: ‘Pent-Up’ Frustration 3 / Knight Moves 7


import numpy as np

base_matrix = np.zeros((8, 8)) 

# The forced moves between each number were calculated using logic
# As a result, the 0-1 path, and the 16-23 path were forced.
# They were placed in the matrices reduce complexity and increase efficiency. 


# 1 represents a region with a tower, 0 represents a region without a tower
tower_matrix = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 1, 1, 0, 0, 0], 
    [0, 0, 0, 1, 1, 1, 0, 0], 
    [0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 1, 1, 0], 
    [0, 1, 0, 1, 1, 1, 0, 0], 
    [0, 1, 1, 1, 1, 0, 0, 0], 
    [1, 1, 1, 1, 0, 0, 0, 0]
    ])

# All of the given numbers and their position (first position is represented as 1 eventhough it is 0)
number_matrix = np.array([
    [0, 0, 0, 0, 14, 37, 0, 1100], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 23, 112, 138, 0, 0], 
    [528, 0, 0, 0, 0, 0, 0, 0], 
    [0, 449, 0, 0, 16, 0, 0, 0], 
    [0, 750, 0, 88, 3, 272, 1, 0], 
    [0, 0, 1, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0]
    ])

# All of the regions without towers, represented with 1s
regions = [
    np.array([
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0, 0, 0], 
    [1, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]), 
    np.array([
    [0, 0, 0, 0, 0, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]), 
    np.array([
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 1, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]), 
    np.array([
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]), 
    np.array([
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 1, 1, 0, 0, 0], 
    [0, 0, 0, 1, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]), 
    np.array([
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 1, 1]
    ]), 
    np.array([
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 1, 1, 0, 0]
    ]),
    np.array([
    [1, 1, 1, 1, 1, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]), 
    np.array([
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]), 
]

# all of the starting numbers with mulitple paths to the next number
# the number of moves and end number was calculated using logic and testing
given_num_dicts = [
    {
    "value": 1,
    "move_number": 3,
    "start": [5,6],
    "end": [4,4],
    "tower": False,
    "moves": ["n","n","n"]
    },
    {
    "value": 23,
    "move_number": 9,
    "start": [2,3],
    "end": [3,0],
    "tower": False,
    "moves": ["n","n","t"]
    },
    {
    "value": 528,
    "move_number": 12,
    "start": [3,0],
    "end": [0,5],
    "tower": True,
    "moves": ["n","n","t"]
    },
    {
    "value": 37,
    "move_number": 15,
    "start": [0,5],
    "end": [5,3],
    "tower": False,
    "moves": ["n","n","n"]
    },
    {
    "value": 88,
    "move_number": 18,
    "start": [5,3],
    "end": [2,5],
    "tower": False,
    "moves": ["n","n","t","n","n","t","n"]
    },
    {
    "value": 138,
    "move_number": 25,
    "start": [2,5],
    "end": [5,5],
    "tower": False,
    "moves": ["n","n","n","n","t","t","n"]
    },
    {
    "value": 272,
    "move_number": 32,
    "start": [5,5],
    "end": [4,1],
    "tower": False,
    "moves": ["t","t","n","n","n","n","n"]
    },
    {
    "value": 449,
    "move_number": 39,
    "start": [4,1],
    "end": [5,1],
    "tower": False,
    "moves": ["n","n","n","n","n","n","n"]
    },
    {
    "value": 750,
    "move_number": 46,
    "start": [5,1],
    "end": [0,7],
    "tower": False,
    "moves": ["n","n","n","n","n","n","n"]
    },
]


# All possible moves if the knight moves to a position on the same level
normal_moves = np.array(
    [[-2,-1], [-2,1], [-1,-2], [-1,2], [1,-2], [1,2], [2,-1], [2,1]]
)
# All possible moves if the knight moves to or from a tower
tower_moves = np.array(
    [[-2,0], [2,0], [0,-2], [0,2]]
)


# Checks if the move is valid i.e. 
# 1: if the move is in the array 
# 2: if the move is to an empty position or if the next value is the same as the move position in number_matrix
def valid_move(next_start, current_path, next_value):
    if 0 <= next_start[0] < 8 and 0 <= next_start[1] < 8:
        if (current_path + number_matrix)[next_start[0]][next_start[1]] == 0:
            return True
        elif number_matrix[next_start[0]][next_start[1]] == next_value:
            return True
    else: 
        return False

# Runs if the next move will place a tower
# Checks if the move will land on a region without a tower
# If it does, add that region to the next_tower_regions array
def valid_tower(next_start, next_tower_regions):
    if (next_tower_regions + tower_matrix)[next_start[0]][next_start[1]] == 0: 
        for region in regions: 
            if region[next_start[0]][next_start[1]] == 1: 
                next_tower_regions += region
                return True
    else: 
        return False


# Recursive function to find all of the paths
def get_paths(value, move_number, start, end, tower, moves, all_paths, current_path, current_tower_regions):
    
    # If there are no moves left and it ended on the right square, save the path and towers
    if start == end and len(moves) == 0: 
        all_paths.append([current_path.copy(), current_tower_regions.copy()])
        return
    elif len(moves) == 0: #If it ended on the wrong square, return
        return
    
    # "Normal" moves (moves on the same height)
    if moves[0] == "n": 

        for move in normal_moves: # Goes through all of the possible normal moves from the starting position
            
            next_start = [start[0]+move[0], start[1]+move[1]] # The next start will be move + start
            next_value = value + move_number + 1 # Because there is no hight delta

            if not valid_move(next_start, current_path, next_value): # Check move validity
                continue
            
            next_tower = tower # Because no height delta
            next_tower_regions = current_tower_regions.copy() 

            if next_tower:
                if not valid_tower(next_start, next_tower_regions): # If there is a tower, check tower validity
                    continue
            
            next_path = current_path.copy()

            # To only add the path between the start and end
            if len(moves) > 1: 
                next_path[next_start[0], next_start[1]] = next_value
            


            # Call the function again, with the next value, move number, start, tower, path and tower regions. Also remove first move from moves
            get_paths(next_value, move_number + 1, next_start, end, next_tower, moves[1:], all_paths, next_path, next_tower_regions)

    # If the knight moves to or from a tower
    elif moves[0] == "t": 
        for move in tower_moves: # Goes through all of the possible "tower" moves from the starting position

            next_start = [start[0]+move[0], start[1]+move[1]] 

            if tower: # If the knight is currently on a tower
                next_value = value/(move_number + 1)
                next_tower = False
            elif not tower: # If the knight is not on a tower
                next_value = value * (move_number + 1)
                next_tower = True
            
            if not valid_move(next_start, current_path, next_value): # check move validity
                continue

            next_tower_regions = current_tower_regions.copy()

            if next_tower:
                if not valid_tower(next_start, next_tower_regions): # If the next move places a tower, check validity
                    continue
            
            next_path = current_path.copy()

            if len(moves) > 1:  # To only add the path between start and end
                next_path[next_start[0], next_start[1]] = next_value
            
            # Run function again with updated variables
            get_paths(next_value, move_number + 1, next_start, end, next_tower, moves[1:], all_paths, next_path, next_tower_regions)

#Check if no numbers between greater than 0 overlaps 
def valid_number_combination(current_numbers, new_numbers):
    for i in range(8):
        for j in range(8):
            if current_numbers[i][j] > 0 and new_numbers[i][j] > 0:
                return False
    return True

# Check if there are multiple towers in a region
def valid_tower_combination(current_towers, new_towers):
    for i in range(8):
        for j in range(8):
            if (current_towers + new_towers)[i][j] > 1:
                return False
    return True

# Recursive function to find the correct path combination
def combine_paths(all_paths, current_numbers, current_towers): 

    if len(all_paths) == 0: # If there are no more paths to add

        # Because the knight moves from 0 to 1100 only places 12 towers, the knight needs to be able to either: 
        # Move from 1100 to a different region and place a tower
        # Move from 1100 and place a tower in the same region

        # This means that current_numbers needs to have [1,5], [2,6] or [2,7] empty

        if current_numbers[1,5] == 0 or current_numbers[2,6] == 0 or current_numbers[2,7] == 0:
            solution.append(current_numbers)
        return
    
    # loop through all of the paths for the first number in all_paths
    for path in all_paths[0]:
        # each path has two 8x8 arrays, one for the numbers and one for the towers
        new_numbers = path[0]
        new_towers = path[1]

        # Check if the validity the combinaition
        if not valid_number_combination(current_numbers, new_numbers):
            continue
        if not valid_tower_combination(current_towers, new_towers):
            continue
        
        # add the numbers and towers and run the function again
        next_numbers = new_numbers + current_numbers
        next_towers = new_towers + current_towers
        combine_paths(all_paths[1:], next_numbers, next_towers)



all_paths = [] # create an array where all of the paths will be stored
current_path = np.zeros((8,8)) 
current_tower_regions = np.zeros((8,8))

for dict in given_num_dicts: # loop through all of the different dictionaries
    paths = [] # create an array where all of the paths for the current dict are stored

    # Find all the paths for dict
    get_paths(dict["value"], dict["move_number"], dict["start"], dict["end"], dict["tower"], dict["moves"], paths, current_path, current_tower_regions)
    all_paths.append(paths) # Add the paths to all_paths





np.set_printoptions(suppress=True) # to remove scientific notation

solution = []
combine_paths(all_paths, number_matrix, tower_matrix) # Adds the solved matrix to solution

print(solution[0])
