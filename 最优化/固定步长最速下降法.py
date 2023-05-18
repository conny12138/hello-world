# 找梯度，固定步长法
import numpy as np
from tabulate import tabulate


def f(_x):
    a = 100*(_x[1]-_x[0]**2)**2 + (1-_x[0])**2
    return a


def f_d(_x):
    a = 100*(4*_x[0]**3-4*_x[0]*_x[1])+2*_x[0]-2
    b = 100*(2*_x[1]-2*_x[0]**2)
    return np.array([a, b])


x0 = np.array([0, 0])[:, np.newaxis]
gradient_x = f_d(x0)
step = 0.05

while np.linalg.norm(gradient_x) >= 10**-4:

    x0 = x0 + step * -gradient_x
    gradient_x = f_d(x0)
    print(f'第次，点到了{x0}，值到了{f(x0)}')


