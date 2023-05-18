import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm  # numpy的画图往右为x正，往下为y正,画出来的图像以此为基准


y, x = np.ogrid[-2:2:200j, -2:2:200j]  # 变量的顺序要十分注意，不然就错了
z = x * np.exp(-x**2-y**2)
extent = [np.min(x), np.max(x), np.min(y), np.max(y)]

plt.imshow(z, extent=extent, cmap=cm.gray)
plt.colorbar()
plt.show()

