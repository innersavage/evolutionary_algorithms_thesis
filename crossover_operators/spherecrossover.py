from crossover_operators.crossoverbase import CrossoverBase
import math
import random


class SphereCrossover1(CrossoverBase):
    datatype = 'real'

    def crossover_function(self, ind, **kwargs):
        return [[math.sqrt(pow(ind[0][i] + ind[1][i], 2) / 2) for i in range(len(ind[0]))]]


class SphereCrossover2(CrossoverBase):
    datatype = 'real'

    def crossover_function(self, ind, **kwargs):
        alpha = random.SystemRandom().random()
        return [[math.sqrt(alpha * pow(ind[0][i], 2) + (1 - alpha) * pow(ind[1][i], 2)) for i in range(len(ind[0]))]]

