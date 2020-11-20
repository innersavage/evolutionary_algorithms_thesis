import random

from crossover_operators.crossoverbase import CrossoverBase


class KPointCrossover(CrossoverBase):
    datatype = 'bin'

    def crossover_function(self, ind, k=2, **kwargs):
        crossover_points = [random.SystemRandom().randint(0, len(ind[0]) - 1) for i in range(k)]
        crossover_points.sort()
        for crossover_point in crossover_points:
            ind[0], ind[1] = ind[0][0:crossover_point] + ind[1][crossover_point:], \
                             ind[1][0:crossover_point] + ind[0][crossover_point:]
        return ind
