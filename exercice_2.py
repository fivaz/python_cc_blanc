"""
a. Implémenter la méthode merge_sort pour en utilisant l'algorithme de tri par fusion

        merge_sort(self):

b. Quelle sont les complexités au pire de cas pour l'algorithme (total)
    et pour la fonction fusion ?

"""

import time
import math

from random import randint


def merge_sort():
    pass















def main(n: int, verbose: bool = False):
    arr: list = []
    for i in range(n):
        rand_int: int = randint(1, 1000)
        arr.append(rand_int)

    if verbose:
        print(arr)
        print()
        print("###### sorting %d elements ######" % n)

    time_begin = time.time()
    merge_sort(arr)
    time_diff: float = time.time() - time_begin

    if verbose:
        print("time: %.7f" % time_diff)
        print("###### sorted ######")
        print(arr)
        print()
    return time_diff


if __name__ == "__main__":

    repeat: int = 1

    for n in [10]:
        time_total: float = 0.0
        for r in range(repeat):
            time_total += main(n, verbose=True)
        print("###### %d sorted in %.20f secs ######" % (n, time_total / repeat))
    print()
