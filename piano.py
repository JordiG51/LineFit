import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit
from fitting_functions import *

data = np.loadtxt("piano_data.csv", delimiter=",", dtype=str)

print(data[0])

t = data[1:, 0].astype(np.float32)
x = data[1:, 1].astype(np.float32)
h = data[1:, 2].astype(np.float32)

print("t =", t)
print("x =", x)
print("h =", h)

# Linear fit (x vs t)
params, params_cov = curve_fit(linear, t, x)
m = params[0]
b = params[1]
print(f"x = {m:.3f} t + {b:.3f}")

plt.figure()
plt.scatter(t, x)
plt.plot(t, linear(t, m, b))
plt.xlabel("Time (s)")
plt.ylabel("Range (m)")
plt.title("Piano Range vs Time (Linear Fit)")
plt.savefig("piano_linear_fit.png")
plt.close()

# Quadratic fit (h vs t)
params, params_cov = curve_fit(quadratic, t, h)
a = params[0]
bb = params[1]
c = params[2]
print(f"h = {a:.3f} t^2 + {bb:.3f} t + {c:.3f}")

plt.figure()
plt.scatter(t, h)
plt.plot(t, quadratic(t, a, bb, c))
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Piano Height vs Time (Quadratic Fit)")
plt.savefig("piano_quadratic_fit.png")
plt.close()

# Discussion comment
# Compared to the cannonball, the piano has much more drag.
# This makes the linear fit for range worse and the quadratic fit for height less accurate.
