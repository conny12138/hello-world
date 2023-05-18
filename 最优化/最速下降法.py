# 找梯度，划界法，黄金分割法找出此方向的极小点
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


while np.linalg.norm(gradient_x) >= 10**-4:
    a0, a1, a2 = 0, 0.1, 0.2
    while True:
        if f(x0 + a1 * -gradient_x) < f(x0 + a0 * -gradient_x) and f(x0 + a1 * -gradient_x) < f(x0 + a2 * -gradient_x):
            # print(f'[{a0}, {a2}]')
            break
        elif f(x0 + a1 * -gradient_x) < f(x0 + a0 * -gradient_x) and f(x0 + a1 * -gradient_x) > f(x0 + a2 * -gradient_x):
            next_a = a2 + 2 * (a2 - a1)
            a0 = a1
            a1 = a2
            a2 = next_a
            continue
        elif f(x0 + a1 * -gradient_x) > f(x0 + a0 * -gradient_x):
            next_a = (a1 + a0) / 2
            a2 = a1
            a1 = next_a
            continue
    # 通过划界法找出了方向上的区间a0,a2

    bound_a, bound_b = a0, a2  # 开始黄金分割法，输入区间范围
    step = 0
    section_length = bound_b - bound_a
    cooificient_p = 1 - 0.61803
    while section_length > 10 ** -4:  # 输入区间压缩停止时的大小
        next_a = bound_a + (bound_b - bound_a) * cooificient_p
        next_b = bound_b - (bound_b - bound_a) * cooificient_p
        if f(x0 + next_a * -gradient_x) < f(x0 + next_b * -gradient_x):
            bound_b = next_b
        else:
            bound_a = next_a
        section_length = bound_b - bound_a
    step = (bound_b + bound_a) / 2

    x0 = x0 + step * -gradient_x
    gradient_x = f_d(x0)
    print(f'第次，点到了{x0}，值到了{f(x0)}')


