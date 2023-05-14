import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    x_expression_vertical = 0 * x
    y_expression_vertical = y
    vertical_eqs = (x_expression_vertical, y_expression_vertical)

    x_expression_horizontal = x
    y_expression_horizontal = 0 * y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)


    wires = [
        Wire((26,26), (64,26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((64,26), (74,26), horizontal_eqs, cartesian_variables,HIGH_WIRE_RESISTANCE),
        Wire((74,26), (76,26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((76,26), (76,56), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((76,56), (76,66), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((76,66), (76,76), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((76,76), (38,76), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((38,76), (36,76), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((36,76), (26,76), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((26,76), (26,26), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        ]

    ground_position = (38, 76)
    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.compute()
    world.show_all()