from .mutationbase import MutationBase
import random
import numpy as np


class LocalGreedingMutation(MutationBase):
    datatype = 'bin'

    def mutation_function(self, ind, evaluation_function, **kwargs):
        for i in range(len(ind)):
            new_ind = [i for i in ind]
            new_ind[i] = '0' if new_ind[i] == '1' else '1'
            if evaluation_function([np.array(j) for j in self.binstring_to_genotype(ind)]) > \
                    evaluation_function([np.array(j) for j in self.binstring_to_genotype(''.join(new_ind))]):
                p = 0.2
            else:
                p = 0.5
            if random.SystemRandom().random() <= p:
                ind = ''.join(new_ind)
        return ind
