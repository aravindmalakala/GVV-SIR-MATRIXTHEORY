import matplotlib.pyplot as plt

# Given values
a = 2
b = 2

# Points
A = (2 * a, 4)
B = (-2, 3 * b)
midpoint = (1, 2 * a + 1)

# Print values of a and b
print(f"The values are: a = {a}, b = {b}")

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(*A, 'ro', label='Point A (4, 4)')
plt.plot(*B, 'bo', label='Point B (-2, 6)')
plt.plot(*midpoint, 'go', label='Midpoint (1, 5)')

# Adding line segments
plt.plot([A[0], B[0]], [A[1], B[1]], 'k--', label='Line AB')

# Labels and legend
plt.text(A[0], A[1], 'A', fontsize=12, verticalalignment='bottom')
plt.text(B[0], B[1], 'B', fontsize=12, verticalalignment='bottom')
plt.text(midpoint[0], midpoint[1], 'Midpoint', fontsize=12, verticalalignment='bottom')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of Points and Midpoint')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()

