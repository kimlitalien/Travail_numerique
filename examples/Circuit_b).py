import env_examples  # Modifies path, DO NOT REMOVE
from sympy import Symbol
from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

if __name__ == "__main__":
    WORLD_SHAPE = (150, 150)
    BATTERY_VOLTAGE = 10.0
    HIGH_WIRE_RESISTANCE = 10.0
    LOW_WIRE_RESISTANCE = 0.001

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    x_expression_vertical = 0 * x
    y_expression_vertical = y
    vertical_eqs = (x_expression_vertical, y_expression_vertical)

    x_expression_horizontal = x
    y_expression_horizontal = 0 * y
    horizontal_eqs= (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((58, 24), (24, 24), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((24, 24), (24, 65), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((24, 65), (24, 85), vertical_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((24, 85), (24, 126), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((24, 126), (58, 126), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 126), (58, 85), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 85), (58, 65), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((58, 65), (58, 24), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 24), (126, 24), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((126, 24), (126, 65), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((126, 65), (126, 85), vertical_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((126, 85), (126, 126), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((126, 126), (58, 126), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 126), (92, 126), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((92, 126), (92, 85), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((92, 85), (92, 65), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((92, 65), (92, 24), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((92, 24), (58, 24), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)
        ]

    ground_position = (58, 24)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)

    world.compute()
    world.show_magnetic_field()
    #world.show_all()