import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

from src.coordinate_and_position import CoordinateSystem
from src.fields import ScalarField


class LaplaceEquationSolver:
    """
    A Laplace equation solver used to compute the resultant potential field P in 2D-space generated by a constant
    voltage field V (for example due to wires).
    """

    def __init__(self, nb_iterations: int = 1000):
        """
        Laplace solver constructor. Used to define the number of iterations for the relaxation method.

        Parameters
        ----------
        nb_iterations : int
            Number of iterations performed to obtain the potential by the relaxation method (default = 1000).
        """
        self.nb_iterations = nb_iterations

    def _solve_in_cartesian_coordinate(
            self,
            constant_voltage: ScalarField,
            delta_x: float,
            delta_y: float
    ) -> ScalarField:
        """
        Solve the Laplace equation to compute the resultant potential field P in 2D-space.

        Parameters
        ----------
        constant_voltage : ScalarField
            A scalar field V : ℝ² → ℝ ; (x, y) → V(x, y), where V(x, y) is the electrical components' voltage at a
            given point (x, y) in space.
        delta_x : float
            Small discretization of the x-axis.
        delta_y : float
            Small discretization of the y-axis.

        Returns
        -------
        potential : ScalarField
            A scalar field P : ℝ² → ℝ ; (x, y) → P(x, y), where P(x, y) is the electric potential at a given point
            (x, y) in space. The difference between P and V is that P gives the potential in the whole world, i.e inside
            the electrical components and in the empty space between the electrical components, while the field V
            always gives V(x, y) = 0 if (x, y) is not a point belonging to an electrical component of the circuit.
        """

        liste_voltage_pas_zero = []

#Trouver les valeurs fixes
        for num_rangee, rangee in enumerate(constant_voltage):
            for num_colone, voltage in enumerate(rangee):
                if voltage != 0:
                    liste_voltage_pas_zero.append((num_colone, num_rangee, voltage))

                #initialise matrice de dépendance avec matrice de tension constante des composants
        matrice_dependance = constant_voltage
        #on itère
        for i in range(self.nb_iterations):
            #on crée des sous-matrices matrices pour calculer le champ de potentiel électrique en chaque point (x,y) de l'espace
            #Les différentes matrices représentent les potentiels électriques en chaque point voisin d'un point donné (x, y) dans les 4 direction: nord, sud, est et ouest 
            #Utilisées pour approximer les dérivées partielles du potentiel électrique en chaque point de l'espace, ce qui permet ensuite de résoudre l'équation de Laplace pour trouver le champ de potentiel électrique.
            V_ouest = np.zeros((constant_voltage.shape[1] + 2, constant_voltage.shape[0] + 2))
            V_ouest[0:-2, 1:-1]=matrice_dependance
            V_est = np.zeros((constant_voltage.shape[1] + 2, constant_voltage.shape[0] + 2))
            V_est[2:, 1:-1]=matrice_dependance
            V_nord = np.zeros((constant_voltage.shape[1] + 2, constant_voltage.shape[0] + 2))
            V_nord[1:-1, 0:-2]=matrice_dependance
            V_sud = np.zeros((constant_voltage.shape[1] + 2, constant_voltage.shape[0] + 2))
            V_sud[1:-1, 2:]=matrice_dependance
            
            # calcule la nouvelle matrice des potentiels, calculée à partir de la matrice de tension constante constant_voltage, ainsi que de des quatre sous-matrices matrices supplémentaires
            matrice_dependance=((1/delta_x**2+1/delta_y**2)**(-1) * 0.5 * ((V_sud+V_nord)/delta_y**2+(V_est+V_ouest)/delta_x**2))[1:-1, 1:-1]
            #parcourt la liste composants_liste et met à jour les potentiels de tous les points correspondant à des composants du circuit électrique, en utilisant les valeurs de tension constante
            for value in liste_voltage_pas_zero:
                matrice_dependance[value[1], value[0]] = value[2]
        # retourne la matrice de potentiel mise à jour sous la forme d'un objet    
        return ScalarField(matrice_dependance)




    def _solve_in_polar_coordinate(
            self,
            constant_voltage: ScalarField,
            delta_r: float,
            delta_theta: float
    ) -> ScalarField:
        """
        Solve the Laplace equation to compute the resultant potential field P in 2D-space.

        Parameters
        ----------
        constant_voltage : ScalarField
            A scalar field V : ℝ² → ℝ ; (r, θ) → V(r, θ), where V(r, θ) is the electrical components' voltage at a
            given point (r, θ) in space.
        delta_r : float
            Small discretization of the r-axis.
        delta_theta : float
            Small discretization of the θ-axis.

        Returns
        -------
        potential : ScalarField
            A scalar field P : ℝ² → ℝ ; (r, θ) → P(r, θ), where P(r, θ) is the electric potential at a given point
            (r, θ) in space. The difference between P and V is that P gives the potential in the whole world, i.e inside
            the electrical components and in the empty space between the electrical components, while the field V
            always gives V(r, θ) = 0 if (r, θ) is not a point belonging to an electrical component of the circuit.
        """

        #création liste contenant coordonnées polaires des composants avec tension non nulle
        composants_liste = []
        for angle, ligne in enumerate(constant_voltage):
            for rayon, val in enumerate(ligne):
                if val != 0:
                    composants_liste.append((rayon, angle, val))
        #initialise matrice de dépendance avec matrice de tension constante des composants
        matrice_dependance = constant_voltage
        #on itère
        for i in range(self.nb_iterations):
            #on crée des sous-matrices matrices pour calculer le champ de potentiel électrique en chaque point (r,theta) de l'espace
            #Les différentes matrices représentent les potentiels électriques en chaque point voisin d'un point donné (r, theta) dans les 4 direction: nord, sud, est et ouest 
            #Utilisées pour approximer les dérivées partielles du potentiel électrique en chaque point de l'espace, ce qui permet ensuite de résoudre l'équation de Laplace pour trouver le champ de potentiel électrique.
            V_nord = np.zeros((constant_voltage.shape[1] + 2, constant_voltage.shape[0] + 2))
            V_nord[0:-2, 1:-1]=matrice_dependance
            V_sud = np.zeros((constant_voltage.shape[1] + 2, constant_voltage.shape[0] + 2))
            V_sud[2:, 1:-1]=matrice_dependance
            V_ouest = np.zeros((constant_voltage.shape[1] + 2, constant_voltage.shape[0] + 2))
            V_ouest[1:-1, 0:-2]=matrice_dependance
            V_est = np.zeros((constant_voltage.shape[1] + 2, constant_voltage.shape[0] + 2))
            V_est[1:-1, 2:]=matrice_dependance
            
            # calcule la nouvelle matrice des potentiels, calculée à partir de la matrice de tension constante constant_voltage, ainsi que de des quatre sous-matrices matrices supplémentaires
            matrice_dependance=((1/delta_r**2+1/delta_theta**2)**(-1) * 0.5 * ((V_sud+V_nord)/delta_r**2+(V_est+V_ouest)/delta_theta**2))[1:-1, 1:-1]
            #parcourt la liste composants_liste et met à jour les potentiels de tous les points correspondant à des composants du circuit électrique, en utilisant les valeurs de tension constante
            for k in composants_liste:
                matrice_dependance[k[1], k[0]] = k[2]
            # retourne la matrice de potentiel mise à jour sous la forme d'un objet    
        return ScalarField(matrice_dependance)


    def solve(
            self,
            constant_voltage: ScalarField,
            coordinate_system: CoordinateSystem,
            delta_q1: float,
            delta_q2: float
    ) -> ScalarField:
        """
        Solve the Laplace equation to compute the resultant potential field P in 2D-space.

        Parameters
        ----------
        constant_voltage : ScalarField
            A scalar field V : ℝ² → ℝ representing a constant voltage field.
        coordinate_system : CoordinateSystem
            Coordinate system.
        delta_q1 : float
            Small discretization of the first axis.
        delta_q2 : float
            Small discretization of the second axis.

        Returns
        -------
        potential : ScalarField
            A scalar field P : ℝ² → ℝ  representing the potential in the 2D world.
        """
        if coordinate_system == CoordinateSystem.CARTESIAN:
            return self._solve_in_cartesian_coordinate(constant_voltage, delta_q1, delta_q2)
        elif coordinate_system == CoordinateSystem.POLAR:
            return self._solve_in_polar_coordinate(constant_voltage, delta_q1, delta_q2)
        else:
            raise NotImplementedError("Only the cartesian and polar coordinates system are implemented.")
