import random

from crossover_operators.crossoverbase import CrossoverBase


class IntermediateCrossover(CrossoverBase):
    datatype = 'real'

    def crossover_function(self, ind, **kwargs):
        xy = [[j[i] for j in ind] for i in range(len(ind[0]))]
        new_ind = [min(x) + random.SystemRandom().random() * (max(x) - min(x)) for x in xy]
        return [new_ind]
