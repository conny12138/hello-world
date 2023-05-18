# 经典未改动的牛顿法求极小点
import numpy as np
from tabulate import tabulate


def f(_x):
    a = 100*(_x[1]-_x[0]**2)**2 + (1-_x[0])**2
    return a


def f_d(_x):
    a = 100*(4*_x[0]**3-4*_x[0]*_x[1])+2*_x[0]-2
    b = 100*(2*_x[1]-2*_x[0]**2)
    return np.array([a, b])


def f_d_d(_x):
    a = 2-400*(_x[1]-3*_x[0]**2)
    b = -400*_x[0]
    d = 200
    return np.array([[a, b], [b, d]], dtype='object')


x0 = np.array([0, 0])[:, np.newaxis]
gradient_x = f_d(x0)
hessian_x = f_d_d(x0).astype(np.float)

for i in range(2):
    x0 = x0 - np.linalg.inv(hessian_x)@gradient_x
    gradient_x = f_d(x0)
    hessian_x = f_d_d(x0).astype(np.float)
    print(x0)
