#!/usr/bin/env python3
'''calcul numérique d'une intégrale par méthode de rejet'''

from math import floor
import random as rd
import sys

DEB = -1
FIN = 1
BORNESUP = 1

def approximation_de_pi_par_monte_carlo(nb_de_points):
    ''' approximation de pi par la méthode de Monte-Carlo '''
    points_dedans = 0
    for _ in range(1, nb_de_points + 1):
        xialea = rd.uniform(0, FIN)
        yialea = rd.uniform(0, BORNESUP)
        points_dedans += int(xialea**2 + yialea**2 <= 1)
    return  4*(points_dedans/nb_de_points) * FIN * BORNESUP


def methode_de_rejet(largeur, hauteur, nb_points_nuage):
    ''' mise en oeuvre'''
    points = {}
    for point in range(1, nb_points_nuage+1):
        points[f'point {point}'] = {}
        xialea = rd.uniform(DEB, FIN)
        yialea = rd.uniform(-BORNESUP, BORNESUP)
        abscisse = floor(xialea*(largeur//2))
        ordonnée = floor(yialea*(hauteur//2))
        points[f'point {point}']['coordonnées'] = (abscisse, ordonnée)
        #points[f'point {point}']['coordonnées'] = (xialea, yialea)
        points[f'point {point}']['dedans ?'] = bool(xialea**2 + yialea**2 <= 1)
    return points

def main():
    """On génère"""
    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], "nombre de points = ")
        sys.exit(1)
    nb_points_nuage = int(sys.argv[1])
    print(approximation_de_pi_par_monte_carlo(nb_points_nuage))

if __name__ == "__main__":
    main()
