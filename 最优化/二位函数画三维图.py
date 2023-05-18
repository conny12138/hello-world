import numpy as np
import mpl_toolkits.mplot3d
from matplotlib import pyplot as plt
from matplotlib import cm

y, x = np.mgrid[-2:2:20j, -2:2:20j]
z = (y-x)**4+12*x*y-x+y-3
z = 3*(1-x)**2*np.exp(-x**2-(y+1)**2)-10*(x/5-x**3-y**5)*np.exp(-x**2-y**2)-\
        np.exp(-(x+1)**2-y**2)/3
# z = 1/5*x**2+y**2
# z = x - y

fig = plt.figure(figsize=(8, 6))
ax = fig.gca(projection='3d')
ax.plot_surface(x, y, z, cmap=cm.ocean)
plt.show()
