import numpy as np

# 1. Vector from 10 to 49
v1 = np.arange(10,50)
print("1.Vector:\n",v1)


# 2. 3x3 matrix from 0 to 8
m1 = np.arange(9).reshape(3,3)
print("\n2.Matrix 3x3:\n",m1)


# 3. Identity matrix 3x3
identity = np.eye(3)
print("\n3.Identity Matrix:\n",identity)


# 4. 3x3x3 random array
arr3d = np.random.random((3,3,3))
print("\n4.3x3x3 Random Array:\n",arr3d)


# 5. 10x10 random array min and max
arr10 = np.random.random((10,10))
print("\n5.Min:",arr10.min())
print("5.Max:",arr10.max())


# 6. Random vector size 30 mean
v2 = np.random.random(30)
print("\n6.Mean:",v2.mean())


# 7. Normalize 5x5 matrix
m2 = np.random.random((5,5))
normalized = (m2 - m2.min())/(m2.max()-m2.min())
print("\n7.Normalized Matrix:\n",normalized)


# 8. Multiply 5x3 and 3x2 matrices
A = np.random.random((5,3))
B = np.random.random((3,2))
product1 = np.dot(A,B)

print("\n8.Matrix Product 5x3 * 3x2:\n",product1)


# 9. Dot product of two 3x3 matrices
C = np.random.random((3,3))
D = np.random.random((3,3))

dot_product = np.dot(C,D)

print("\n9.Dot Product:\n",dot_product)


# 10. Transpose 4x4 matrix
M = np.random.random((4,4))
transpose = M.T

print("\n10.Transpose:\n",transpose)


# 11. Determinant of 3x3 matrix
M3 = np.random.random((3,3))

determinant = np.linalg.det(M3)

print("\n11.Determinant:",determinant)


# 12. A(3x4) * B(4x3)
A2 = np.random.random((3,4))
B2 = np.random.random((4,3))

product2 = np.dot(A2,B2)

print("\n12.A*B:\n",product2)


# 13. Matrix-vector product
M4 = np.random.random((3,3))
vector = np.random.random((3,1))

mv_product = np.dot(M4,vector)

print("\n13.Matrix-Vector Product:\n",mv_product)


# 14. Solve Ax=b
A3 = np.random.random((3,3))
b = np.random.random((3,1))

x = np.linalg.solve(A3,b)

print("\n14.Solution x:\n",x)


# 15. Row-wise and Column-wise sums
M5 = np.random.random((5,5))

row_sum = M5.sum(axis=1)
col_sum = M5.sum(axis=0)

print("\n15.Row sums:\n",row_sum)
print("\n15.Column sums:\n",col_sum)