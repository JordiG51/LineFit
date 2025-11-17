import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit
from fitting_functions import *


def linear(x, m, b):
    return m * x + b

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c


data = np.loadtxt("cannon.csv", delimiter=",", dtype=str)

print(data[0])

t = data[1:, 0].astype(np.float32)
x = data[1:, 1].astype(np.float32)
h = data[1:, 2].astype(np.float32)

print("t =", t)
print("x =", x)
print("h =", h)


params, _ = curve_fit(linear, t, x)
slope = params[0]
intercept = params[1]

print("x = {:.3f} t + {:.3f}".format(slope, intercept))

plt.figure()
plt.scatter(t, x, label="Data")
plt.plot(t, linear(t, slope, intercept), label="Linear Fit")
plt.xlabel("time (s)")
plt.ylabel("range (m)")
plt.legend(loc="best")
plt.title("Cannonball Range vs Time")
plt.savefig("cannon_range_fit.png")
plt.close()


params, _ = curve_fit(quadratic, t, h)
a, b, c = params

print("h = {:.3f} t^2 + {:.3f} t + {:.3f}".format(a, b, c))

plt.figure()
plt.scatter(t, h, label="Data")
plt.plot(t, quadratic(t, a, b, c), label="Quadratic Fit")
plt.xlabel("time (s)")
plt.ylabel("height (m)")
plt.legend(loc="best")
plt.title("Cannonball Height vs Time")
plt.savefig("cannon_height_fit.png")
plt.close()
