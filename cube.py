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


    # Scramble the cube
    def CreateScramble (self):
        move_list = ['R','L','F','B','U','D','r','l','f','b','u','d',]
        new_scramble = []
        for x in range(0, 30):
            new_scramble.append(random.choice(move_list))

    # # Rotate face handler
    # def rotate_face(self, face):

    # Rotate face clockwise
    def rotate_clockwise(self, face):
        # Rotate pieces on face
        self.state[face] = [self.state[face][6],self.state[face][3],self.state[face][0],
                            self.state[face][7],self.state[face][4],self.state[face][1],
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

            # Back Face 
            self.state[2][6] = self.state[1][6]
            self.state[2][7] = self.state[1][7]
            self.state[2][8] = self.state[1][8]

            # Right Face 
            self.state[1][6] = self.state[0][6]
            self.state[1][7] = self.state[0][7]
            self.state[1][8] = self.state[0][8]

            # Front Face 
            self.state[0][6] = self.state[3][6]
            self.state[0][7] = self.state[3][7]
            self.state[0][8] = self.state[3][8]

            # Left Face 
            self.state[3][6] = temp_0
            self.state[3][7] = temp_1
            self.state[3][8] = temp_2        
        # Side rotation
        else:
            front = (face+3) % 4
            back = (face+1) % 4
            if face == 0:
                # Temp Front Face
                temp_0 = self.state[front][8]
                temp_1 = self.state[front][5]
                temp_2 = self.state[front][2]

                # Front Face 
                self.state[front][2] = self.state[5][0]
                self.state[front][5] = self.state[5][1]
                self.state[front][8] = self.state[5][2]

                # Bottom Face 
                self.state[5][0] = self.state[back][6]
                self.state[5][1] = self.state[back][3]
                self.state[5][2] = self.state[back][0]

                # Back Face 
                self.state[back][0] = self.state[4][6]
                self.state[back][3] = self.state[4][7]
                self.state[back][6] = self.state[4][8]

                # Top Face 
                self.state[4][6] = temp_0
                self.state[4][7] = temp_1
                self.state[4][8] = temp_2
            elif face == 1:
                # Temp Front Face
                temp_0 = self.state[front][2]
                temp_1 = self.state[front][5]
                temp_2 = self.state[front][8]

                # Front Face 
                self.state[front][2] = self.state[5][2]
                self.state[front][5] = self.state[5][5]
                self.state[front][8] = self.state[5][8]

                # Bottom Face 
                self.state[5][2] = self.state[back][6]
                self.state[5][5] = self.state[back][3]
                self.state[5][8] = self.state[back][0]

                # Back Face 
                self.state[back][0] = self.state[4][8]
                self.state[back][3] = self.state[4][5]
                self.state[back][6] = self.state[4][2]

                # Top Face 
                self.state[4][2] = temp_0
                self.state[4][5] = temp_1
                self.state[4][8] = temp_2
            elif face == 2:
                # Temp Front Face
                temp_0 = self.state[front][2]
                temp_1 = self.state[front][5]
                temp_2 = self.state[front][8]

                # Front Face 
                self.state[front][2] = self.state[5][8]
                self.state[front][5] = self.state[5][7]
                self.state[front][8] = self.state[5][6]

                # Bottom Face 
                self.state[5][6] = self.state[back][0]
                self.state[5][7] = self.state[back][3]
                self.state[5][8] = self.state[back][6]

                # Back Face 
                self.state[back][0] = self.state[4][2]
                self.state[back][3] = self.state[4][1]
                self.state[back][6] = self.state[4][0]

                # Top Face 
                self.state[4][0] = temp_0
                self.state[4][1] = temp_1
                self.state[4][2] = temp_2
            else:
                # Temp Front Face
                temp_0 = self.state[front][8]
                temp_1 = self.state[front][5]
                temp_2 = self.state[front][2]

                # Front Face 
                self.state[front][2] = self.state[5][6]
                self.state[front][5] = self.state[5][3]
                self.state[front][8] = self.state[5][0]

                # Bottom Face 
                self.state[5][0] = self.state[back][0]
                self.state[5][3] = self.state[back][3]
                self.state[5][6] = self.state[back][6]

                # Back Face 
                self.state[back][0] = self.state[4][0]
                self.state[back][3] = self.state[4][3]
                self.state[back][6] = self.state[4][6]

                # Top Face 
                self.state[4][0] = temp_0
                self.state[4][3] = temp_1
                self.state[4][6] = temp_2
            

    # Rotate face counter-clockwise (Prime)
    def rotate_prime(self, face):
        # Rotate pieces on face
        self.state[face] = [self.state[face][2],self.state[face][5],self.state[face][8],
                            self.state[face][1],self.state[face][4],self.state[face][7],
                            self.state[face][0],self.state[face][3],self.state[face][6]]    
    
        # Rotate pieces along edge of face
        # If U face rotation
        if face == 4:
            # Temp Front Face
            temp_0 = self.state[2][0]
            temp_1 = self.state[2][1]
            temp_2 = self.state[2][2]

            # Back Face 
            self.state[2][0] = self.state[1][0]
            self.state[2][1] = self.state[1][1]
            self.state[2][2] = self.state[1][2]

            # Right Face 
            self.state[1][0] = self.state[0][0]
            self.state[1][1] = self.state[0][1]
            self.state[1][2] = self.state[0][2]

            # Front Face 
            self.state[0][0] = self.state[3][0]
            self.state[0][1] = self.state[3][1]
            self.state[0][2] = self.state[3][2]

            # Left Face 
            self.state[3][0] = temp_0
            self.state[3][1] = temp_1
            self.state[3][2] = temp_2
        # If D face rotation
        elif face == 5:
            # Temp Back Face
            temp_0 = self.state[0][6]
            temp_1 = self.state[0][7]
            temp_2 = self.state[0][8]

            # Front Face 
            self.state[0][6] = self.state[1][6]
            self.state[0][7] = self.state[1][7]
            self.state[0][8] = self.state[1][8]

            # Right Face 
            self.state[1][6] = self.state[2][6]
            self.state[1][7] = self.state[2][7]
            self.state[1][8] = self.state[2][8]

            # Back Face 
            self.state[2][6] = self.state[3][6]
            self.state[2][7] = self.state[3][7]
            self.state[2][8] = self.state[3][8]

            # Left Face 
            self.state[3][6] = temp_0
            self.state[3][7] = temp_1
            self.state[3][8] = temp_2        
        # Side rotation
        else:
            front = (face+3) % 4
            back = (face+1) % 4
            if face == 0:
                # Temp Front Face
                temp_0 = self.state[back][0]
                temp_1 = self.state[back][3]
                temp_2 = self.state[back][6]

                # Back Face 
                self.state[back][0] = self.state[5][2]
                self.state[back][3] = self.state[5][1]
                self.state[back][6] = self.state[5][0]

                # Bottom Face 
                self.state[5][0] = self.state[front][2]
                self.state[5][1] = self.state[front][5]
                self.state[5][2] = self.state[front][8]

                # Front Face 
                self.state[front][2] = self.state[4][8]
                self.state[front][5] = self.state[4][7]
                self.state[front][8] = self.state[4][6]
                
                # Top Face 
                self.state[4][6] = temp_0
                self.state[4][7] = temp_1
                self.state[4][8] = temp_2
            elif face == 1:
                # Temp Front Face
                temp_0 = self.state[back][6]
                temp_1 = self.state[back][3]
                temp_2 = self.state[back][0]

                # Back Face 
                self.state[back][0] = self.state[5][8]
                self.state[back][3] = self.state[5][5]
                self.state[back][6] = self.state[5][2]

                # Bottom Face 
                self.state[5][2] = self.state[front][2]
                self.state[5][5] = self.state[front][5]
                self.state[5][8] = self.state[front][8]

                # Front Face 
                self.state[front][2] = self.state[4][2]
                self.state[front][5] = self.state[4][5]
                self.state[front][8] = self.state[4][8]
                
                # Top Face 
                self.state[4][2] = temp_0
                self.state[4][5] = temp_1
                self.state[4][8] = temp_2
            elif face == 2:
                # Temp Front Face
                temp_0 = self.state[back][6]
                temp_1 = self.state[back][3]
                temp_2 = self.state[back][0]

                # Back Face 
                self.state[back][0] = self.state[5][6]
                self.state[back][3] = self.state[5][7]
                self.state[back][6] = self.state[5][8]

                # Bottom Face 
                self.state[5][6] = self.state[front][8]
                self.state[5][7] = self.state[front][5]
                self.state[5][8] = self.state[front][2]

                # Front Face 
                self.state[front][2] = self.state[4][0]
                self.state[front][5] = self.state[4][1]
                self.state[front][8] = self.state[4][2]
                
                # Top Face 
                self.state[4][0] = temp_0
                self.state[4][1] = temp_1
                self.state[4][2] = temp_2
            else:
                # Temp Front Face
                temp_0 = self.state[back][0]
                temp_1 = self.state[back][3]
                temp_2 = self.state[back][6]

                # Back Face 
                self.state[back][0] = self.state[5][0]
                self.state[back][3] = self.state[5][3]
                self.state[back][6] = self.state[5][6]

                # Bottom Face 
                self.state[5][0] = self.state[front][8]
                self.state[5][3] = self.state[front][5]
                self.state[5][6] = self.state[front][2]

                # Front Face 
                self.state[front][2] = self.state[4][6]
                self.state[front][5] = self.state[4][3]
                self.state[front][8] = self.state[4][0]
                
                # Top Face 
                self.state[4][0] = temp_0
                self.state[4][3] = temp_1
                self.state[4][6] = temp_2

# Main
if __name__ == '__main__':

    cube = Cube()

    cube.rotate_clockwise(0)
    cube.rotate_clockwise(1)
    cube.rotate_clockwise(2)
    cube.rotate_clockwise(3)
    cube.rotate_prime(4)
    cube.rotate_prime(5)
    cube.rotate_prime(0)
    cube.rotate_prime(1)
    cube.rotate_prime(2)
    cube.rotate_prime(3)

    for x in cube.state:
        print("{0} {1} {2}\n{3} {4} {5}\n{6} {7} {8}\n".format( x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8] ))

    # Output should match below
    # B W R
    # G R B
    # O Y O

    # G W G
    # R G R
    # B O W

    # O W Y
    # Y O G
    # R B B

    # B O O
    # Y B R
    # R R G

    # R B Y
    # Y Y O
    # Y G Y

    # W B W
    # W W G
    # W O G
