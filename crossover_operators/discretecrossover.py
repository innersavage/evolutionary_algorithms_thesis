import random

from crossover_operators.crossoverbase import CrossoverBase


class DiscreteCrossover(CrossoverBase):
    datatype = 'bin'

    def crossover_function(self, ind, **kwargs):
        new_ind = ''
        for i in range(len(ind[0])):
            if random.SystemRandom().random() <= 0.5:
                new_ind += ind[0][i]
            else:
                new_ind += ind[1][i]
        return [new_ind]
