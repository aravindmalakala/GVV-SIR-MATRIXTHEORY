import numpy as np
import matplotlib.pyplot as plt

# Define the value of 'a'
data = np.loadtxt('values.tex', delimiter=':', dtype=str, comments='%')
a = float(data[1][1].strip())  # Set the value of 'a' here

# Create theta values for the full circle
theta = np.linspace(0, 2 * np.pi, 100)

# Parametric equations for the circle
x_values_circle = a * np.cos(theta)
y_values_circle = a * np.sin(theta)

# Create the vertical line x = a/sqrt(2)
x_line = a / np.sqrt(2)

# Define Riemann sum parameters
n = 1000  # Number of rectangles
x_r = np.linspace(x_line, a, n)  # x values from a/sqrt(2) to a
dx = x_r[1] - x_r[0]  # Width of each rectangle

# Corresponding y values for the circle (upper half)
y_upper = np.sqrt(a**2 - x_r**2)  # y = sqrt(a^2 - x^2)

# Corresponding y values for the circle (lower half)
y_lower = -np.sqrt(a**2 - x_r**2)  # y = -sqrt(a^2 - x^2)

# Create the plot
plt.figure(figsize=(10, 10))

# Plot the circle
plt.plot(x_values_circle, y_values_circle, label='$x^2 + y^2 = a^2$', color='blue')

# Shade the area using Riemann sum for the upper minor arc
plt.fill_between(x_r, y_upper, 0, color='lightblue', alpha=0.5, label='Shaded Upper Minor Arc Area ')

# Shade the area below the arc
plt.fill_between(x_r, y_lower, 0, color='lightblue', alpha=0.5)

# Plot the vertical line
plt.plot([x_line, x_line], [-a, a], label='$x = \\frac{a}{\\sqrt{2}}$', color='red', linestyle='--')

# Add x-axis and y-axis
plt.axhline(0, color='black', linewidth=1.2)  # X-axis
plt.axvline(0, color='black', linewidth=1.2)  # Y-axis

# Set the limits of the plot
plt.xlim(-a - 1, a + 1)
plt.ylim(-a - 1, a + 1)

# Add labels and title
plt.title('Circle, Vertical Line, and Shaded Areas ')
plt.xlabel('X-axis (x)')
plt.ylabel('Y-axis (y)')
plt.grid()
plt.axis('equal')  # Set equal scaling for x and y axes
plt.legend()

# Show the plot
plt.show()

