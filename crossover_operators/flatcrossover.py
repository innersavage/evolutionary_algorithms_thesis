import random

from crossover_operators.crossoverbase import CrossoverBase


class FlatCrossover(CrossoverBase):
    datatype = 'real'

    def crossover_function(self, ind, **kwargs):
        x, y = [ind[0][0], ind[1][0]], [ind[1][0], ind[1][1]]
        new_ind = [random.SystemRandom().uniform(min(x), max(x)), random.SystemRandom().uniform(min(y), max(y))]
        return [new_ind]
