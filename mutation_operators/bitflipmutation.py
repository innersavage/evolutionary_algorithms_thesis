from .mutationbase import MutationBase
import random


class BitFlipMutation(MutationBase):
    datatype = 'bin'

    def mutation_function(self, ind, p, **kwargs):
        new_ind = ''
        for gene in ind:
            if random.SystemRandom().random() <= p:
                new_ind += '1' if gene in ['0', 0] else '0'
            else:
                new_ind += gene
        return new_ind
