import sys
import numpy as np
import matplotlib.pyplot as plt

# Path to external scripts (ensure the path is correct)
sys.path.insert(0, '/home/malakala/Desktop/GVV-SIR-MATRIXTHEORY/matgeo/codes/CoordGeo')

# Local imports (ensure these modules exist and are correct)
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Direction vector - Given points
A = np.array([-7/3, 5])
B = np.array([2/3, 5])
colors = np.arange(1, 3)

# Labeling the coordinates
quad_coords = np.vstack([A, B])

# Calculate distance between A and B
distance_AB = np.linalg.norm(B - A)

# Plotting
plt.scatter(quad_coords[:, 0], quad_coords[:, 1], c=colors, cmap='viridis', label=['A', 'B'])
plt.plot([A[0], B[0]], [A[1], B[1]], 'k-', color='red', label='Line Segment AB')  # Add line segment

# Annotate the points
vert_labels = ['A', 'B']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({quad_coords[i, 0]:.2f}, {quad_coords[i, 1]:.2f})',
                 (quad_coords[i, 0], quad_coords[i, 1]), 
                 textcoords="offset points",
                 xytext=(-10, -5), 
                 ha='right')

# Customize axes
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlabel('$X$-Axis')
plt.ylabel('$Y$-Axis')
plt.grid(True)
plt.axis('equal')
plt.title(f'Calculating the distance AB: {distance_AB:.2f}', loc='right', pad=15)
plt.legend()  # Add legend to differentiate points and line segment
plt.show()

