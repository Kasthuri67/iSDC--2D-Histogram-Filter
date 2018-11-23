#import pdb
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
    new_beliefs = []

    #
    # TODO - implement this in part 2
    #
    height, width  = len(beliefs), len(beliefs[0])

    new_beliefs = [[0.0 for row_index in range(width)]for col_index in range(height)]

    sum_new_beliefs = 0

    for row_index, row in enumerate(grid):
        for col_index, item in enumerate(row):
            hit = (color == grid[row_index][col_index])
            new_beliefs[row_index][col_index] = beliefs[row_index][col_index] * (hit * p_hit + (1-hit) * p_miss)
    sum_new_beliefs += sum(new_beliefs[row_index])
  

    return normalize(new_beliefs)

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            #pdb.set_trace()
            new_G[int(new_j)][int(new_i)] = cell
    return blur(new_G, blurring)