import env_examples
import numpy as np
from sympy import Symbol
from src import Circuit, CoordinateSystem, VoltageSource, Wire, World



if __name__ == "__main_":
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
        Wire((20, 1/12 * np.pi), (80, 1/12 * np.pi), eqs_radial, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, 1/12 * np.pi), (80, 5/24 * np.pi), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, 5/24 * np.pi), (60, 7/24 * np.pi), eqs_tangentiel, polar_variables, HIGH_WIRE_RESISTANCE),
        Wire((80, 7/24 * np.pi), (80, 5/12 * np.pi), eqs_tangentiel, polar_variables, HIGH_WIRE_RESISTANCE),
        Wire((80, 5/12 * np.pi), (20, 5/12 * np.pi), eqs_radial, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((20, 5/12 * np.pi), (20, 13/48 * np.pi), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((20, 13/48 * np.pi), (20, 11/48 * np.pi), eqs_tangentiel, polar_variables, BATTERY_VOLTAGE),
        Wire((20, 11/48 * np.pi), (20, 1/12 * np.pi), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE),
    ]
    ground = (20, 11/48 * np.pi)

    circuit = Circuit(wires, ground)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)

    world.show_circuit(
        {0: (20, 1/12 * np.pi),
        1: (80, 1/12 * np.pi),
        2: (80, 5/24 * np.pi),
        3: (80, 7/24 * np.pi),
        4: (80, 5/12 * np.pi),
        5: (20, 5/12 * np.pi),
        6: (20, 13/48 * np.pi),
        7: (20, 11/48 * np.pi)}
    )

    world.compute()
    world.show_all()