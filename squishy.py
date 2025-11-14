import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit
from fitting_functions import *

data = np.loadtxt("data.csv", delimiter=",", dtype=str)

print(data[0])

x = data[1:, 0].astype(np.float32)
y = data[1:, 1].astype(np.float32)

print("x =", x)
print("y =", y)

params, params_cov = curve_fit(linear, x, y)
m = params[0]
b = params[1]

print_equation(m, b, "grams", "cm")

# Equation of the line: copy what printed here

plt.figure()
plt.scatter(x, y)
plt.plot(x, linear(x, m, b))
plt.xlabel("Mass (g)")
plt.ylabel("Height (cm)")
plt.title("Squishing a Marshmallow – Line Fit")
plt.savefig("marshmallow_fit.png")
plt.close()
