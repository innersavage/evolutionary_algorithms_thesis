from crossover_operators.crossoverbase import CrossoverBase


class AverageCrossover(CrossoverBase):
    datatype = 'real'

    def crossover_function(self, ind, **kwargs):
        return [[(ind[0][i] + ind[1][i]) / 2 for i in range(len(ind[0]))]]
