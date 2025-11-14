import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *
from scipy.optimize import curve_fit

# Load data
data = np.loadtxt("cannon.csv", delimiter=",", dtype=str)

# Check first row
print(data[0])

# Create arrays
t = data[1:, 0].astype(np.float32)
x = data[1:, 1].astype(np.float32)
h = data[1:, 2].astype(np.float32)

print("t =", t)
print("x =", x)
print("h =", h)

# ========= Linear fit of x vs t =========
params, params_cov = curve_fit(linear, t, x)
m = params[0]
b = params[1]

print(f"x = {m:.3f} t + {b:.3f}")

# Plot linear fit
plt.figure()
plt.scatter(t, x)
plt.plot(t, linear(t, m, b))
plt.xlabel("Time (s)")
plt.ylabel("Range (m)")
plt.title("Cannonball Range vs Time (Linear Fit)")
plt.savefig("cannon_linear_fit.png")
plt.close()

### EXERCISE 1
# ========= Quadratic fit of h vs t =========
params, params_cov = curve_fit(quadratic, t, h)
a = params[0]
b = params[1]
c = params[2]

print(f"h = {a:.3f} t^2 + {b:.3f} t + {c:.3f}")

# Plot quadratic fit
plt.figure()
plt.scatter(t, h)
plt.plot(t, quadratic(t, a, b, c))
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Cannonball Height vs Time (Quadratic Fit)")
plt.savefig("cannon_quadratic_fit.png")
plt.close()

### EXERCISE 2
# Do this in piano.py (see next file)
