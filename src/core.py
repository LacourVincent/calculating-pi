import numpy as np
import matplotlib.pyplot as plt

N = 1000  # Number of points of the approximation
R = 1  # Radius of the circle

angles = np.linspace(0, 2 * np.pi, N+1)
points = [(R*np.cos(angle), R*np.sin(angle))
          for angle in angles]

distances = []
for i in range(len(points)-1):
    p1 = points[i]
    p2 = points[i + 1]
    distance = np.hypot(p2[0] - p1[0], p2[1] - p1[1])
    distances.append(distance)

pi = sum(distances) / (2 * R)
print("Value of PI : {}".format(pi))

x = [point[0] for point in points]
y = [point[1] for point in points]

plt.plot(x, y, ".")
plt.title(
    "Approximation of a circle using polygon with N = {}".format(N), fontsize=15)
plt.axis("equal")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
plt.close()
