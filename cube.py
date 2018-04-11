#!/usr/bin/env python
# Daniel Delago

import sys

class Cube:
    def __init__(self):
        # 2D List representation of the cube
        #     0       1      2      3     4     5
        # [[Front],[Right],[Back],[Left],[Up],[Down]]
        #     0         1         2         3         4        5           6           7            8
        # [Top-Left, Top-Mid, Top-Right, Mid-Left, CENTER, Mid-Right, Bottom-Left, Bottom-Mid, Bottom-Right]
        # [0, 1, 2,
        #  3, 4, 5,
        #  6, 7, 8]
        self.state = [['R','R','R','R','R','R','R','R','R'],
                      ['G','G','G','G','G','G','G','G','G'],
                      ['O','O','O','O','O','O','O','O','O'],
                      ['B','B','B','B','B','B','B','B','B'],
                      ['Y','Y','Y','Y','Y','Y','Y','Y','Y'],
                      ['W','W','W','W','W','W','W','W','W']]

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

    # Rotate face handler
    def rotate_face(self, face):

    # Rotate face clockwise
    def rotate_clockwise(self, face):
        # Rotate pieces on face
        self.state[face] = [self.state[face][6],self.state[face][3],self.state[face][0],
                            self.state[face][7],self.state[face][5],self.state[face][1],
                            self.state[face][8],self.state[face][5],self.state[face][2]]

        # Rotate pieces along edge of face
        # If U face rotation
        if face == 4:
            # Front Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]

            # Right Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]

            # Back Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]

            # Left Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
        # If D face rotation
        elif face == 5:
            # Front Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]

            # Right Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]

            # Back Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]

            # Left Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
        # Side rotation
        else:


    # Rotate face counter-clockwise (Prime)
    def rotate_prime(self, face):
        # Rotate pieces on face
        self.state[face] = [self.state[face][2],self.state[face][5],self.state[face][8],
                            self.state[face][1],self.state[face][5],self.state[face][7],
                            self.state[face][0],self.state[face][3],self.state[face][6]]    
    
        # Rotate pieces along edge of face
        # If U face rotation
        if face == 4:
            # Front Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]

            # Right Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]

            # Back Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]

            # Left Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
        # If D face rotation
        elif face == 5:
            # Front Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]

            # Right Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]

            # Back Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]

            # Left Face 
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
            self.state[face][] = self.state[face][6]
        # Side rotation
        else:

# Main
if __name__ == '__main__':

    cube = Cube()

    print(cube.state)