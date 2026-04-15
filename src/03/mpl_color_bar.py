import numpy as np
import matplotlib.pyplot as plt

# setup some generic data
N = 37
# https://numpy.org/doc/stable/reference/generated/numpy.mgrid
x_dir, y_dir = np.mgrid[:N, :N]

# keep in mind that we add arrays here
val_map = (np.cos(x_dir * 0.2) + np.sin(y_dir * 0.3))
print(val_map.shape)

# mask out the negative and positive values, respectively
# np.ma.masked marks a value as masked out
# https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked
# Z[Z < 0] = np.ma.masked

fig, ax1 = plt.subplots()

# plot the data and save the
# color "mappable" object returned by ax1.imshow
ax_image = ax1.imshow(val_map, cmap='plasma', interpolation='none')

# add the colorbar using the figure's method,
# telling which mappable we're talking about and
# which axes object it should be near
cbar = fig.colorbar(ax_image, ax=ax1)

cbar.minorticks_on()
fig.tight_layout()
fig.show()
