"""
Étant donné un tableau de notes trié en fonction des critères :

-	Le critère de réussite est d’avoir une note égale ou supérieur à 4.0.
-	Les notes ne doivent pas forcément être triées dans l’ordre croissant
    ou décroissant mais séparées en deux :
        les notes réussies d’un côté et les notes échouées de l’autre
-	Comme convention, les notes plus petites que 4.0 restent à gauche et
    les notes plus grandes restent à droite

a) Écrire un algorithme le plus efficient pour rechercher l’indice i du premier élément
    plus grand ou égal à 4.0 dans le tableau trié

# cas 1 -> [3.5, 2.3, 4.5, 4.0, 5.0]    : i = 2
# cas 2 -> [4.5, 4.0, 5.0]              : i = 0
# cas 3 -> [3.5, 2.3]                   : i = 2
"""
from random import random


def recherche_reussite():
    pass














############################################################
# [3.5, 4.5, 2.3, 4.0, 5.0] --> [3.5, 2.3, 4.5, 4.0, 5.0]

def tri_note(A: list, cutoff: float = 4.0):
    """
    tri note -> tri lineaire basé sur l'algo tri pair-impair
    :param A: un tableau de note à trier
    :param cutoff: la note
    :return:
    """
    e: int = 0
    r: int = len(A) - 1
    while e < r:
        while e <= len(A) - 1 and A[e] < cutoff:
            e += 1
        while r >= 0 and A[r] >= cutoff:
            r -= 1

        if e < r:
            tmp: float = A[e]
            A[e] = A[r]
            A[r] = tmp


############################################################


if __name__ == "__main__":
    n: int = 10
    notes: list = []
    for i in range(n):
        rand_float: float = round(10 * (random() * 5 + 1)) / 10
        notes.append(rand_float)

    tri_note(notes, 4.0)
    print(notes)
    print()
    print("nombre de réussites:", len(notes) - recherche_reussite(notes))
