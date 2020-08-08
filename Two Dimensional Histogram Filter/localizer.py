import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs =[[] for i in range(0,len(beliefs))]
    sum =0
     # TODO - implement this in part 2
        
    for  row in range(0,len(grid)):
        for col in range(0,len(grid[0])):
            # check the measurment by the gird
            if grid[row][col] == color:
                new_beliefs[row].append(beliefs[row][col]* p_hit)
                
            else:
                new_beliefs[row].append(beliefs[row][col] * p_miss)
                
            #sum all elemnts to normalize    
            sum +=  new_beliefs[row][col] 
            
    for  i in range(0,len(new_beliefs)):
        for j in range(0,len(new_beliefs[0])):
            #normalization
            new_beliefs[i][j] /= sum
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0 for i in range(0,width)]  for k in range(0,height)]
    for i, row in enumerate(beliefs):
        for k, cell in enumerate(row):
            new_i = (i + dy ) % (height)
            new_j = (k + dx ) % (width)
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)