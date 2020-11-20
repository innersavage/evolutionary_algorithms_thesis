import numpy as np

from crossover_operators.crossoverbase import CrossoverBase


class ElitistCrossover(CrossoverBase):
    datatype = 'real'

    def crossover_function(self, ind, crossover_function, evaluation_function, **kwargs):
        crossed = crossover_function(ind, **kwargs)
        if len(crossed[0]) > 1:
            ind += crossed
        else:
            ind += [crossed]
        ind_to_eval = [np.float64([np.float64(j[i]) for j in ind]) for i in range(len(ind[0]))]
        evaluation = evaluation_function(ind_to_eval)
        new_ind = []
        for i in range(2):
            idx = np.argmax(evaluation)
            evaluation = np.delete(evaluation, idx)
            new_ind.append(np.array(ind.pop(idx)))
        return new_ind
