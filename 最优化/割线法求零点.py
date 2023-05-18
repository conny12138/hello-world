import numpy as np
from tabulate import tabulate


def f(_x):
    return (2*_x-1)**2 + 4*(4-1024*_x)**4


def f_d(x):
    return 2*x - 4*np.sin(x)


x0, x1 = 0, 1
rho = 10**-5
gap = x1 - x0
times = 0
print(x1, 'AAAAAA', f(x1), times)
while gap > x1*rho:
    next_x = x1 - (x1-x0)/(f(x1)-f(x0))*f(x1)
    x0 = x1
    x1 = next_x
    gap = abs(x1 - x0)
    times += 1
    print(x1, 'AAAAAA', f(x1), times)
