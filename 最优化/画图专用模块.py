import numpy as np
import matplotlib.pyplot as plt

'''
def f(x):
    return 8*np.exp(1-x) + 7*np.log(x)


coordinates_x = np.linspace(1, 2.5)
coordinates_y = f(coordinates_x)
plt.plot(coordinates_x, coordinates_y)
plt.show()
'''


def f(_x):
    return 1/2*np.transpose(_x)@np.array([[2, 1], [1, 2]])@_x


def f_d(_x):
    return _x.T@np.array([[2, 1], [1, 2]])


x0 = np.array([0.8, -0.25])
x0 = x0[:, np.newaxis]
gradient_x = f_d(x0).T
coordinates_x = np.linspace(0.3, 0.6)
coordinates_y = np.array([])
for i in coordinates_x:
    coordinates_y = np.append(coordinates_y, f(x0 + i*-gradient_x))
#print(coordinates_y)
plt.plot(coordinates_x, coordinates_y)
plt.show()
