import random
import struct

import numpy as np


class MutationBase:
    datatype = None

    def __init__(self):
        if getattr(self, 'datatype', None) not in ['real', 'bin', 'any']:
            raise Exception('Wrong mutation operator datatype (or not set)')

    def mutation_function(self, **kwargs):
        raise NotImplementedError

    @staticmethod
    def genotype_to_binstring(genotype):
        genotype_bytes = struct.pack('{}d'.format(len(genotype)), *genotype)
        binstring = ''
        for i in genotype_bytes:
            binstring += '{:08b}'.format(i)
        return binstring

    @staticmethod
    def binstring_to_genotype(binstring):
        binstrings = [binstring[i:i + 8] for i in range(0, len(binstring), 8)]
        genotype_bytes = b''
        for i in binstrings:
            genotype_bytes += int(i, 2).to_bytes(1, 'little')
        genotype = struct.unpack('{}d'.format(int(len(genotype_bytes) / 8)), genotype_bytes)
        return [np.float64(i) for i in genotype]

    def mutate(self, population, **kwargs):
        if self.datatype == 'real':
            return self.generic_mutate_real(population, **kwargs)
        elif self.datatype == 'bin':
            return self.generic_mutate(population, **kwargs)
        else:
            raise Exception('Wrong mutation operator datatype')

    def generic_mutate(self, population, **kwargs):
        population = [i.copy() for i in population]
        new_population = [[] for i in range(len(population))]
        for idx in range(len(population[0])):
            ind = [population[i][idx] for i in range(len(population))]
            new_ind = self.mutation_function(ind=self.genotype_to_binstring(ind), **kwargs)
            for i, chromosome in enumerate(self.binstring_to_genotype(new_ind)):
                new_population[i].append(np.array(chromosome))
        return [np.array(i) for i in new_population]

    def generic_mutate_real(self, population, **kwargs):
        population = [i.copy() for i in population]
        new_population = [[] for i in range(len(population))]
        for idx in range(len(population[0])):
            ind = [population[i][idx] for i in range(len(population))]
            new_ind = self.mutation_function(ind=ind, **kwargs)
            for i, chromosome in enumerate(new_ind):
                new_population[i].append(np.float64(chromosome))
        return [np.array(i) for i in new_population]
