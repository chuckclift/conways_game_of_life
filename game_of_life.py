#!/usr/bin/env python3

from random import random
import time

def count_neighbors(target, board):
    target_x, target_y = target
    relative_points = [(a,b) for a in (-1,0,1) for b in (-1, 0, 1)
                                             if not (a,b) == (0,0)]

    adjacent_living = 0
    for x,y in relative_points:
        adjusted = (target_x + x, target_y + y)
        if adjusted in board:
            adjacent_living += board[adjusted] 
    return adjacent_living

def display_board(board):
    x_dim = max((x for x,y in board))
    y_dim = max((y for x,y in board))

    print("="*x_dim)


    for y in range(y_dim):
        for x in range(x_dim):
            print("*" if board[(x,y)] else " ", end="")
        print("")
    print(" ")

def randomize_board(board):
    return {tile: 1 if random() > 0.5 else 0  for tile in board}

def random_board(x,y):
    return {(a,b): 1 if random() > 0.5 else 0 for a in range(x) for b in range(y)} 


def tile_alive(neighbors, life_value):
    alive = life_value == 1
    if alive and  neighbors in {2,3}:
        return 1
    if not alive and neighbors == 3:
        return 1
    else:
        return 0

def simulate_tile(tile, board):
    neighbors = count_neighbors(tile, board)
    return tile_alive(neighbors, board[tile])

def update_board(board):
    return {tile:simulate_tile(tile, board) for tile in board}

def board_difference(board1, board2):
    return sum([b for a, b in board1.items()]) - sum([b for a, b in board2.items()])

def get_entropy(board1, board2):
    return abs(board_difference(board1, board2))

def zero_entropy(historic_entropy):
    return sum(historic_entropy) == 0

def main():
    X = 180 # 90
    Y = 50
    previous = {(a,b):0 for a in range(X) for b in range(Y)}
    cells = randomize_board(previous)

    start = time.time()

    # initializing values to nonzero entropy so it gets past the exit condition             
    historic_entropy = [1 for a in range(5)]
        
    while not zero_entropy(historic_entropy):
        cells = update_board(cells)
        entropy = get_entropy(cells, previous)
        historic_entropy = historic_entropy[-4:] + [entropy]
        previous = cells

        display_board(cells)
        print("entropy: ", entropy)
#        time.sleep(0.1)


if __name__ == "__main__":
    main()
