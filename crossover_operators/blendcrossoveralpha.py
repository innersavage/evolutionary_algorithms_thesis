import random

from crossover_operators.crossoverbase import CrossoverBase


class BlendCrossoverAlpha(CrossoverBase):
    datatype = 'real'

    def crossover_function(self, ind, alpha=0.7, **kwargs):
        xy = [[j[i] for j in ind] for i in range(len(ind[0]))]
        dd = [abs(i[0] - i[1]) for i in xy]
        new_ind = []
        for i in range(2):
            new_ind.append([random.SystemRandom().uniform(min(xy[i]) - alpha * dd[i], max(xy[i]) + alpha * dd[i])
                            for i in range(len(ind[0]))])
        return new_ind
