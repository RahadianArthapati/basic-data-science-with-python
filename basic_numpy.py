import numpy as np

A = np.matrix([[1,0],[8,2]])
B = np.matrix([[3,2],[4,6]])
C = A*B
# print(C)

# determinant
deter = np.linalg.det(A)
# print(deter)

# transpose
# In matrix transpose, rows become columns and columns should be rows.
m = np.matrix([[3,6,7],[2,7,9],[8,5,1]])
transpose = np.transpose(m)
print(transpose)

#inverse
inverse = np.linalg.inv(m)
print(inverse)

# solving simultaneous linear equations
x = np.linalg.solve(A,B)
print(x)

#eigenvalues and eigenvectors
eigvals = np.linalg.eig(A)
print(eigvals)

# expectation
numbers = [1, 2, 3, 4, 5, 6]
num_array = np.array(numbers)
exp = np.mean(num_array)
print(exp)

# mean, median, mode
from scipy import stats
data = np.array([3, 5, 9, 2, 7, 3, 6, 9, 3])
# Mean
dt_mean = np.mean(data);
print("Mean :", round(dt_mean, 2))
# Median
dt_median = np.median(data);
print("Median :", dt_median)
# Mode
dt_mode = stats.mode(data);
print("Mode :", dt_mode[0][0])