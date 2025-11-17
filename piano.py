import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit
from fitting_functions import *

def linear(x, m, b):
    return m * x + b

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

data = np.loadtxt("piano_data.csv", delimiter=",", dtype=str)

t = data[1:, 0].astype(np.float32)
x = data[1:, 1].astype(np.float32)
h = data[1:, 2].astype(np.float32)

params, _ = curve_fit(linear, t, x)
m, b = params

print("x = {:.3f} t + {:.3f}".format(m, b))

plt.figure()
plt.scatter(t, x, label="Data")
plt.plot(t, linear(t, m, b), label="Linear Fit")
plt.xlabel("time (s)")
plt.ylabel("range (m)")
plt.legend(loc="best")
plt.title("Piano Range vs Time")
plt.savefig("piano_range_fit.png")
plt.close()

params, _ = curve_fit(quadratic, t, h)
a, bb, c = params

print("h = {:.3f} t^2 + {:.3f} t + {:.3f}".format(a, bb, c))

plt.figure()
plt.scatter(t, h, label="Data")
plt.plot(t, quadratic(t, a, bb, c), label="Quadratic Fit")
plt.xlabel("time (s)")
plt.ylabel("height (m)")
plt.legend(loc="best")
plt.title("Piano Height vs Time")
plt.savefig("piano_height_fit.png")
plt.close()

