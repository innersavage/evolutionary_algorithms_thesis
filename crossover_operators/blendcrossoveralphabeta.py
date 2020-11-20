import random

from crossover_operators.crossoverbase import CrossoverBase


class BlendCrossoverAlphaBeta(CrossoverBase):
    datatype = 'real'

    def crossover_function(self, ind, alpha=0.7, beta=0.5, **kwargs):
        x, y = [ind[0][0], ind[1][0]], [ind[1][0], ind[1][1]]
        dx, dy = abs(x[0] - x[1]), abs(y[0] - y[1])
        new_ind = []
        for i in range(2):
            new_ind.append([random.SystemRandom().uniform(min(x) - alpha * dx, max(x) + beta * dx),
                            random.SystemRandom().uniform(min(y) - alpha * dy, max(y) + beta * dy)])
        return new_ind
