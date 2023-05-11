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

wires = [(Wire((26,26), (64, 26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)),
         (Wire((64,26), (74,26), horizontal_eqs, cartesian_variables,HIGH_WIRE_RESISTANCE)),
         (Wire((74,26), (76,26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)),
         (Wire((26,26), (26,76), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)),
         (Wire((76,26), (76,56), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)),
         (Wire((76,56), (76,66), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE)),
         (Wire((76,66), (76,76), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)),
         (Wire((26,76), (36,76), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)),
         (VoltageSource((36,76), (38,76), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)),
         (Wire((38,76), (76,76), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
         ]

circuit = Circuit(wires)
world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
world.show_circuit(
    {0: (64, 26), 1: (74, 26), 2: (76, 56), 3: (76, 66), 4: (38, 76), 5: (36, 76)}
)
world.compute()
world.show_all()