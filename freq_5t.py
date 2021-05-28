import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Yu Mincho'

x = np.linspace(-np.pi*5, np.pi*5, 200)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.xticks(np.arange(-5, 6, 1), c='None')
plt.yticks(c='None')
plt.xlim(-5, 5)
plt.ylim(-2.0, 2.0)
plt.grid(ls='--')
plt.axhline(0, c='lightgray')
plt.axvline(0, c='lightgray')
plt.tick_params(length=0)
plt.plot(x/np.pi, np.sin(x+np.pi)*1.25, c='k', ls='-')

ax.text(-1.5, -1.8, 'TIME/DIV = 1[msec]/cm', fontsize=10, backgroundcolor='w')

x = [-5, 5]
for n in x:
    ax.arrow(n, 2, 0, 0.5,  color='gray', clip_on=False)

x = [-3, -1, 1, 3]
for n in x:
    ax.arrow(n, 2, 0, 0.2,  color='gray', clip_on=False)

x = [-4, -2, 0, 2, 4]
i = 1
for n in x:
    ax.arrow(n+0.3, 2.1,  0.7, 0, head_width=0.08, length_includes_head=True, color='gray', clip_on=False)
    ax.arrow(n-0.2, 2.1, -0.8, 0, head_width=0.08, length_includes_head=True, color='gray', clip_on=False)
    ax.text(n-0.15, 2.05, str(i)+'T')
    i+=1

ax.arrow( 1.5, 2.4,  3.5, 0, head_width=0.08, length_includes_head=True, color='gray', clip_on=False)
ax.arrow(-1.5, 2.4, -3.5, 0, head_width=0.08, length_includes_head=True, color='gray', clip_on=False)
ax.text(-1.45, 2.35, '10cm = 10[msec] , 5T')

plt.show()
