from fitting_functions import *

#Test1
print("Testing linear(m, x, b):")
print("Expected 10 →", linear(2, 3, 4))
print()

#Test2
print("Testing slope_units(x_units, y_units):")
print("meters, kg →", slope_units("meters", "kg"))   
print("sec, meters →", slope_units("sec", "meters")) 
print()

#Test2
print("Testing print_equation():")
print_equation(4, 1, "kg", "meters")
