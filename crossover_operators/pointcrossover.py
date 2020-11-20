import random

from crossover_operators.crossoverbase import CrossoverBase


class PointCrossover(CrossoverBase):
    datatype = 'bin'

    def crossover_function(self, ind, **kwargs):
        crossover_point = random.SystemRandom().randint(0, len(ind[0]))
        ind[0], ind[1] = ind[0][0:crossover_point] + ind[1][crossover_point:], \
                         ind[1][0:crossover_point] + ind[0][crossover_point:]
        return ind
