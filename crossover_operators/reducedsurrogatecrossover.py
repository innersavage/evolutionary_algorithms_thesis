import random

from crossover_operators.crossoverbase import CrossoverBase


class ReducedSurrogateCrossover(CrossoverBase):
    datatype = 'bin'

    def crossover_function(self, ind, **kwargs):
        potential_crossover_points = []
        for i in range(len(ind[0])):
            if ind[0][i] != ind[1][i]:
                potential_crossover_points.append(i)
        if len(potential_crossover_points) > 0:
            crossover_point = potential_crossover_points[random.SystemRandom().
                randint(0, len(potential_crossover_points) - 1)]
            ind[0], ind[1] = ind[0][0:crossover_point] + ind[1][crossover_point:], \
                             ind[1][0:crossover_point] + ind[0][crossover_point:]
        return ind
