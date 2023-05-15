#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
from copy import deepcopy

class Matrix:
    
    # Constructor to initialize the matrix with random integers
    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.nrows = nrows
        self.ncols = ncols
        # Use list comprehension to initialize the matrix with random integers
        self.matrix = [[random.randint(0, 10) for j in range(ncols)] for i in range(nrows)]

    # Method to add two matrices    
    def add(self, m):
        """return a new Matrix object after summation"""
        # Check two matrices are in the same size
        if self.nrows != m.nrows or self.ncols != m.ncols:
            print("Matrixs' size should be in the same size")
            return None
        # Initialize a new matrix to store the result
        result = deepcopy(self)
        # Add the corresponding elements of the matrices
        for i in range(self.nrows):
            for j in range(self.ncols):
                result.matrix[i][j] += m.matrix[i][j]
        return result

    # Method to subtract two matrices
    def sub(self, m):
        """return a new Matrix object after substraction"""
        # Check two matrices are in the same size
        if self.nrows != m.nrows or self.ncols != m.ncols:
            print("Matrixs' size should be in the same size")
            return None
        # Initialize a new matrix to store the result
        result = deepcopy(self)
        # Subtract the corresponding elements of the matrices
        for i in range(self.nrows):
            for j in range(self.ncols):
                result.matrix[i][j] -= m.matrix[i][j]
        return result

    # Method to multiply two matrices
    def mul(self, m):
        """return a new Matrix object after multiplication"""
        # Check if the nrows of m is the same as ncols of self
        if self.ncols != m.nrows:
            print("Cannot multiply two matrixs with size ({}, {}) and ({}, {})".format(self.nrows, self.ncols, m.nrows, m.ncols))
            return None
        # Initialize a new matrix to store the result
        result = Matrix(self.nrows, m.ncols)
        # Perform matrix multiplication
        for i in range(self.nrows):
            for j in range(m.ncols):
                result.matrix[i][j] = sum([self.matrix[i][k] * m.matrix[k][j] for k in range(self.ncols)])
        return result

    # Method to transpose the matrix
    def transpose(self):
        """return a new Matrix object after transpose"""
        # Initialize a new matrix to store the transposed matrix
        result = Matrix(self.ncols, self.nrows)
        # Transpose the matrix
        for i in range(self.nrows):
            for j in range(self.ncols):
                result.matrix[j][i] = self.matrix[i][j]
        return result
    
    # Method to display the matrix
    def display(self):
        """Display the content in the matrix"""
        for i in range(self.nrows):
            for j in range(self.ncols):
                print(self.matrix[i][j], end=" ")
            print()
        print()
        
a_rows = int(input("Enter A matrix's rows:"))
a_cols = int(input("Enter A matrix's cols:"))
print("Matrix A({}, {}):".format(a_rows, a_cols))
A = Matrix(a_rows, a_cols)
A.display()

b_rows = int(input("Enter B matrix's rows:"))
b_cols = int(input("Enter B matrix's cols:"))
print("Matrix B({}, {}):".format(b_rows, b_cols))
B = Matrix(b_rows, b_cols)
B.display()

print("="*10, "A + B", "="*10)
result = A.add(B)
if result is not None:
    result.display()

print("="*10, "A - B", "="*10)
result = A.sub(B)
if result is not None:
    result.display()

print("="*10, "A * B", "="*10)
result = A.mul(B)
if result is not None:
    result.display()
    
print("="*5, "the transpose of A*B", "="*5)
result = result.transpose()
if result is not None:
    result.display()

