import random

from crossover_operators.crossoverbase import CrossoverBase


class IntermediateCrossover(CrossoverBase):
    datatype = 'real'

    def crossover_function(self, ind, **kwargs):
        x, y = [ind[0][0], ind[1][0]], [ind[1][0], ind[1][1]]
        new_ind = [min(x) + random.SystemRandom().random() * (max(x) - min(x)),
                   min(y) + random.SystemRandom().random() * (max(y) - min(y))]
        return [new_ind]
