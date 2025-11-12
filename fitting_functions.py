def linear(m, x, b):
    return m * x + b


def slope_units(x_units, y_units):
    x_clean = x_units.rstrip('s')
    y_clean = y_units.rstrip('s')
    return f"{y_clean}/{x_clean}"


def print_equation(m, b, x_units, y_units):
    slope = slope_units(x_units, y_units)
    print(f"The equation of the line is: y = {m} {slope} x + {b} {y_units.rstrip('s')}")

