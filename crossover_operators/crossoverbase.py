import random
import struct

import numpy as np


class CrossoverBase:
    datatype = None

    def __init__(self):
        if getattr(self, 'datatype', None) not in ['real', 'bin']:
            raise Exception('Wrong crossover operator datatype (or not set)')

    def crossover_function(self, **kwargs):
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

    def crossover(self, population, **kwargs):
        if self.datatype == 'real':
            return self.generic_crossover_real(population, **kwargs)
        elif self.datatype == 'bin':
            return self.generic_crossover(population, **kwargs)
        else:
            raise Exception('Wrong crossover operator datatype')

    def generic_crossover(self, population, **kwargs):
        population = [i.copy() for i in population]
        new_population = [[] for i in range(len(population))]
        while len(population[0]) > 1:
            ind = []
            if len(population[0]) == 1:
                for i in range(len(population)):
                    new_population[i].append(population[i][0])
                continue
            for j in range(2):
                pick = random.SystemRandom().randint(0, len(population[0]) - 1)
                parent = [population[i].pop(pick) for i in range(len(population))]
                ind.append(self.genotype_to_binstring(parent))
            ind = self.crossover_function(ind=ind, **kwargs)
            for genotype in ind:
                for i, chromosome in enumerate(self.binstring_to_genotype(genotype)):
                    new_population[i].append(np.array(chromosome))
        return [np.array(i) for i in new_population]

    def generic_crossover_real(self, population, **kwargs):
        population = [i.copy() for i in population]
        new_population = [[] for i in range(len(population))]
        while len(population[0]) > 1:
            ind = []
            if len(population[0]) == 1:
                for i in range(len(population)):
                    new_population[i].append(population[i][0])
                continue
            for j in range(2):
                pick = random.SystemRandom().randint(0, len(population[0]) - 1)
                parent = [population[i].pop(pick) for i in range(len(population))]
                ind.append(parent)
            ind = self.crossover_function(ind=ind, **kwargs)
            for genotype in ind:
                for i, chromosome in enumerate(genotype):
                    new_population[i].append(np.float64(chromosome))
        return [np.array(i) for i in new_population]
