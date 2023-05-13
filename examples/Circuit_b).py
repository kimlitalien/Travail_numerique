import env_examples  # Modifies path, DO NOT REMOVE
from sympy import Symbol
from src import Circuit, CoordinateSystem, VoltageSource, Wire, World

if __name__ == "__main__":
    WORLD_SHAPE = (150, 150)
    BATTERY_VOLTAGE = 10.0
    HIGH_WIRE_RESISTANCE = 10.0
    LOW_WIRE_RESISTANCE = 0.001

    c_var = Symbol("x"), Symbol("y")
    x, y = c_var

    x_expression_vertical = 0 * x
    y_expression_vertical = y
    v_eqs = (x_expression_vertical, y_expression_vertical)

    x_expression_horizontal = x
    y_expression_horizontal = 0 * y
    h_eqs = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((58, 24), (24, 24), h_eqs, c_var, LOW_WIRE_RESISTANCE),
        Wire((24, 24), (24, 65), v_eqs, c_var, LOW_WIRE_RESISTANCE),
        VoltageSource((24, 65), (24, 85), v_eqs, c_var, BATTERY_VOLTAGE),
        Wire((24, 85), (24, 126), v_eqs, c_var, LOW_WIRE_RESISTANCE),
        Wire((24, 126), (58, 126), h_eqs, c_var, LOW_WIRE_RESISTANCE),
        Wire((58, 126), (58, 85), v_eqs, c_var, LOW_WIRE_RESISTANCE),
        Wire((58, 85), (58, 65), v_eqs, c_var, HIGH_WIRE_RESISTANCE),
        Wire((58, 65), (58, 24), v_eqs, c_var, LOW_WIRE_RESISTANCE),
        Wire((58, 24), (126, 24), h_eqs, c_var, LOW_WIRE_RESISTANCE),
        Wire((126, 24), (126, 65), v_eqs, c_var, LOW_WIRE_RESISTANCE),
        VoltageSource((126, 65), (126, 85), v_eqs, c_var, BATTERY_VOLTAGE),
        Wire((126, 85), (126, 126), v_eqs, c_var, LOW_WIRE_RESISTANCE),
        Wire((126, 126), (58, 126), h_eqs, c_var, LOW_WIRE_RESISTANCE), # la le trou
        Wire((58, 126), (92, 126), h_eqs, c_var, LOW_WIRE_RESISTANCE),
        Wire((92, 126), (92, 85), v_eqs, c_var, LOW_WIRE_RESISTANCE),
        Wire((92, 85), (92, 65), v_eqs, c_var, HIGH_WIRE_RESISTANCE),
        Wire((92, 65), (92, 24), v_eqs, c_var, LOW_WIRE_RESISTANCE),
        Wire((92, 24), (58, 24), h_eqs, c_var, LOW_WIRE_RESISTANCE)
        ]

    ground_position = (58, 24)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)

    world.compute()
    world.show_all()