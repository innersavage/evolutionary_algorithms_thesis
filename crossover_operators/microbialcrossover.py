from .crossoverbase import CrossoverBase
import random
import numpy as np


class MicrobialCrossover(CrossoverBase):
    datatype = 'bin'

    def crossover_function(self, ind, segment_length, evaluation_function, **kwargs):
        crossover_point = random.SystemRandom().randint(0, len(ind[0]) - segment_length)
        ind_to_eval = [np.float64([np.float64(j[i]) for j in ind]) for i in range(len(ind[0]))]
        evaluation = evaluation_function(ind_to_eval)
        if evaluation[0] >= evaluation[1]:
            new_ind = [ind[0], ind[1][0:crossover_point]
                       + ind[0][crossover_point:crossover_point+segment_length]
                       + ind[1][crossover_point+segment_length:]]
        else:
            new_ind = [ind[1], ind[0][0:crossover_point]
                       + ind[1][crossover_point:crossover_point + segment_length]
                       + ind[0][crossover_point + segment_length:]]
        return new_ind


class MicrobialCrossoverWithRand(CrossoverBase):
    datatype = 'bin'

    def crossover_function(self, ind, segment_length, evaluation_function, p=0.5, **kwargs):
        crossover_point = random.SystemRandom().randint(0, len(ind[0]) - segment_length)
        ind_to_eval = [np.float64([np.float64(j[i]) for j in ind]) for i in range(len(ind[0]))]
        evaluation = evaluation_function(ind_to_eval)
        if evaluation[0] >= evaluation[1]:
            new_ind = [ind[0], ind[1][0:crossover_point]
                       + ''.join([ind[0][i] if random.SystemRandom().random() <= p else
                                  ind[1][i] for i in range(crossover_point, crossover_point+segment_length)])
                       + ind[1][crossover_point+segment_length:]]
        else:
            new_ind = [ind[1], ind[0][0:crossover_point]
                       + ''.join([ind[1][i] if random.SystemRandom().random() <= p else
                                  ind[0][i] for i in range(crossover_point, crossover_point+segment_length)])
                       + ind[0][crossover_point + segment_length:]]
        return new_ind
