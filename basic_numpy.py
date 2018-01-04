import numpy as np

A = np.matrix([[1,0],[8,2]])
B = np.matrix([[3,2],[4,6]])
C = A*B
print(C)
deter = np.linalg.det(A)
print(deter)
