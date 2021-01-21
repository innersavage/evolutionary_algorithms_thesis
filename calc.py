from test_functions import *
from selection_methods import *
from crossover_operators import *
from mutation_operators import *

import os
import sys
import csv

import numpy as np
np.errstate(all='raise')


test_functions = [{'class': Rastrigin, 'params': {'negative': True}, 'best': 0},
                  {'class': Michalewicz, 'params': {'negative': True}, 'best': -1.8013},
                  {'class': BukinF6, 'params': {'negative': True}, 'best': 0},
                  {'class': Easom, 'params': {'negative': True}, 'best': -1},
                  {'class': Wolfe, 'params': {'negative': True}, 'best': 0}]
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

def run(test_functions, population, offset_from=0, offset_to=200):
    results = {}
    for testfunction in test_functions:
        # test_function = testfunction['class'](**testfunction['params'])
        algo = 0
        for selectionmethod in selection_methods:
            # selection_method = selectionmethod['func']
            for crossover_method in crossover_methods:
                # crossover = crossover_method['class']()
                for mutation_method in mutation_methods:
                    algo += 1
                    if algo not in results:
                        results[algo] = {}
                    if testfunction['class'].__name__ + '_time_average_min' not in results:
                        results[testfunction['class'].__name__ + '_time_average_min'] = 99999999999999999999
                    if testfunction['class'].__name__ + '_time_average_max' not in results:
                        results[testfunction['class'].__name__ + '_time_average_max'] = 0
                    if testfunction['class'].__name__ + '_distance_min' not in results:
                        results[testfunction['class'].__name__ + '_distance_min'] = np.float128(99999999999999999999)
                    if testfunction['class'].__name__ + '_distance_max' not in results:
                        results[testfunction['class'].__name__ + '_distance_max'] = np.float128(0)
                    best_epoch = 0
                    best = np.array([])
                    best100 = np.array([])
                    best50 = np.array([])
                    with open('{}/results/{}/result_{}.csv'.format(path,
                                                                   testfunction['class'].__name__,
                                                                   algo), 'r') as csvfile:
                        dialect = csv.Sniffer().sniff(csvfile.readline())
                        csvfile.seek(0)
                        reader = csv.DictReader(csvfile, dialect=dialect)
                        for i, row in enumerate(reader, start=1):
                            print(algo)
                            best_epoch += int(row['Best in epoch'])
                            best = np.append(best, np.float128(row['Best']))
                            best100 = np.append(best100, np.float128(row['Best after 100 epoch']))
                            best50 = np.append(best50, np.float128(row['Best afer 50 epoch']))
                        best_epoch = best_epoch / i
                        if algo == 197:
                            pass
                        best = np.mean(best, dtype=np.float128)
                        best100 = np.mean(best100, dtype=np.float128)
                        best50 = np.mean(best50, dtype=np.float128)
                    with open('{}/results_time/{}/result_{}.csv'.format(path,
                                                                        testfunction['class'].__name__,
                                                                        algo), 'r') as csvfile:
                        time_average = 0
                        for i, j in enumerate(csvfile.readlines(), start=1):
                            time_average += int(j)
                        time_average = time_average / i
                        if time_average > results[testfunction['class'].__name__ + '_time_average_max']:
                            results[testfunction['class'].__name__ + '_time_average_max'] = time_average
                        if time_average < results[testfunction['class'].__name__ + '_time_average_min']:
                            results[testfunction['class'].__name__ + '_time_average_min'] = time_average
                        if (np.negative(best) - testfunction['best']) > \
                                results[testfunction['class'].__name__ + '_distance_max']:
                            results[testfunction['class'].__name__ + '_distance_max'] = \
                                (np.negative(best) - testfunction['best'])
                        if (np.negative(best) - testfunction['best']) < \
                                results[testfunction['class'].__name__ + '_distance_min']:
                            results[testfunction['class'].__name__ + '_distance_min'] = \
                                (np.negative(best) - testfunction['best'])

                    # Save calculation result
                    results[algo][testfunction['class'].__name__] = {
                        'best50': np.format_float_scientific(np.negative(best50), precision=4, exp_digits=3),
                        'best100': np.format_float_scientific(np.negative(best100), precision=4, exp_digits=3),
                        'best': np.format_float_scientific(np.negative(best), precision=4, exp_digits=3),
                        'best_epoch': best_epoch,
                        'distance_from_minimum': (np.negative(best) - testfunction['best']),
                        'algorithm': '{}_{}_{}_{}_{}'.format(selectionmethod['name'],
                                                             crossover_method['class'].__name__,
                                                             crossover_method['params'],
                                                             mutation_method['class'].__name__,
                                                             mutation_method['params']),
                        'average_epoch_time': time_average
                    }

    header = 'Algo;GA Combination;' \
             'Rastrigin_Best;Rastrigin_BestEpoch;Rastrigin_Best50;Rastrigin_Best100;' \
             'Rastrigin_AverageEpochTimeNormalized;Rastrigin_DistanceNormalized;' \
             'Michalewicz_Best;Michalewicz_BestEpoch;Michalewicz_Best50;Michalewicz_Best100;' \
             'Michalewicz_AverageEpochTimeNormalized;Michalewicz_DistanceNormalized;' \
             'BukinF6_Best;BukinF6_BestEpoch;BukinF6_Best50;BukinF6_Best100;' \
             'BukinF6_AverageEpochTimeNormalized;BukinF6_DistanceNormalized;' \
             'Easom_Best;Easom_BestEpoch;Easom_Best50;Easom_Best100;' \
             'Easom_AverageEpochTimeNormalized;Easom_DistanceNormalized;'
    resultfile = open('{}/results/consolidated_results.csv'.format(path), 'w')
    resultfile.write(header + '\n')
    for algo in range(1, 737):
        row = []
        for funcname in ['Rastrigin', 'Michalewicz', 'BukinF6', 'Easom']:
            row += [results[algo][funcname]['best'],
                    np.format_float_positional(results[algo][funcname]['best_epoch'], precision=4),
                    results[algo][funcname]['best50'],
                    results[algo][funcname]['best100'],
                    np.format_float_positional((results[algo][funcname]['average_epoch_time'] - 
                                                results['{}_time_average_min'.format(funcname)]) /
                                               (results['{}_time_average_max'.format(funcname)] - 
                                                results['{}_time_average_min'.format(funcname)]),
                                               precision=4),
                    np.format_float_positional((results[algo][funcname]['distance_from_minimum'] - 
                                                results['{}_distance_min'.format(funcname)]) /
                                               (results['{}_distance_max'.format(funcname)] - 
                                                results['{}_distance_min'.format(funcname)]), 
                                               precision=4)
                    ]
        resultfile.write('{};"{}";'
                         '"{}";{};"{}";"{}";{};{};'
                         '"{}";{};"{}";"{}";{};{};'
                         '"{}";{};"{}";"{}";{};{};'
                         '"{}";{};"{}";"{}";{};{}\n'.format(algo,
                                                            results[algo][funcname]['algorithm'],
                                                            *row
                                                            ))
    resultfile.close()


if len(sys.argv) > 1:
    offset_from = 0
    offset_to = 736
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
    if len(sys.argv) > 2:
        offset_from = int(sys.argv[2])
    if len(sys.argv) > 3:
        offset_to = int(sys.argv[3])
    run(func, population, offset_from, offset_to)
else:
    run(test_functions, population)
