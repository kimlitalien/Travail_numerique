import env_examples
import numpy as np
from sympy import Symbol
from src import Circuit, CoordinateSystem, VoltageSource, Wire, World



if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    polar_variables = Symbol("r"), Symbol("theta")
    r, theta = polar_variables

    #tangentiel
    r_tangentiel = 0 * r
    theta_tangentiel = theta
    eqs_tangentiel = (r_tangentiel, theta_tangentiel)

    #radiale
    r_radial = r
    theta_radial = 0 * theta
    eqs_radial = (r_radial, theta_radial)


    wires = [
        Wire((60, 1), (40, 1), eqs_radial, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((60, 1), (60, 0.8), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((60, 0.8), (60, 0.7), eqs_tangentiel, polar_variables, HIGH_WIRE_RESISTANCE),
        Wire((60, 0.7), (60, 0.5), eqs_tangentiel, polar_variables, HIGH_WIRE_RESISTANCE),
        Wire((40, 0.5), (60, 0.5), eqs_radial, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((40, 0.5), (40, 0.7), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((40, 0.7), (40, 0.8), eqs_tangentiel, polar_variables, BATTERY_VOLTAGE),
        Wire((40, 0.8), (40, 1), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE),
    ]
    ground = (40, 1)

    circuit = Circuit(wires, ground)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)

    world.show_circuit(
        {0: (40, 1),
        1: (60, 1),
        2: (40, 0.5),
        3: (60, 0.5),
        4: (40, 0.7),
        5: (60, 0.7),
        6: (40, 0.8),
        7: (60, 0.8)}
    )

    world.compute()
    world.show_all()