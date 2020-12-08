from .mutationbase import MutationBase
import random


class CountPreservingMutation(MutationBase):
    datatype = 'bin'

    def mutation_function(self, ind, p, **kwargs):
        new_ind = [i for i in ind]
        for i, j in enumerate(new_ind):
            if random.SystemRandom().random() <= p:
                new_ind[i] = '0' if j == '1' else '1'
                balance = False
                while balance is False:
                    k = random.SystemRandom().randint(0, len(ind) - 1)
                    if new_ind[k] == new_ind[i]:
                        new_ind[k] = '0' if new_ind[i] == '1' else '1'
                        balance = True
        return ''.join(new_ind)
