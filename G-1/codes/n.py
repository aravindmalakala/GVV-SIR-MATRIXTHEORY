import matplotlib.pyplot as plt
import numpy as np

# Define weight percentages of B and temperature ranges
weight_percentages = np.linspace(0, 100, 500)
solidus = 1100 + 4 * weight_percentages       # Approximation for the lower boundary
liquidus = 1300 + 2.5 * weight_percentages - 0.01 * weight_percentages ** 2  # Approximation for the upper boundary

# Plot the boundaries and regions
plt.figure(figsize=(10, 6))
plt.plot(weight_percentages, solidus, 'k-', label="Solidus Line")
plt.plot(weight_percentages, liquidus, 'k-', label="Liquidus Line")

# Fill regions
plt.fill_between(weight_percentages, solidus, 1000, where=(weight_percentages <= 100), color='lightblue', alpha=0.3, label="Solid")
plt.fill_between(weight_percentages, solidus, liquidus, where=(weight_percentages <= 100), color='lightcoral', alpha=0.3, label="Solid + Liquid")
plt.fill_between(weight_percentages, liquidus, 1500, where=(weight_percentages <= 100), color='lightyellow', alpha=0.3, label="Liquid")

# Add labels, grid, and title
plt.xlabel("Weight Percentage of B, %")
plt.ylabel("Temperature, °C")
plt.title("Binary Phase Diagram")
plt.xlim(0, 100)
plt.ylim(1000, 1500)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

