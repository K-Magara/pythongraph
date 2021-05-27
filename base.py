import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi*1.8, np.pi*1.8)

plt.xticks(np.arange(-5, 6, 1))
plt.grid(ls='dotted')
plt.axhline(0, c='lightgray')
plt.axvline(0, c='lightgray')
plt.xticks(color='None')
plt.yticks(color='None')
plt.tick_params(length=0)
plt.plot(x, np.sin(x), c='k', ls='-', label='sin')
plt.xlim(-5, 5)
plt.ylim(-2.0, 2.0)

plt.show()
