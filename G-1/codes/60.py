import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
strain = [0, 1, 4]  # Strain in %
stress = [0, 0.8, 0.82]  # Stress in GPa

# Plotting the data
plt.figure(figsize=(8, 4))
plt.plot(strain, stress, marker='o', color='blue', linewidth=2)

# Adding a large 'x' marker at the last point
plt.plot(strain[-1], stress[-1], 'kx', markersize=15, markeredgewidth=2)

# Labels and grid
plt.xlabel("Strain, %")
plt.ylabel("Stress, GPa")
plt.xticks(np.arange(0, 6, 1))
plt.yticks(np.arange(0, 1.2, 0.2))
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Displaying the plot
plt.tight_layout()
plt.show()

