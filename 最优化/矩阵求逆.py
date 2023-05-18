import numpy as np


x = np.array([[6, 4], [4, 6]])
print(x.shape)
print(np.linalg.inv(x))

eigenvalue, featurevector = np.linalg.eig(mat)
