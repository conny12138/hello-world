import numpy as np
from tabulate import tabulate
from matplotlib import pyplot as plt


def f(_x):
    a = (_x[1]-_x[0])**4+12*_x[0]*_x[1]-_x[0]+_x[1]-3
    return np.float(a)


def return_vector(number):
    if number == 2:
        return p2
    elif number == 1:
        return p1
    else:
        return p0


def draw(_p1, _p2, _p3):
    _A = np.hstack([_p1, _p2, _p3, _p1])
    x_axis_data = []
    y_axis_data = []
    for i in _A[0, :]:
        x_axis_data.append(i)
    for i in _A[1, :]:
        y_axis_data.append(i)
    plt.plot(x_axis_data, y_axis_data)
    return 0


# x_axis_data = []
# y_axis_data = []
plt.figure()
x0 = np.array([10, 2])[:, np.newaxis]
e1 = np.array([0, 1])[:, np.newaxis]
e2 = np.array([1, 0])[:, np.newaxis]
p0 = x0
p1 = p0 + e1
p2 = p0 + e2
sort_index = np.argsort(np.array([f(p0), f(p1), f(p2)]))
p_l = return_vector(sort_index[-1])
p_s = return_vector(sort_index[0])
p_nl = return_vector(sort_index[1])
draw(p0, p1, p2)

while abs(f(p_l) - f(p_s)) >= 1e-4:
    sort_index = np.argsort(np.array([f(p0), f(p1), f(p2)]))
    p_l = return_vector(sort_index[-1])
    p_s = return_vector(sort_index[0])
    p_nl = return_vector(sort_index[1])
    p_g = (p_nl + p_s) / 2
    p_r = p_g + (p_g - p_l)
    if f(p_s) <= f(p_r) < f(p_nl):
        p0 = p_s
        p1 = p_r
        p2 = p_nl
    elif f(p_r) < f(p_s):
        p_e = p_g + 2*(p_r - p_g)
        if f(p_e) < f(p_r):
            p_r = p_e
        p0 = p_r
        p1 = p_s
        p2 = p_nl
    elif f(p_r) >= f(p_nl):
        if f(p_r) < f(p_l):
            p_c = p_g + 0.5*(p_r - p_g)
            if f(p_c) <= f(p_l):
                p_r = p_c
        else:
            p_c = p_g + 0.5 * (p_l - p_g)
            if f(p_c) <= f(p_l):
                p_r = p_c
        if f(p_r) <= f(p_l):
            p0 = p_r
            p1 = p_s
            p2 = p_nl
        else:
            p0 = p_s
            p1 = p0 + 0.5*(p_nl - p_s)
            p2 = p0 + 0.5*(p_l - p_s)
    draw(p0, p1, p2)

# plt.plot(x_axis_data, y_axis_data)
plt.show()
#print(p_s, f(p_s))


