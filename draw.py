#!/usr/bin/env python3
'''calcul numérique d'une intégrale par méthode de rejet'''

import sys
from approximate_pi import methode_de_rejet, approximation_de_pi_par_monte_carlo

EPAISSEUR = 2
W_NUM = 10
H_NUM = 20
B_NUMS = 5
DIMENSIONS_VIRGULE = (2, 2)

class Tests:
    '''Cette classe comporte des méthodes publiques qui permettent de tester
    si un pixel de coordonées i, j est à l'intérieur du dessin formé par
    un numéro'''

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def test_caractère_3(self):
        ''' renvoie True si le pixel i, j est dans le dessin de "3"'''
        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2:
            if (H_NUM//2 - EPAISSEUR + 1) <= self.i <= H_NUM//2:
                return True

        if W_NUM//2 - EPAISSEUR + 1 <= self.j + W_NUM//2 <= W_NUM//2:
            if -(H_NUM//2 - EPAISSEUR + 1) <= self.i <= H_NUM//2 - EPAISSEUR:
                return True

        if -W_NUM//2 + 1<= self.j + W_NUM//2 <= W_NUM//2 - EPAISSEUR:
            if -EPAISSEUR//2 + 1 <= self.i <= EPAISSEUR//2:
                return True

        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2:
            if -H_NUM//2 + 1 <= self.i <= -(H_NUM//2 - EPAISSEUR):
                return True

        return None

    def test_caractère_virgule(self):
        ''' renvoie True si le pixel i, j est dans le dessin de la virgule '''
        largeurvirg = DIMENSIONS_VIRGULE[0]
        hauteurvirg = DIMENSIONS_VIRGULE[1]

        if -largeurvirg + 1 <= self.j  <= 0 :
            if H_NUM//2 -hauteurvirg + 1 <= self.i <= H_NUM//2:
                return True

        return None


    def test_caractère_5(self):
        ''' renvoie True si le pixel i, j est dans le dessin de "5"'''
        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if (H_NUM//2 - EPAISSEUR + 1) <= self.i <= H_NUM//2:
                return True

        if W_NUM//2 - EPAISSEUR + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if -EPAISSEUR//2 + 1 <= self.i <= H_NUM//2 - EPAISSEUR:
                return True

        if -W_NUM//2 + 1<= self.j + W_NUM//2 <= W_NUM//2 - EPAISSEUR:
            if -EPAISSEUR//2 + 1 <= self.i <= EPAISSEUR//2 :
                return True

        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= EPAISSEUR - W_NUM//2:
            if -H_NUM//2 + EPAISSEUR <= self.i <= -EPAISSEUR//2 :
                return True

        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if -H_NUM//2 + 1 <= self.i <= -(H_NUM//2 - EPAISSEUR):
                return True

        return None

    def test_caractère_2(self):
        ''' renvoie True si le pixel i, j est dans le dessin de "2"'''
        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if (H_NUM//2 - EPAISSEUR + 1) <= self.i <= H_NUM//2:
                return True

        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= EPAISSEUR - W_NUM//2:
            if -EPAISSEUR//2 + 1 <= self.i <= H_NUM//2 - EPAISSEUR:
                return True

        if EPAISSEUR - W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2:
            if -EPAISSEUR//2 + 1 <= self.i <= EPAISSEUR//2:
                return True

        if W_NUM//2 - EPAISSEUR + 1 <= self.j + W_NUM//2 <= W_NUM//2:
            if -H_NUM//2 + EPAISSEUR <= self.i <= -EPAISSEUR//2:
                return True

        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2:
            if -H_NUM//2 + 1 <= self.i <= -(H_NUM//2 - EPAISSEUR):
                return True

        return None

    def test_caractère_4(self):
        ''' renvoie True si le pixel i, j est dans le dessin de "4"'''
        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= EPAISSEUR - W_NUM//2:
            if EPAISSEUR//2 + 1 <= self.i + H_NUM//2 + EPAISSEUR//2 <= H_NUM//2:
                return True

        if -W_NUM//2 + 1<= self.j + W_NUM//2 <= W_NUM//2 - EPAISSEUR:
            if -EPAISSEUR//2 + 1 <= self.i <= EPAISSEUR//2 :
                return True

        if W_NUM//2 - EPAISSEUR + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if - H_NUM//2 + 1 <= self.i  <= H_NUM//2:
                return True

        return None

    def test_caractère_6(self):
        ''' renvoie True si le pixel i, j est dans le dessin de "6"'''
        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if (H_NUM//2 - EPAISSEUR + 1) <= self.i <= H_NUM//2:
                return True

        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= EPAISSEUR - W_NUM//2:
            if -H_NUM//2 + 1 <= self.i  <= H_NUM//2:
                return True

        if -W_NUM//2 + 1<= self.j + W_NUM//2 - EPAISSEUR <= W_NUM//2 - EPAISSEUR:
            if -EPAISSEUR//2 + 1 <= self.i <= EPAISSEUR//2 :
                return True

        if W_NUM//2 - EPAISSEUR + 1 <= self.j + W_NUM//2 <= W_NUM//2:
            if -H_NUM//2 - EPAISSEUR//2 + 1 <= self.i - H_NUM//2 <= -EPAISSEUR:
                return True

        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if -H_NUM//2 + 1 <= self.i <= -(H_NUM//2 - EPAISSEUR):
                return True

        return None


    def test_caractère_9(self):
        ''' renvoie True si le pixel i, j est dans le dessin de "9"'''
        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if (H_NUM//2 - EPAISSEUR + 1) <= self.i <= H_NUM//2:
                return True

        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= EPAISSEUR - W_NUM//2:
            if EPAISSEUR//2 + 1 <= self.i + H_NUM//2 - EPAISSEUR//2 <= H_NUM//2 - EPAISSEUR:
                return True

        if -W_NUM//2 + 1<= self.j + W_NUM//2 <= W_NUM//2 - EPAISSEUR:
            if -EPAISSEUR//2 + 1 <= self.i <= EPAISSEUR//2 :
                return True

        if W_NUM//2 - EPAISSEUR + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if -(H_NUM//2 - EPAISSEUR + 1) <= self.i <= H_NUM//2 - EPAISSEUR:
                return True

        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if -H_NUM//2 + 1 <= self.i <= -(H_NUM//2 - EPAISSEUR):
                return True

        return None


    def test_caractère_7(self):
        ''' renvoie True si le pixel i, j est dans le dessin de "7"'''
        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if -H_NUM//2 + 1 <= self.i <= -(H_NUM//2 - EPAISSEUR):
                return True

        if W_NUM//2 - EPAISSEUR + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if - H_NUM//2 + 1 <= self.i  <= H_NUM//2:
                return True

        return None

    def test_caractère_1(self):
        ''' renvoie True si le pixel i, j est dans le dessin de "1"'''
        if W_NUM//2 - EPAISSEUR + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if - H_NUM//2 + 1 <= self.i  <= H_NUM//2:
                return True

        return None

    def test_caractère_0(self):
        ''' renvoie True si le pixel i, j est dans le dessin de "0"'''
        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if (H_NUM//2 - EPAISSEUR + 1) <= self.i <= H_NUM//2:
                return True

        if W_NUM//2 - EPAISSEUR + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if - H_NUM//2 + 1 <= self.i  <= H_NUM//2:
                return True

        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= EPAISSEUR - W_NUM//2:
            if -H_NUM//2 + 1 <= self.i  <= H_NUM//2:
                return True

        if -W_NUM//2 + 1 <= self.j + W_NUM//2 <= W_NUM//2 :
            if -H_NUM//2 + 1 <= self.i <= -(H_NUM//2 - EPAISSEUR):
                return True

        return None

    def test_caractère_8(self):
        ''' renvoie True si le pixel i, j est dans le dessin de "8"'''
        if Tests.test_caractère_0(self):
            return True

        if -W_NUM//2 + EPAISSEUR + 1 <= self.j + W_NUM//2 <= W_NUM//2 - EPAISSEUR:
            if -EPAISSEUR//2 + 1 <= self.i <= EPAISSEUR//2 :
                return True

        return None

    def test_caractère_fictif(self):
        ''' on renvoie rien s'il y a rien à afficher '''

def affichage_nuage(largeur, hauteur, nb_points_nuage):
    ''' mise en oeuvre '''
    print('P3')
    print(f'{largeur} {hauteur}')
    print('255')
    points = methode_de_rejet(largeur, hauteur, nb_points_nuage)
    ensemble_coordonnées_points = [points[f'point {num}']['coordonnées']
                            for num in range(1, nb_points_nuage +1)]
    précision = 5
    pi_approx = str(approximation_de_pi_par_monte_carlo(nb_points_nuage))
    pi_approx = pi_approx + '0'*(len(pi_approx) +1 - précision + 1)

    liste_num_approx = [num for num in pi_approx[:précision + 2] if num != '.']
    liste_num_approx = liste_num_approx + ['fictif']*(7 - précision + 1)

    for pixlin in range(-largeur//2, largeur//2):
        for pixcol in range(-hauteur//2, hauteur//2):
            point_cour = (pixlin, pixcol)

            if getattr(Tests, f'test_caractère_{liste_num_approx[0]}')(Tests(pixlin, pixcol +(B_NUMS
                +W_NUM//2)*(précision -1))) or getattr(Tests,'test_caractère_virgule')(Tests(pixlin,
                pixcol + (B_NUMS + W_NUM//2)*(précision - 1) - W_NUM//2)):
                print('0 0 0')

            elif getattr(Tests, f'test_caractère_{liste_num_approx[1]}')(Tests(pixlin, pixcol
                + (B_NUMS + W_NUM//2)*(précision - 3))):
                print('0 0 0')

            elif getattr(Tests, f'test_caractère_{liste_num_approx[2]}')(Tests(pixlin, pixcol
                + (B_NUMS + W_NUM//2)*(précision - 1) - 2*W_NUM - 3*B_NUMS )):
                print('0 0 0')

            elif getattr(Tests, f'test_caractère_{liste_num_approx[3]}')(Tests(pixlin, pixcol
                + (B_NUMS + W_NUM//2)*(précision - 1) - 3*W_NUM - 4*B_NUMS )):
                print('0 0 0')

            elif getattr(Tests, f'test_caractère_{liste_num_approx[4]}')(Tests(pixlin, pixcol
                + (B_NUMS + W_NUM//2)*(précision - 1) - 4*W_NUM - 5*B_NUMS )):
                print('0 0 0')

            elif getattr(Tests, f'test_caractère_{liste_num_approx[5]}')(Tests(pixlin, pixcol
+ (B_NUMS + W_NUM//2)*(précision - 1) - 5*W_NUM - 6*B_NUMS)):
                print('0 0 0')

            elif point_cour not in ensemble_coordonnées_points:
                print('255 255 255')
            else:
                numéro_point = ensemble_coordonnées_points.index(point_cour)
                if points[f'point {numéro_point + 1}']['dedans ?']:
                    print('180 30 130')
                else:
                    print('25 100 101')

def main():
    """On génère"""
    if len(sys.argv) != 4 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], "largeur hauteur nombre_de_points > image.ppm")
        sys.exit(1)

    largeur, hauteur = int(sys.argv[1]), int(sys.argv[2])
    nombre_de_points = int(sys.argv[3])

    affichage_nuage(largeur, hauteur, nombre_de_points)

if __name__ == "__main__":
    main()
