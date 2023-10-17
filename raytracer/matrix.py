import math
from raytracer.tuples import Tuple

class Matrix:

    def __init__(self, size, data):
        #size is one number bc we always want size by size matrices
        self.size = size
        #the data will be a 2d array
        if data:
            # You can check if the data is of correct shape here
            if len(data) == self.size and len(data[0]) == self.size:
                self.data = data
            else:
                raise ValueError("data does not match specified matrix size.")
        else:
            #otherwise make an empty size by size matrix
            self.data = [[0] * self.size for _ in range(self.size)]

    def __eq__(self, other):
        epsilon = 1e-5

        if self.size != other.size:
            return False
        for i in range(self.size):
            for j in range(self.size):
                if abs(self.data[i][j] - other.data[i][j]) > epsilon:
                    return False
        return True
        
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
        
    def transpose(self):
        new_data = [[0] * self.size for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                new_data[row][col] = self.data[col][row]
        return Matrix(self.size, new_data)
    
        
    def matrix_multiply(self, other):
        if self.size != 4 or other.size != 4:
            raise ValueError("Matrix multiplication is only for multiplying 4x4 matrices")
        
        data = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        #self rows
        for row in range(4):
            for col in range(4):
                data[row][col] = (self.data[row][0] * other.data[0][col] + 
                                  self.data[row][1] * other.data[1][col] + 
                                  self.data[row][2] * other.data[2][col] + 
                                  self.data[row][3] * other.data[3][col])
            
        return Matrix(4, data)
    
    def tuple_multiply(self, tuple):
        if self.size != 4:
            raise ValueError("matrix x tuple multiplication is only for 4x4 matrices")
        
        new_tuple_data = [0,0,0,0]
        for row in range(4):
            new_tuple_data[row] = (self.data[row][0] * tuple.x + 
                                   self.data[row][1] * tuple.y + 
                                   self.data[row][2] * tuple.z + 
                                   self.data[row][3] * tuple.w)

        return Tuple(new_tuple_data[0],new_tuple_data[1],new_tuple_data[2],new_tuple_data[3])


    def determinant(self):
        det = 0
        if self.size == 2:
            det = (self.data[0][0] * self.data[1][1]) - (self.data[0][1] * self.data[1][0])
        else:
            for col in range(self.size):
                det = det + self.data[0][col] * self.cofactor(0, col)
        return det

    def submatrix(self, row, col):
        new_data = []
        for i in range(self.size):
            if i != row:  # Skip the row to be removed
                new_row = []
                for j in range(self.size):
                    if j != col:  # Skip the column to be removed
                        new_row.append(self.data[i][j])
                new_data.append(new_row)
        return Matrix(len(new_data), new_data)
    
    def minor(self, row, col):
        s = self.submatrix(row, col)
        return s.determinant()
    
    def cofactor(self, row, col):
        if (row + col) % 2 == 0:
            return self.minor(row, col)
        else:
            return -self.minor(row, col)
        
    def is_invertible(self):
        return self.determinant() != 0
    
    def inverse(self):
        if not self.is_invertible():
            ValueError("Matrix has 0 determinant therefore not invertible")
            return
        det = self.determinant()
        inverse = Matrix(self.size, None)
        for row in range(self.size):
            for col in range(self.size):
                c = self.cofactor(row, col)
                inverse.data[col][row] = c / det

        return inverse

IDENTITY_DATA = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

IDENTITY = Matrix(4, IDENTITY_DATA)