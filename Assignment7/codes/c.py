import sys                                          # for path to external scripts
sys.path.insert(0, '/home/malakala/Desktop/GVV-SIR-MATRIXTHEORY/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define points for the line
x_values = np.linspace(-5, 10, 100)
y_values = (6 - x_values) / 2  # Rearranged line equation: y = (6 - x) / 2

# Create a figure
plt.figure(figsize=(8, 6))

# Plot the line
plt.plot(x_values, y_values, label='Line: $x + 2y = 6$', color='cyan')

# Define the direction vector and normal vector
data = np.genfromtxt('output.dat', delimiter=' ', names=True)
x = data['d']
y = data['n']
direction_vector = np.array([x[0],x[1]])  
normal_vector = np.array([y[0], y[1]])
origin = np.array([0, 3])  
# Plot the direction vector
plt.quiver(*origin, *direction_vector, angles='xy', scale_units='xy', scale=1, color='green', label='Direction Vector')

# Plot the normal vector
plt.quiver(*origin, *normal_vector, angles='xy', scale_units='xy', scale=1, color='blue', label='Normal Vector')

# Set limits and labels
plt.xlim(-5, 10)
plt.ylim(-5, 10)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')

# Set labels and title
plt.xlabel('$X$-Axis')
plt.ylabel('$Y$-Axis')
plt.title('Plot of the Line: $x + 2y = 6$ with Direction and Normal Vectors')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

