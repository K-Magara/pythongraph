import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Yu Mincho'

x = np.linspace(-np.pi*1.8, np.pi*1.8)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.xticks(np.arange(-5, 6, 1), color='None')
plt.yticks(color='None')
plt.xlim(-5, 5)
plt.ylim(-2.0, 2.0)
plt.grid(ls='--')
plt.axhline(0, c='lightgray')
plt.axvline(0, c='lightgray')
plt.tick_params(length=0)
plt.plot(x, np.sin(x), c='k', ls='-')

ax.text( 90*np.pi/180,  1.1, '山頂', fontsize=10)
ax.text(-90*np.pi/180, -1.2, '谷底', fontsize=10)
ax.arrow(90*np.pi/180, 1, 5, 0)

plt.show()
