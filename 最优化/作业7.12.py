import numpy as np
from tabulate import tabulate


def f(_x):
    return 1/2*np.transpose(_x)@np.array([[2, 1], [1, 2]])@_x


def f_d(_x):
    return _x.T@np.array([[2, 1], [1, 2]])


x0 = np.array([0.8, -0.25])
x0 = x0[:, np.newaxis]
gradient_x = f_d(x0).T
a0, a1, a2 = 0, 0.1, 0.2
while True:
    if f(x0+a1*-gradient_x) < f(x0+a0*-gradient_x) and f(x0+a1*-gradient_x) < f(x0+a2*-gradient_x):
        print(f'[{a0}, {a2}]')
        break
    elif f(x0+a1*-gradient_x) < f(x0+a0*-gradient_x) and f(x0+a1*-gradient_x) > f(x0+a2*-gradient_x):
        next_a = a2 + 2 * (a2 - a1)
        a0 = a1
        a1 = a2
        a2 = next_a
        continue
    elif f(x0+a1*-gradient_x) > f(x0+a0*-gradient_x):
        next_a = (a1 + a0) / 2
        a2 = a1
        a1 = next_a
        continue
print(gradient_x)
