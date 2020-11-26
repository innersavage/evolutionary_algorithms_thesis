from .mutationbase import MutationBase
import random


class BitInsertionMutation(MutationBase):
    datatype = 'bin'

    def mutation_function(self, ind, **kwargs):
        insertion_point = random.SystemRandom().randint(0, len(ind) - 1)
        insertion_bit = random.SystemRandom().randint(0, 1)
        new_ind = ind[0:insertion_point] + str(insertion_bit) + ind[insertion_point + 1:]
        return new_ind
