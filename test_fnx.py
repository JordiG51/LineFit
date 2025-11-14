# test_fxn.py
from fitting_functions import *

# Test 1
print("Test 1: linear(2, 3, 4)")
print("Expected:", 10)
print("Got:", linear(2, 3, 4))
print()

# Test 2
print("Test 2: slope_units('meters', 'kg')")
print("Expected:", "kg/meter")
print("Got:", slope_units('meters', 'kg'))
print()

print("Test 3: slope_units('sec', 'meters')")
print("Expected:", "meter/sec")
print("Got:", slope_units('sec', 'meters'))
print()

# Test 3
print("Test 4: print_equation(4, 1, 'meters', 'kg')")
print_equation(4, 1, 'meters', 'kg')
