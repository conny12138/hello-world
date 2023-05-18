import numpy as np


def f(_x):
    # a = (_x[1]-_x[0])**4+12*_x[0]*_x[1]-_x[0]+_x[1]-3
    a = 3*(1-_x[0])**2*np.exp(-_x[0]**2-(_x[1]+1)**2)-\
        10*(_x[0]/5-_x[0]**3-_x[1]**5)*np.exp(-_x[0]**2-_x[1]**2)-\
        np.exp(-(_x[0]+1)**2-_x[1]**2)/3
    return np.float(a)


def p(_k, _z, _x):
    t = 2/np.log(_k + 2)
    lst = [1, np.exp((-_z+_x)/t)]
    return np.min(lst)


a = 1
x0 = np.array([0, 0])[:, np.newaxis]
for k in range(10 * 6):
    z0 = a * (2 * np.random.rand(2, 1) - 1) + x0
    if np.random.rand(1) <= p(k, f(z0), f(x0)):
        x0 = z0

print(f(x0))