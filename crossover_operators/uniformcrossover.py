import random

from crossover_operators.crossoverbase import CrossoverBase


class UniformCrossover(CrossoverBase):
    datatype = 'bin'

    def crossover_function(self, ind, p, **kwargs):
        ind = [list(i) for i in ind]
        for i in range(len(ind[0])):
            if random.SystemRandom().random() < p:
                ind[0][i], ind[1][i] = ind[1][i], ind[0][i]
        return [''.join(i) for i in ind]
