import sys                                          # for path to external scripts
sys.path.insert(0, '/home/malakala/Desktop/GVV-SIR-MATRIXTHEORY/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Given vector
data = np.genfromtxt('output.dat', delimiter=' ', names=True)
xx = data['X']

# Assuming we are working with a single vector
vector = np.array([xx[0], xx[1], xx[2]])

# Calculate the direction cosines
norm = LA.norm(vector)
direction_cosines = vector / norm

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the vector
origin = np.array([0, 0, 0])
ax.quiver(*origin, *vector, color='b', arrow_length_ratio=0.1)  # Plot the vector

# Add text for direction cosines
ax.text(vector[0], vector[1], vector[2], 
        f'Direction Cosines:\n({direction_cosines[0]:.2f}, {direction_cosines[1]:.2f}, {direction_cosines[2]:.2f})', 
        color='blue', fontsize=12)

# Set limits and aspect ratio
ax.set_xlim(-1, 1)  # Adjust limits based on your data
ax.set_ylim(-1, 1)  # Adjust limits based on your data
ax.set_zlim(-1, 1)  # Adjust limits based on your data
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio for x, y, and z axes

# Set labels and title
ax.set_xlabel('$X$-Axis')
ax.set_ylabel('$Y$-Axis')
ax.set_zlabel('$Z$-Axis')

plt.grid(True)
plt.title('Vector and its Direction Cosines', loc='right', pad=15)
plt.show()

