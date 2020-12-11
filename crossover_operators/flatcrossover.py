import random

from crossover_operators.crossoverbase import CrossoverBase


class FlatCrossover(CrossoverBase):
    datatype = 'real'

    def crossover_function(self, ind, **kwargs):
        xy = [[j[i] for j in ind] for i in range(len(ind[0]))]
        new_ind = [random.SystemRandom().uniform(min(x), max(x)) for x in xy]
        return [new_ind]
