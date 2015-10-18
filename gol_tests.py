#!/usr/bin/env python3

from game_of_life import *
import unittest

class TestBabiStuff(unittest.TestCase):

    def test_count_neighbors(self):

        X = Y = 3
        board = {(a,b):0 for a in range(X) for b in range(Y)} 
        board[(0,0)] = 1
        adjacent = count_neighbors((1,1), board)
        self.assertTrue(adjacent == 1)

        X = Y = 3
        board = {(a,b):0 for a in range(X) for b in range(Y)} 
        board[(0,0)] = 1
        board[(2,2)] = 1
        adjacent = count_neighbors((1,1), board)
        self.assertTrue(adjacent == 2)

        adjacent = count_neighbors((0,1), board)
        self.assertTrue(adjacent == 1)



    def test_update_board(self):
        X = Y = 3
        board = {(a,b):0 for a in range(X) for b in range(Y)} 
        
        board[(1,1)] = 1

        board = update_board(board)
        self.assertTrue(board[(1,1)] == 0)
        



if __name__ == "__main__":
    unittest.main()
