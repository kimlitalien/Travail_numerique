import numpy as np
import matplotlib.pyplot as mpl


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
    x_expression = x
    y_expression = y
    eqs = (x_expression, y_expression)




    #on emplante une fonction pour paramétriser un cercle en cartésien
    def paramétrisation_cercle(rayon, angle_début, angle_fin, points):
        theta = np.linspace(angle_début, angle_fin, points)
        x = rayon * np.cos(theta) + décalage[0]
        y = rayon * np.sin(theta) + décalage[1]

        return (x,y)
    
    #on inplante une fonction pour paramétriser une droite:
    def paramétrisation_droite(départ, arrivée, points):
        t = np.linspace(0, 1, points)
        x = départ[0] + (arrivée[0] - départ[0]) * t
        y = départ[1] + (arrivée[1] - départ[1]) * t

        return (x,y)
    
    #on définit les constantes nécessaires pour le circuit d) 
    rayon_1 = 125
    rayon_2 = 90
    points = 50
    décalage = (0,0)

    wires = []
    liste_x = []
    liste_y =[]

    #on calcule le nombre de points proportionnels à l'angle
    points_haut_droite = int(points * 1/8 / 2)
    points_resistance = int(points * 1/12 / 2)
    points_haut_gauche = int(points * 1/8 /2)
    points_bas_droite = int(points * 7/48 / 2)
    points_source = int(points * 1/24)
    points_bas_gauche = int(points * 7/48 / 2)

    #section du haut (droite)
    for i in range(points_haut_droite-1):
        début_x = paramétrisation_cercle(rayon_1, 1/12 * np.pi, 5/24 * np.pi, points_haut_droite)[0][i]
        fin_x = paramétrisation_cercle(rayon_1, 1/12 * np.pi, 5/24 * np.pi, points_haut_droite)[0][i+1]
        début_y = paramétrisation_cercle(rayon_1, 1/12 * np.pi, 5/24 * np.pi, points_haut_droite)[1][i]
        fin_y = paramétrisation_cercle(rayon_1, 1/12 * np.pi, 5/24 * np.pi, points_haut_droite)[1][i+1]
        wires.append(Wire((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
        print((début_x, début_y), (fin_x, fin_y))
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)

    #section avec la résistance
    for i in range(points_resistance-1):
        début_x = paramétrisation_cercle(rayon_1, 5/24 * np.pi, 7/24 * np.pi, points_resistance)[0][i]
        fin_x = paramétrisation_cercle(rayon_1, 5/24 * np.pi, 7/24 * np.pi, points_resistance)[0][i+1]
        début_y = paramétrisation_cercle(rayon_1, 5/24 * np.pi, 7/24 * np.pi, points_resistance)[1][i]
        fin_y = paramétrisation_cercle(rayon_1, 5/24 * np.pi, 7/24 * np.pi, points_resistance)[1][i+1]
        wires.append(Wire((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, HIGH_WIRE_RESISTANCE))
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)
        print((début_x, début_y), (fin_x, fin_y))

    #section du haut (gauche)
    for i in range(points_haut_gauche-1):
        début_x = paramétrisation_cercle(rayon_1, 7/24 * np.pi, 5/12 * np.pi, points_haut_gauche)[0][i]
        fin_x = paramétrisation_cercle(rayon_1, 7/24 * np.pi, 5/12 * np.pi, points_haut_gauche)[0][i+1]
        début_y = paramétrisation_cercle(rayon_1, 7/24 * np.pi, 5/12 * np.pi, points_haut_gauche)[1][i]
        fin_y = paramétrisation_cercle(rayon_1, 7/24 * np.pi, 5/12 * np.pi, points_haut_gauche)[1][i+1]
        wires.append(Wire((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
        print((début_x, début_y), (fin_x, fin_y))
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)

    #section de gauche pour fermer le cicruit
    p1 = (paramétrisation_cercle(rayon_1, 5/12 * np.pi, 5/12 * np.pi, 1)[0], (paramétrisation_cercle(rayon_1, 5/12 * np.pi, 5/12 * np.pi, 1))[1])
    p2 = (paramétrisation_cercle(rayon_2, 5/12 * np.pi, 5/12 * np.pi, 1)[0], (paramétrisation_cercle(rayon_2, 5/12 * np.pi, 5/12 * np.pi, 1))[1])
    for i in range(points-1):
        début_x = paramétrisation_droite(p1, p2, points)[0][i]
        fin_x = paramétrisation_droite(p1, p2, points)[0][i+1]
        début_y = paramétrisation_droite(p1, p2, points)[1][i]
        fin_y = paramétrisation_droite(p1, p2, points)[1][i+1]
        wires.append(Wire((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
        print((début_x, début_y), (fin_x, fin_y))
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)

    #section du bas (gauche)
    for i in range(points_bas_gauche-1):
        début_x = paramétrisation_cercle(rayon_2, 5/12 * np.pi, 13/48 * np.pi, points_bas_gauche)[0][i]
        fin_x = paramétrisation_cercle(rayon_2, 5/12 * np.pi, 13/48 * np.pi, points_bas_gauche)[0][i+1]
        début_y = paramétrisation_cercle(rayon_2, 5/12 * np.pi, 13/48 * np.pi, points_bas_gauche)[1][i]
        fin_y = paramétrisation_cercle(rayon_2, 5/12 * np.pi, 13/48 * np.pi, points_bas_gauche)[1][i+1]
        wires.append(Wire((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
        print((début_x, début_y), (fin_x, fin_y))
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)

    #section avec la source
    for i in range(points_source-1):
        début_x = paramétrisation_cercle(rayon_2, 13/48 * np.pi, 11/48 * np.pi, points_source)[0][i]
        fin_x = paramétrisation_cercle(rayon_2, 13/48 * np.pi, 11/48 * np.pi, points_source)[0][i+1]
        début_y = paramétrisation_cercle(rayon_2, 13/48 * np.pi, 11/48 * np.pi, points_source)[1][i]
        fin_y = paramétrisation_cercle(rayon_2, 13/48 * np.pi, 11/48 * np.pi, points_source)[1][i+1]
        wires.append(VoltageSource((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, BATTERY_VOLTAGE))
        ground_position = (fin_x, fin_y)
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)
        print((début_x, début_y), (fin_x, fin_y))

    #section du bas (droite)
    for i in range(points_bas_droite-1):
        début_x = paramétrisation_cercle(rayon_2, 11/48 * np.pi, 1/12 * np.pi, points_bas_droite)[0][i]
        fin_x = paramétrisation_cercle(rayon_2, 11/48 * np.pi, 1/12 * np.pi, points_bas_droite)[0][i+1]
        début_y = paramétrisation_cercle(rayon_2, 11/48 * np.pi, 1/12 * np.pi, points_bas_droite)[1][i]
        fin_y = paramétrisation_cercle(rayon_2, 11/48 * np.pi, 1/12 * np.pi, points_bas_droite)[1][i+1]
        wires.append(Wire((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
        print((début_x, début_y), (fin_x, fin_y))
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)

    #section de droite pour fermer le circuit
    p3 = (paramétrisation_cercle(rayon_2, 1/12 * np.pi, 1/12 * np.pi, 1)[0], (paramétrisation_cercle(rayon_2, 1/12 * np.pi, 1/12 * np.pi, 1))[1])
    p4 = (paramétrisation_cercle(rayon_1, 1/12 * np.pi, 1/12 * np.pi, 1)[0], (paramétrisation_cercle(rayon_1, 1/12 * np.pi, 1/12 * np.pi, 1))[1])
    for i in range(points-1):
        début_x = paramétrisation_droite(p3, p4, points)[0][i]
        fin_x = paramétrisation_droite(p3, p4, points)[0][i+1]
        début_y = paramétrisation_droite(p3, p4, points)[1][i]
        fin_y = paramétrisation_droite(p3, p4, points)[1][i+1]
        wires.append(Wire((début_x, début_y), (fin_x, fin_y), eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
        print((début_x, début_y), (fin_x, fin_y))
        liste_x.append(début_x)
        liste_x.append(fin_x)
        liste_y.append(début_y)
        liste_y.append(fin_y)



    mpl.scatter(liste_x, liste_y)
    mpl.scatter(p1[0], p1[1])
    mpl.scatter(p2[0], p2[1])
    mpl.scatter(p3[0], p3[1])
    mpl.scatter(p4[0], p4[1])
    mpl.show()



    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    
    world.compute()
    world.show_all()




