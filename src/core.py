import numpy as np
import matplotlib.pyplot as plt


def getPiFromPolygonalApproximation(N, R):
    angles = np.linspace(0, 2 * np.pi, N+1)
    points = [(R*np.cos(angle), R*np.sin(angle))
              for angle in angles]
    distances = []
    for i in range(len(points)-1):
        p1 = points[i]
        p2 = points[i + 1]
        distance = np.hypot(p2[0] - p1[0], p2[1] - p1[1])
        distances.append(distance)
    return sum(distances) / (2 * R)


def getPiFromGregoryLeibniz(N):
    pi = 1
    for i in range(1, N):
        pi += ((-1)**i)*1/(i*2 + 1)
    return 4*pi


def getPiFromNilakantha(N):
    pi = 3
    for i in range(1, N):
        pi += ((-1)**(i-1))*4/((2*i*(2*i+1)*(2*i+2)))
    return pi


def plotFigure(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.plot(x, y, ".")
    plt.title("Approximation of a circle using polygon with N = {}".format(
        len(points) - 1), fontsize=15)
    plt.axis("equal")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    plt.close()


piFromPolygonalApproximation = getPiFromPolygonalApproximation(1000, 1)
piFromGregoryLeibniz = getPiFromGregoryLeibniz(1000)
piFromNilakantha = getPiFromNilakantha(1000)

print("Polygonal Appproximation:")
print("π = {}".format(piFromPolygonalApproximation))

print("Gregory Leibniz Serie:")
print("π = {}".format(piFromGregoryLeibniz))

print("Nilakantha Serie:")
print("π = {}".format(piFromNilakantha))
