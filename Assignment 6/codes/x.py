import sys                                          # for path to external scripts
sys.path.insert(0, '/home/malakala/Desktop/GVV-SIR-MATRIXTHEORY/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# Local imports
from line.funcs import line_gen

# Given values
BC = 6  # Length of BC
angle_B = 30  # Angle B in degrees
AC_minus_AB = 4  # AC - AB = 4 cm

# Convert angle B to radians for calculations
angle_B_rad = np.radians(angle_B)

# Assume a position for point B
B = np.array([0, 0])  # Point B at origin
C = np.array([BC, 0])  # Point C at (6, 0)

# Prepare to plot multiple triangles for different lengths of AB
ab_values = np.linspace(1, 10, 10)  # Varying AB from 1 cm to 10 cm

# Create a figure for the plots
plt.figure(figsize=(10, 8))

for c_value in ab_values:
    # Calculate AC based on the condition AC - AB = 4
    b_value = c_value + AC_minus_AB  # AC

    # Using the Law of Cosines
    # b^2 = c^2 + BC^2 - 2*c*BC*cos(B)
    equation = Eq(b_value**2, c_value**2 + BC**2 - 2*c_value*BC*np.cos(angle_B_rad))
    
    # Solve for c if needed (for verification)
    # This step is not strictly necessary for plotting but good for validation
    solution = solve(equation, symbols('c'))

    # Calculate coordinates of point A
    A_x = c_value * np.cos(np.pi / 2 - angle_B_rad)  # x-coordinate of A
    A_y = c_value * np.sin(np.pi / 2 - angle_B_rad)  # y-coordinate of A
    A = np.array([A_x, A_y])

    # Generate lines for the triangle
    x_AC = line_gen(A, C)
    x_CB = line_gen(C, B)
    x_AB = line_gen(A, B)

    # Plot the triangle
    plt.plot(x_AC[0, :], x_AC[1, :], label=f'$AC$ (c={c_value:.1f} cm)')
    plt.plot(x_CB[0, :], x_CB[1, :], label='$CB$')
    plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')

    # Mark points A, B, C
    plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='red')
    plt.annotate('A', (A[0], A[1]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate('B', (B[0], B[1]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate('C', (C[0], C[1]), textcoords="offset points", xytext=(0,10), ha='center')

# Configure plot aesthetics
plt.xlabel('$x$ (cm)')
plt.ylabel('$y$ (cm)')
plt.title('Triangles for Varying Lengths of AB')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.axis('equal')
plt.legend()
plt.show()

