
# Script to calculate time consumption of each genetic algorithm

from test_functions import *
from selection_methods import *
from crossover_operators import *
from mutation_operators import *

import os
import sys

import numpy as np
np.errstate(all='raise')


test_functions = [{'class': Rastrigin, 'params': {'negative': True}},
                  {'class': Michalewicz, 'params': {'negative': True}},
                  {'class': BukinF6, 'params': {'negative': True}},
                  {'class': Easom, 'params': {'negative': True}}]
test_functions_3d = [{'class': Wolfe, 'params': {'negative': True}}]
selection_methods = [{'func': roulette_selection, 'name': 'Roulette Selection'},
                     {'func': ranking_selection_linear, 'name': 'Ranking Selection Linear'},
                     {'func': ranking_selection_nonlinear, 'name': 'Ranking Selection NonLinear'},
                     {'func': tournament_selection, 'name': 'Tournament Selection'}]
crossover_methods = [{'class': PointCrossover, 'params': {}},
                     {'class': KPointCrossover, 'params': {'k': 2}},
                     {'class': KPointCrossover, 'params': {'k': 3}},
                     {'class': ShuffleCrossover, 'params': {}},
                     {'class': AverageCrossover, 'params': {}},
                     {'class': BlendCrossoverAlphaBeta, 'params': {'alpha': 0.7, 'beta': 0.5}},
                     {'class': BlendCrossoverAlphaBeta, 'params': {'alpha': 0.4, 'beta': 0.7}},
                     {'class': DiscreteCrossover, 'params': {}},
                     {'class': HighlyDisruptiveCrossover, 'params': {}},
                     {'class': ReducedSurrogateCrossover, 'params': {}},
                     {'class': BlendCrossoverAlpha, 'params': {'alpha': 0.5}},
                     {'class': BlendCrossoverAlpha, 'params': {'alpha': 0.7}},
                     {'class': FlatCrossover, 'params': {}},
                     {'class': IntermediateCrossover, 'params': {}},
                     {'class': UniformCrossover, 'params': {'p': 0.5}},
                     {'class': UniformCrossover, 'params': {'p': 0.7}},
                     {'class': GaussianUniformCrossover, 'params': {}},
                     {'class': MicrobialCrossover, 'params': {'segment_length': 15}},
                     {'class': MicrobialCrossover, 'params': {'segment_length': 30}},
                     {'class': MicrobialCrossoverWithRand, 'params': {'segment_length': 15, 'p': 0.5}},
                     {'class': MicrobialCrossoverWithRand, 'params': {'segment_length': 15, 'p': 0.7}},
                     {'class': SphereCrossover1, 'params': {}},
                     {'class': SphereCrossover2, 'params': {}}]
mutation_methods = [{'class': NoMutation, 'params': {}},
                    {'class': BitFlipMutation, 'params': {'p': 0.1}},
                    {'class': BitFlipMutation, 'params': {'p': 0.2}},
                    {'class': BitFlipMutation, 'params': {'p': 0.5}},
                    {'class': BitInsertionMutation, 'params': {}},
                    {'class': CountPreservingMutation, 'params': {'p': 0.2}},
                    {'class': LocalGreedingMutation, 'params': {}},
                    {'class': GradientDescentTechniquesApproxMutation, 'params': {}}]
X1 = np.random.random_sample((100, 1)) * 200 - 100
X2 = np.random.random_sample((100, 1)) * 200 - 100
X3 = np.random.random_sample((100, 1)) * 200 - 100
population = [X1, X2]
population_3d = [X1, X2, X3]
path = os.path.dirname(os.path.abspath(__file__))


def run(test_functions, population):
    for testfunction in test_functions:
        test_function = testfunction['class'](**testfunction['params'])
        algo = 0
        for selectionmethod in selection_methods:
            selection_method = selectionmethod['func']
            for crossover_method in crossover_methods:
                crossover = crossover_method['class']()
                for mutation_method in mutation_methods:
                    algo += 1
                    # Verbose
                    print('\nCalculating {} of {}'.format(algo, testfunction['class'].__name__), end='')
                    # Create directory and result file and save calculation output
                    os.makedirs('{}/results_time/{}'.format(path, testfunction['class'].__name__),
                                exist_ok=True)
                    if not os.path.isfile('{}/results_time/{}/result_{}.csv'.format(path,
                                                                               testfunction['class'].__name__,
                                                                               algo)):
                        f = open('{}/results_time/{}/result_{}.csv'.format(path,
                                                                      testfunction['class'].__name__,
                                                                      algo), 'w')
                    else:
                        with open('{}/results_time/{}/result_{}.csv'.format(path,
                                                                      testfunction['class'].__name__,
                                                                      algo), 'r') as f:
                            if len(f.readlines()) > 10:
                                # Verbose
                                print(' Hooray! This one is already done!', end='')
                                continue
                        f = open('{}/results_time/{}/result_{}.csv'.format(path,
                                                                      testfunction['class'].__name__,
                                                                      algo), 'a')
                    # Preparation
                    mutation = mutation_method['class']()
                    newpop = population.copy()
                    # Magic loop which runs GA
                    import time
                    time_measure = None
                    for i in range(1, 11):
                        if time_measure is None:
                            time_measure = [time.process_time_ns()]
                        newpop = repair_population(newpop)
                        Y = test_function.calculate(newpop)
                        newpop, Y = repair_population(newpop, Y)
                        pick = selection_method(newpop, Y, amount=100)
                        newpop = crossover.crossover(pick, evaluation_function=test_function.calculate,
                                                     **crossover_method['params'])
                        newpop = mutation.mutate(newpop, evaluation_function=test_function.calculate,
                                                 **mutation_method['params'])
                        time_measure.append(time.process_time_ns())

                    # Save calculation result
                    for i in range(1, len(time_measure)):
                        f.write('{}\n'.format(time_measure[i] - time_measure[i-1]))
                    f.close()


if len(sys.argv) > 1:
    if sys.argv[1] == '1':
        func = [{'class': Rastrigin, 'params': {'negative': True}}]
    elif sys.argv[1] == '2':
        func = [{'class': Michalewicz, 'params': {'negative': True}}]
    elif sys.argv[1] == '3':
        func = [{'class': BukinF6, 'params': {'negative': True}}]
    elif sys.argv[1] == '4':
        func = [{'class': Easom, 'params': {'negative': True}}]
    elif sys.argv[1] == '5':
        func = test_functions_3d
        population = population_3d
    run(func, population)
else:
    print('Usage re-run.py [func_no]')
