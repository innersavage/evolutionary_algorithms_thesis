import random

from crossover_operators.crossoverbase import CrossoverBase


class HighlyDisruptiveCrossover(CrossoverBase):
    datatype = 'bin'

    def crossover_function(self, ind, **kwargs):
        new_ind = [list(i) for i in ind]
        ind = [list(i) for i in ind]
        diff = 0
        for i in range(len(ind[0])):
            if ind[0][i] != ind[1][i]:
                diff += 1
        counter = 0
        while counter < int(diff / 2):
            for i in range(len(ind[0])):
                if new_ind[0][i] != new_ind[1][i] and new_ind[0][i] != ind[1][i] and random.SystemRandom().random() <= 0.5:
                    new_ind[0][i], new_ind[1][i] = ind[1][i], ind[0][i]
                    counter += 1
        return [''.join(i) for i in new_ind]
