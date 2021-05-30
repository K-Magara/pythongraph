import numpy as np
import matplotlib.pyplot as plt

x = [i/10 for i in range(0, 101)]
y = [3*(i-4)**2+2 for i in x]

dx, dy = np.loadtxt("data.txt", unpack=True)

plt.plot(x, y, c='k', label='理論値')
plt.plot(dx, dy, 'o', c='k', mfc='w', label='測定値') # markerfacecolor

plt.xlabel('$\it{x}$ [mm]')
plt.ylabel('$\it{y}$ [mm]')
plt.legend(prop={"family":"Yu Mincho"})

plt.show()
