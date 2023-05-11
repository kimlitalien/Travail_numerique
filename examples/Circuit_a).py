import os
import sys

# Append module root directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

cartesian_variables = Symbol("x"), Symbol("y")
x, y = cartesian_variables
x_expression_vertical = 0 * x
y_expression_vertical = y
vertical_eqs = (x_expression_vertical, y_expression_vertical)

x_expression_horizontal = x
y_expression_horizontal = 0 * y
horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

WORLD_SHAPE = (101, 101)
BATTERY_VOLTAGE = 1.0
HIGH_WIRE_RESISTANCE = 1.0
LOW_WIRE_RESISTANCE = 0.01

