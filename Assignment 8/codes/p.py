import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys  # for path to external scripts
sys.path.insert(0, '/home/malakala/Desktop/GVV-SIR-MATRIXTHEORY/matgeo/codes/CoordGeo')  # path to my scripts

# local imports
from conics.funcs import circ_gen
from line.funcs import *

# Load data from the .tex file
data = np.loadtxt('values.tex', delimiter=':', dtype=str, comments='%')
a1 = float(data[0][1].strip())  # Convert to float
a2 = float(data[1][1].strip())  # Convert to float

# New center points based on a1 and a2
O1 = np.array([2 * a1, a1 - 7]).reshape(-1, 1)
O2 = np.array([2 * a2, a2 - 7]).reshape(-1, 1)

# Additional point
point = np.array([11, -9]).reshape(-1, 1)

# New radius
r = 5 * np.sqrt(2)

# Generating circles
x_circ1 = circ_gen(O1, r)
x_circ2 = circ_gen(O2, r)

# Plotting the circles
plt.plot(x_circ1[0, :], x_circ1[1, :], label=f'Circle 1: Center {O1.flatten()}')
plt.plot(x_circ2[0, :], x_circ2[1, :], label=f'Circle 2: Center {O2.flatten()}')

# Plotting the additional point
plt.scatter(point[0], point[1], color='red', label='Point (11, -9)')
plt.annotate('A (11, -9)', 
             (point[0], point[1]),  # this is the point to label
             textcoords="offset points",  # how to position the text
             xytext=(-20, 5),  # distance from text to points (x, y)
             ha='center')  # horizontal alignment can be left, right or center

# Labeling the coordinates for the centers
colors = np.arange(1, 3)
tri_coords = np.block([O1, O2])
plt.scatter(tri_coords[0, :], tri_coords[1, :], c=colors)
vert_labels = ['$\mathbf{O_1}$', '$\mathbf{O_2}$']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[0, i]:.0f}, {tri_coords[1, i]:.0f})',
                 (tri_coords[0, i], tri_coords[1, i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(-20, 5),  # distance from text to points (x, y)
                 ha='center')  # horizontal alignment can be left, right or center

# Use set_position for axis aesthetics
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Set the aspect ratio to be equal
plt.axis('equal')

plt.legend(loc='best')
plt.grid()  # minor
plt.show()

