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

    wires = [
        Wire((20, 0.13), (80, 0.13), eqs_radial, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, 0.13), (80, 0.45), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, 0.45), (80, 0.7), eqs_tangentiel, polar_variables, HIGH_WIRE_RESISTANCE),
        Wire((80, 0.7), (80, 0.45), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, 1), (80, 1), eqs_radial, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((80, 1), (20, 0.7), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((20, 0.7), (20, 0.45), eqs_tangentiel, polar_variables, BATTERY_VOLTAGE),
        Wire((80, 0.45), (20, 0.13), eqs_tangentiel, polar_variables, LOW_WIRE_RESISTANCE),
    ]
    ground = (20, 0.75)

    circuit = Circuit(wires, ground)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)

    world.show_circuit(
        {0: (20, 0.13),
        1: (80, 0.13),
        2: (80, 0.45),
        3: (20, 0.7),
        4: (20, 1),
        5: (20, 1),
        6: (20, 0.7),
        7: (20, 0.45)}
    )

    world.compute()
    world.show_all()