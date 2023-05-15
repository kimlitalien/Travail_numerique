
import env_examples  # Modifies path, DO NOT REMOVE
from sympy import Symbol
from src import Circuit, CoordinateSystem, VoltageSource, Wire, World
import numpy as np
import matplotlib.pyplot as mpl
if __name__ == "__main__":
    WORLD_SHAPE = (150, 150)
    BATTERY_VOLTAGE = 10.0
    HIGH_WIRE_RESISTANCE = 10.0
    LOW_WIRE_RESISTANCE = 0.001

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    x_expression = x
    y_expression = y
    eqs = (x_expression, y_expression)

        #on emplante une fonction pour paramétriser un cercle en cartésien
    def paramétrisation_cercle(rayon, angle_début, angle_fin, points):
        theta = np.linspace(angle_début, angle_fin, points)
        x = rayon * np.cos(theta) + décalage[0]
        y = rayon * np.sin(theta) + décalage[1]

        return (x,y)
    
    #on définit les constantes nécessaires pour le circuit c) 
    rayon = 50
    points = 100
    décalage = (75,75)
    wires = []
    liste_x = []
    liste_y =[]

    #on calcule le nombre de points proportionnels à l'angle
    points_droite_haut = int(points * 5/12 / 2)
    points_resistance = int(points * 1/6 / 2)
    points_gauche = int(points * 7/8 /2)
    points_source = int(points * 1/12 / 2)
    points_droite_bas = int(points * 11/24 / 2)

    #section de droite (haut)
    for i in range(points_droite_haut-1):
        début_x = paramétrisation_cercle(rayon, 0, 5/12 * np.pi, points_droite_haut)[0][i]
        fin_x = paramétrisation_cercle(rayon, 0 * np.pi, 5/12 * np.pi, points_droite_haut)[0][i+1]
        début_y = paramétrisation_cercle(rayon, 0 * np.pi, 5/12 * np.pi, points_droite_haut)[1][i]
        fin_y = paramétrisation_cercle(rayon, 0 * np.pi, 5/12 * np.pi, points_droite_haut)[1][i+1]
        wires.append(Wire((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)

    #section avec la résistance
    for i in range(points_resistance-1):
        début_x = paramétrisation_cercle(rayon, 5/12 * np.pi, 7/12 * np.pi, points_resistance)[0][i]
        fin_x = paramétrisation_cercle(rayon, 5/12 * np.pi, 7/12 * np.pi, points_resistance)[0][i+1]
        début_y = paramétrisation_cercle(rayon, 5/12 * np.pi, 7/12 * np.pi, points_resistance)[1][i]
        fin_y = paramétrisation_cercle(rayon, 5/12 * np.pi, 7/12 * np.pi, points_resistance)[1][i+1]
        wires.append(Wire((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, HIGH_WIRE_RESISTANCE))
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)

    #section de gauche
    for i in range(points_gauche-1):
        début_x = paramétrisation_cercle(rayon, 7/12 * np.pi, 35/24 * np.pi, points_gauche)[0][i]
        fin_x = paramétrisation_cercle(rayon, 7/12 * np.pi, 35/24 * np.pi, points_gauche)[0][i+1]
        début_y = paramétrisation_cercle(rayon, 7/12 * np.pi, 35/24 * np.pi, points_gauche)[1][i]
        fin_y = paramétrisation_cercle(rayon, 7/12 * np.pi, 35/24 * np.pi, points_gauche)[1][i+1]
        wires.append(Wire((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)

    #section avec la source
    for i in range(points_source-1):
        début_x = paramétrisation_cercle(rayon, 35/24 * np.pi, 37/24 * np.pi, points_source)[0][i]
        fin_x = paramétrisation_cercle(rayon, 35/24 * np.pi, 37/24 * np.pi, points_source)[0][i+1]
        début_y = paramétrisation_cercle(rayon, 35/24 * np.pi, 37/24 * np.pi, points_source)[1][i]
        fin_y = paramétrisation_cercle(rayon, 35/24 * np.pi, 37/24 * np.pi, points_source)[1][i+1]
        wires.append(VoltageSource((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, BATTERY_VOLTAGE))
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)

  #section de droite(bas)
    for i in range(points_droite_bas-1):
        début_x = paramétrisation_cercle(rayon, 37/24 * np.pi, 2 * np.pi, points_droite_bas)[0][i]
        fin_x = paramétrisation_cercle(rayon, 37/24 * np.pi, 2 * np.pi, points_droite_bas)[0][i+1]
        début_y = paramétrisation_cercle(rayon, 37/24 * np.pi, 2 * np.pi, points_droite_bas)[1][i]
        fin_y = paramétrisation_cercle(rayon, 37/24 * np.pi, 2 * np.pi, points_droite_bas)[1][i+1]
        wires.append(Wire((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)

    #ajout d'un segment pour fermer le cercle
    premier_point = (liste_x[0], liste_y[0])
    dernier_point = (liste_x[-1], liste_y[-1])
    wires.append(Wire(premier_point, dernier_point, eqs, cartesian_variables, LOW_WIRE_RESISTANCE))

            
    ground_position = (125,75)
    
    mpl.scatter(liste_x, liste_y)
    mpl.show()
    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    
    world.compute()
    world.show_all()