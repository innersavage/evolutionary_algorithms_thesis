from .crossoverbase import CrossoverBase
import random


class GaussianUniformCrossover(CrossoverBase):
    datatype = 'real'

    def crossover_function(self, ind, **kwargs):
        new_ind = [[], []]
        alpha = random.SystemRandom().random()
        for i in range(len(ind[0])):
            distance = abs(ind[0][i] - ind[1][i])
            if random.SystemRandom().random() <= 0.5:
                new_ind[0].append(ind[0][i] + alpha * distance / 3)
                new_ind[1].append(ind[1][i] + alpha * distance / 3)
            else:
                new_ind[0].append(ind[1][i] + alpha * distance / 3)
                new_ind[1].append(ind[0][i] + alpha * distance / 3)
        return new_ind
