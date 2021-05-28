import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Yu Mincho'

x = np.linspace(-5, 5, 200)

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
plt.plot(x, np.sin(x*np.pi/4)*1.5, c='k', ls='-')
plt.plot(x, np.sin(x*np.pi/4+0.63)*1.5, c='k', ls='-')

ax.text(-1.5, 2.1, 'すすむ <<     >> おくれる')

ax.arrow(-4, 0, 0, -1.8, color='gray')
ax.arrow( 4, 0, 0, -1.8, color='gray')
ax.arrow( 1, -1.75,  3, 0, head_width=0.08, length_includes_head=True, color='gray')
ax.arrow(-1, -1.75, -3, 0, head_width=0.08, length_includes_head=True, color='gray')
ax.text(-0.7, -1.8, '360度 = 8div', fontsize=10, backgroundcolor='w')

ax.arrow(-0.8, 0, 0, 1, color='gray')
ax.text(-0.68, 0.7, '位相差', backgroundcolor='w')
ax.text(-0.68, 0.5, '0.8div', backgroundcolor='w')

ax.arrow(-3, 0.5, -1, -0.5, head_width=0.08, length_includes_head=True, color='gray')
ax.text( -3, 0.5, 'CH1=$\it{V_R}$', backgroundcolor='w')
ax.arrow(-3.3, 0.75, -1.5, -0.75, head_width=0.08, length_includes_head=True, color='gray')
ax.text( -3.3, 0.75, 'CH2=$\it{V}$',   backgroundcolor='w')

plt.show()
