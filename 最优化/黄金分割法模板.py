import numpy as np  # 黄金分割法
import matplotlib.pyplot as plt
from tabulate import tabulate

'''
def f(x):
    return 8*np.exp(1-x) + 7*np.log(x)


coordinates_x = np.linspace(1, 2.5)
coordinates_y = f(coordinates_x)
cooificient_p = 1 - 0.61803
bound_a, bound_b = 1, 2 # 输入区间范围
section_length = bound_b - bound_a
k = 0
table = [['迭代次数k', 'ak', 'bk', 'f(ak)', 'f(bk)', '新的区间'],
         [k, bound_a, bound_b, f(bound_a), f(bound_b), f'[{bound_a:.5f}, {bound_b:.5f}]']]

while section_length > 0.23: # 输入区间压缩停止时的大小
    next_a = bound_a + (bound_b - bound_a) * cooificient_p
    next_b = bound_b - (bound_b - bound_a) * cooificient_p
    copy_next_a = next_a
    copy_next_b = next_b
    if f(next_a) < f(next_b):
        bound_b = next_b
    else:
        bound_a = next_a
    section_length = bound_b - bound_a
    k += 1
    table.append([k, copy_next_a, copy_next_b, f(copy_next_a), f(copy_next_b),
                  f'[{bound_a:.5f}, {bound_b:.5f}]'])

print(tabulate(table, headers='firstrow', tablefmt='grid'))
# plt.plot(coordinates_x, coordinates_y)
# plt.show()
'''


def f(_x):
    return 1/2*np.transpose(_x)@np.array([[2, 1], [1, 2]])@_x


def f_d(_x):
    return _x.T@np.array([[2, 1], [1, 2]])


x0 = np.array([0.8, -0.25])
x0 = x0[:, np.newaxis]
gradient_x = f_d(x0).T

cooificient_p = 1 - 0.61803
bound_a, bound_b = 0.2, 0.8
section_length = bound_b - bound_a
k = 0
table = [['迭代次数k', 'ak', 'bk', 'f(ak)', 'f(bk)', '新的区间'],
         [k, bound_a, bound_b, f(x0+bound_a*-gradient_x), f(x0+bound_b*-gradient_x), f'[{bound_a:.5f}, {bound_b:.5f}]']]
nonuse_a, nonuse_b = 0, 0
while section_length > 0.01:
    next_a = bound_a + (bound_b - bound_a) * cooificient_p
    next_b = bound_b - (bound_b - bound_a) * cooificient_p
    copy_next_a = next_a
    copy_next_b = next_b
    if f(x0+next_a*-gradient_x) < f(x0+next_b*-gradient_x):
        bound_b = next_b
    else:
        bound_a = next_a
    section_length = bound_b - bound_a
    k += 1
    table.append([k, copy_next_a, copy_next_b, f(x0+copy_next_a*-gradient_x), f(x0+copy_next_b*-gradient_x),
                  f'[{bound_a:.5f}, {bound_b:.5f}]'])

print(tabulate(table, headers='firstrow', tablefmt='grid'))
print(x0+bound_a*-gradient_x)
print(x0+bound_b*-gradient_x)
