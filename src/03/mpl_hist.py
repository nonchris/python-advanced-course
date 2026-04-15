# copied en directly from the mpl docs
# but modified in some way or the other
import numpy as np
from matplotlib import pyplot as plt

mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')

# the histogram of the data
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist
n, bins, patches = ax.hist(x, bins=50, density=True, facecolor='C0', alpha=0.75)

ax.set_xlabel('Something on X')
ax.set_ylabel('Probability')
ax.set_title('A plot saying something')
# we can do TeX notation here!
ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
ax.axis([55, 175, 0, 0.03])
# enable the grid
ax.grid(True)

fig.show()
