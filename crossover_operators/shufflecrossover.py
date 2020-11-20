import random

from crossover_operators.pointcrossover import PointCrossover


class ShuffleCrossover(PointCrossover):
    datatype = 'bin'

    def point_crossover_function(self, ind, **kwargs):
        return super().crossover_function(ind)

    def crossover_function(self, ind, **kwargs):
        shuffle_pattern = []
        ind = [list(i) for i in ind]
        for i in range(len(ind[0])):
            pattern = [random.SystemRandom().randint(0, len(ind[0]) - 1), random.SystemRandom().randint(0, len(ind[0]) - 1)]
            pattern.sort()
            shuffle_pattern.insert(0, pattern)
            for j in ind:
                j[pattern[0]], j[pattern[1]] = j[pattern[1]], j[pattern[0]]
        ind = [''.join(i) for i in ind]
        ind = self.point_crossover_function(ind)
        ind = [list(i) for i in ind]
        for pattern in shuffle_pattern:
            for j in ind:
                j[pattern[0]], j[pattern[1]] = j[pattern[1]], j[pattern[0]]
        return [''.join(i) for i in ind]
