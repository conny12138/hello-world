import numpy as np
from itertools import combinations


'''
A = np.array([[0.03, 0.08, 0.16, 0.04, -1, 0, 0],
              [0.06, 0.46, 0.09, 0.09, 0, -1, 0],
              [0.2, 0.05, 0.04, 0, 0, 0, -1],
              [1, 1, 1, 1, 0, 0, 0]])
b = np.array([20, 20, 50, 1000])[:, np.newaxis]
for i in combinations(range(7), 4):
    X = A[:, i]
    if np.linalg.matrix_rank(X) != 4:
        print('rank not right')
        continue
    else:
        # print(i, np.linalg.inv(X) @ b)
        x = np.linalg.inv(X) @ b
        x1 = np.array([0 for j in range(7)])[:, np.newaxis]
        x1[i, :] = x  # x1才是不动自变量位置的原方程的解
        if all(x1 >= 0):
            x0 = np.array([2, 4, 1, 2, 0, 0, 0])[np.newaxis, :]
            print(x1, x0 @ x1, '###########')
'''


A = np.array([[5, 6, -1, 0],
              [3, 2, 0, -1]])
b = np.array([30, 12])[:, np.newaxis]
for i in combinations(range(4), 2):
    X = A[:, i]
    if np.linalg.matrix_rank(X) != 2:
        print('rank not right')
        continue
    else:
        # print(i, np.linalg.inv(X) @ b)
        x = np.linalg.inv(X) @ b
        x1 = np.array([0 for j in range(4)])[:, np.newaxis]
        x1[i, :] = x  # x1才是不动自变量位置的原方程的解
        if all(x1 >= 0):
            x0 = np.array([1, 5, 0, 0])[np.newaxis, :]
            print(x1, x0 @ x1, '###########')

x0 = np.array([1, 5, 0, 0])[np.newaxis, :]
x1 = np.array([2, 100, 0, 0])[:, np.newaxis]
print(x1, x0 @ x1, '###########')