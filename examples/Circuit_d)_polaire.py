import numpy as np 
import env_examples
from sympy import Symbol


from src import Circuit, CoordinateSystem, VoltageSource, Wire, World
from src.laplace_equation_solver import LaplaceEquationSolver
from src.biot_savart_equation_solver import BiotSavartEquationSolver


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

    #constantes pour le circuit d)
    theta1 = np.pi / 24
    theta2 = np.pi / 3

    wires = [
        Wire((20, theta1), (80, theta1), eqs_radial, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, theta1), (80, np.pi/7), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, np.pi/7), (80, 2*np.pi/9), eqs_tangentiel, polar_variables, HIGH_WIRE_RESISTANCE),
        Wire((80, 2*np.pi/9), (80, theta2), eqs_tangentiel, polar_variables, HIGH_WIRE_RESISTANCE),
        Wire((80, theta2), (20, theta2), eqs_radial, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((20, theta2), (20, 2*np.pi/9), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((20, 2*np.pi/9), (20, np.pi/7), eqs_tangentiel, polar_variables, BATTERY_VOLTAGE),
        Wire((20, np.pi/7), (20, theta1), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE)
    ]
    ground = (20, np.pi/7)

    circuit = Circuit(wires, ground)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)

    world.show_circuit(
        {0: (20, theta1),
        1: (80, theta1), 
        2: (80, np.pi/7),
        3: (80, 2*np.pi/9),
        4: (80, theta2),
        5: (20, theta2),
        6: (20, 2*np.pi/9),
        7: (20, np.pi/7)}
    )

    world.compute()
    world.show_all()