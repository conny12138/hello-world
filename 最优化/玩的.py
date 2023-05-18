import numpy as np


a = np.array([1, 1/2])
print(a.shape)
a = a[np.newaxis, :]
print(a.shape)
print(a)
