#!/usr/bin/env python
# Daniel Delago

import sys

class Cube:
    def __init__(self):
        # Create 2D List of the cube
        # [[Front],[Back],[Left],[Right],[Up],[Down]]
        self.state = [['R','R','R','R','R','R'],
                      ['G','G','G','G','G','G'],
                      ['O','O','O','O','O','O'],
                      ['B','B','B','B','B','B'],
                      ['Y','Y','Y','Y','Y','Y'],
                      ['W','W','W','W','W','W']]
        # Distance from root
        self.cost = 0
        # Parent node with shortest path
        self.parent = None
        # Dictionary of connected edges with path cost as values 
        self.edges = {}

    # Scramble the cube
    def CreateScramble (self):
        move_list = ['R','L','F','B','U','D','r','l','f','b','u','d',]
        new_scramble = []
        for x in range(0, 30):
            new_scramble.append(random.choice(move_list))


    # Cube Rotations
    # Right Hand 
    def R(self):
    def r(self):

    # Left Hand 
    def L(self):
    def l(self):
    
    # Front Face 
    def F(self):
    def f(self):
    
    # Back Face 
    def B(self):
    def b(self):

    # Top Face  
    def U(self):
    def u(self):

    # Bottom Face
    def D(self):
    def d(self):
    
    
# Main
if __name__ == '__main__':

    cube = Cube()

    print(cube.state)