from sympy import *

# M = Matrix([[1, 0, 1, 3, 6], [2, 3, 4, 7, 8]])
# 1.00 0.00 1.00 3.00 6.00
# 0.00 3.00 2.00 1.00 -4.00

# input
print("Enter number of rows and columns")
m, n = map(int, input().split())  # m = row and n = column
M = []
for _ in range(m):
    row = list(map(int, input().split()))[:n]
    M.append(row)
matrix = Matrix(M)
# print("Matrix:", matrix)

# Use sympy.rref() method
M_rref = matrix.rref()

print("the echelon form of the matrix is", M_rref)
