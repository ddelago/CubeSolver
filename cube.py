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
            # Temp Front Face
            temp_0 = self.state[0][0]
            temp_1 = self.state[0][1]
            temp_2 = self.state[0][2]

            # Front Face 
            self.state[0][0] = self.state[1][0]
            self.state[0][1] = self.state[1][1]
            self.state[0][2] = self.state[1][2]

            # Right Face 
            self.state[1][0] = self.state[2][0]
            self.state[1][1] = self.state[2][1]
            self.state[1][2] = self.state[2][2]

            # Back Face 
            self.state[2][0] = self.state[3][0]
            self.state[2][1] = self.state[3][1]
            self.state[2][2] = self.state[3][2]

            # Left Face 
            self.state[3][0] = temp_0
            self.state[3][1] = temp_1
            self.state[3][2] = temp_2
        # If D face rotation
        elif face == 5:
            # Temp Back Face
            temp_0 = self.state[2][6]
            temp_1 = self.state[2][7]
            temp_2 = self.state[2][8]

            # Front Face 
            self.state[0][6] = self.state[3][6]
            self.state[0][7] = self.state[3][7]
            self.state[0][8] = self.state[3][8]

            # Right Face 
            self.state[1][6] = self.state[0][6]
            self.state[1][7] = self.state[0][7]
            self.state[1][8] = self.state[0][8]

            # Back Face 
            self.state[2][6] = self.state[1][6]
            self.state[2][7] = self.state[1][7]
            self.state[2][8] = self.state[1][8]

            # Left Face 
            self.state[3][6] = temp_0
            self.state[3][7] = temp_1
            self.state[3][8] = temp_2        
        # Side rotation
        else:
            # Temp Front Face
            temp_0 = self.state[face-1][2]
            temp_1 = self.state[face-1][5]
            temp_2 = self.state[face-1][8]

            # Front Face 
            self.state[0][2] = self.state[1][2]
            self.state[0][5] = self.state[1][5]
            self.state[0][8] = self.state[1][8]

            # Bottom Face 
            self.state[1][2] = self.state[2][2]
            self.state[1][5] = self.state[2][5]
            self.state[1][8] = self.state[2][8]

            # Back Face 
            self.state[2][2] = self.state[3][2]
            self.state[2][5] = self.state[3][5]
            self.state[2][8] = self.state[3][8]

            # Top Face 
            self.state[3][2] = temp_0
            self.state[3][5] = temp_1
            self.state[3][8] = temp_2

    # Rotate face counter-clockwise (Prime)
    def rotate_prime(self, face):
        # Rotate pieces on face
        self.state[face] = [self.state[face][2],self.state[face][5],self.state[face][8],
                            self.state[face][1],self.state[face][5],self.state[face][7],
                            self.state[face][0],self.state[face][3],self.state[face][6]]    
    
        # Rotate pieces along edge of face
        # If U face rotation
        if face == 4:
            # Temp Front Face
            temp_0 = self.state[0][0]
            temp_1 = self.state[0][1]
            temp_2 = self.state[0][2]

            # Front Face 
            self.state[0][0] = self.state[1][0]
            self.state[0][1] = self.state[1][1]
            self.state[0][2] = self.state[1][2]

            # Right Face 
            self.state[1][0] = self.state[2][0]
            self.state[1][1] = self.state[2][1]
            self.state[1][2] = self.state[2][2]

            # Back Face 
            self.state[2][0] = self.state[3][0]
            self.state[2][1] = self.state[3][1]
            self.state[2][2] = self.state[3][2]

            # Left Face 
            self.state[3][0] = temp_0
            self.state[3][1] = temp_1
            self.state[3][2] = temp_2
        # If D face rotation
        elif face == 5:
            # Temp Back Face
            temp_0 = self.state[2][6]
            temp_1 = self.state[2][7]
            temp_2 = self.state[2][8]

            # Front Face 
            self.state[0][6] = self.state[3][6]
            self.state[0][7] = self.state[3][7]
            self.state[0][8] = self.state[3][8]

            # Right Face 
            self.state[1][6] = self.state[0][6]
            self.state[1][7] = self.state[0][7]
            self.state[1][8] = self.state[0][8]

            # Back Face 
            self.state[2][6] = self.state[1][6]
            self.state[2][7] = self.state[1][7]
            self.state[2][8] = self.state[1][8]

            # Left Face 
            self.state[3][6] = temp_0
            self.state[3][7] = temp_1
            self.state[3][8] = temp_2
        # Side rotation
        else:

# Main
if __name__ == '__main__':

    cube = Cube()

    print(cube.state)