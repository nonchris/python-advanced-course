import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

file_name = "wallpaper"  # base name of the file
dpi = 650                # resolution
edge_color = "#FF0050"   # color of the logo
scale_factor = 1.55      # how large shall it be?
landscape = True         # landscape or portrait mode?

# https://www.omnicalculator.com/other/pixel-aspect-ratio
# .6 for 16/9
# .5 for 16/10
# for ios:
# deliberately too long to it can be shifted while centered
# short: (-0.46, .46)
# long: (-1.2, 1.2)
proportions_short_side = (-0.6, .6)
# can stay untouched most of the time
proportions_long_side = (-1, 1)


# set background to black
plt.style.use('dark_background')

# create a figure and axes
ax: plt.Axes
fig, ax = plt.subplots()

# set canvas so that (0, 0) is the center
# current aspect ratio: 16/9
# y = 0.5 for 16/10
if landscape:
    ax.set_xlim(*proportions_long_side)
    ax.set_ylim(*proportions_short_side)
    img_name = f"{file_name}-'horizontal'.png"

else:
    ax.set_xlim(*proportions_short_side)
    ax.set_ylim(*proportions_long_side)
    img_name = f"{file_name}-vertical.png"


# set aspect ratio to be equal
ax.set_aspect('equal')
# set limits and remove ticks
ax.axis('off')

# used for patches that need a center as reference
center = (0, 0)

# kwargs that are passed to every patch
style_kwargs = {
    "facecolor": "black",
    "edgecolor": edge_color,
    "linewidth": 5.0
}

# create circles
circle_inner = patches.Circle(center, 0.2 * scale_factor, **style_kwargs)

circle_outer = patches.Circle(center, 0.35 * scale_factor, **style_kwargs)

# create a triangle
# coords: left, mid, right
# we create them separately, so we can easily apply shift to both axis
x_points = np.array([-0.25, 0.0, 0.25]) * scale_factor
y_points = np.array([0.15, -0.3, 0.15]) * scale_factor

# combine to x-y-tuples
vertices = list(zip(x_points, y_points))

triangle = patches.Polygon(vertices, **style_kwargs)

# add patches in right order
ax.add_patch(circle_outer)
ax.add_patch(circle_inner)
ax.add_patch(triangle)

# finish off plot
fig.tight_layout()

# show the plot
plt.savefig(img_name, bbox_inches="tight", pad_inches=0, dpi=dpi)
print(f"Figure saved unter '{img_name}'")
fig.show()
