import numpy as np

from crossover_operators.crossoverbase import CrossoverBase


class ElitistCrossover(CrossoverBase):
    datatype = 'real'

    def crossover_function(self, ind, crossover_operator, evaluation_function, **kwargs):
        if crossover_operator.datatype == 'real':
            ind += crossover_operator.crossover_function(ind, evaluation_function=evaluation_function, **kwargs)
        elif crossover_operator.datatype == 'bin':
            ind_bin = [self.genotype_to_binstring(i) for i in ind]
            ind_bin_crossed = crossover_operator.crossover_function(ind_bin, evaluation_function=evaluation_function,
                                                                    **kwargs)
            ind += [self.binstring_to_genotype(i) for i in ind_bin_crossed]
        ind_to_eval = [np.float64([np.float64(j[i]) for j in ind]) for i in range(len(ind[0]))]
        evaluation = evaluation_function(ind_to_eval)
        new_ind = []
        for i in range(2):
            idx = np.argmax(evaluation)
            evaluation = np.delete(evaluation, idx)
            new_ind.append(np.array(ind.pop(idx)))
        return new_ind
