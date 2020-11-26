from .mutationbase import MutationBase
import random
import numpy as np


class GradientDescentTechniquesApproxMutation(MutationBase):
    datatype = 'bin'

    def mutation_function(self, ind, evaluation_function, **kwargs):
        mutation_point = random.SystemRandom().randint(0, len(ind) - 1)
        new_ind = [i for i in ind]
        new_ind[mutation_point] = '0' if new_ind[mutation_point] == '1' else '1'
        while evaluation_function([np.array(j) for j in self.binstring_to_genotype(ind)]) < \
                evaluation_function([np.array(j) for j in self.binstring_to_genotype(''.join(new_ind))]) \
                and 0 < mutation_point:
            ind = ''.join(new_ind)
            mutation_point -= 1
            new_ind[mutation_point] = new_ind[mutation_point + 1]
        return ''.join(new_ind)
