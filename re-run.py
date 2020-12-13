
# Alternative script to re-run calculations for operators which have been changed due to bugs
blend_and_flat_to_re_run = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 81, 82, 83, 84, 85, 86, 87,
                            88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 225, 226, 227, 228,
                            229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 265, 266, 267, 268, 269, 270,
                            271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288,
                            409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 449, 450,
                            451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468,
                            469, 470, 471, 472, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606,
                            607, 608, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648,
                            649, 650, 651, 652, 653, 654, 655, 656]
microbial_and_gaussian_to_re_run = [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145,
                                    146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162,
                                    163, 164, 165, 166, 167, 168, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323,
                                    324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340,
                                    341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 497, 498, 499, 500, 501,
                                    502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518,
                                    519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535,
                                    536, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696,
                                    697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713,
                                    714, 715, 716, 717, 718, 719, 720]
Rastrigin_to_re_run = [225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 265, 266, 267,
                       268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286,
                       287, 288, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 449,
                       450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468,
                       469, 470, 471, 472, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606,
                       607, 608, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648,
                       649, 650, 651, 652, 653, 654, 655, 656, 313, 314, 315, 316, 317, 318, 319, 320,
                       321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339,
                       340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 497, 498, 499, 500, 501,
                       502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520,
                       521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 681, 682, 683,
                       684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699]
Michalewicz_to_re_run = [100, 101, 102, 103, 104, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238,
                         239, 240, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281,
                         282, 283, 284, 285, 286, 287, 288, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138,
                         139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157,
                         158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 313, 314, 315, 316, 317, 318, 319, 320,
                         321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339,
                         340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 497, 498, 499, 500, 700, 701,
                         702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720]
BukinF6_to_re_run = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 81, 82, 83, 84, 85, 86, 87,
                     88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 225, 226, 227, 228,
                     229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 265, 266, 267, 268, 269, 270, 271, 272,
                     273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 129, 130, 131, 132,
                     133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152,
                     153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 313, 314, 315, 316,
                     317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336,
                     337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 497, 498, 499, 500,
                     501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518,
                     519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535,
                     536, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696,
                     697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713,
                     714, 715, 716, 717, 718, 719, 720]
Easom_to_re_run = [313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332,
                   333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352,
                   497, 498, 499, 500, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715,
                   716, 717, 718, 719, 720]
Wolfe_to_re_run = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 25, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236,
                   237, 238, 239, 240, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280,
                   281, 282, 283, 284, 285, 286, 287, 288]

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



def create_gaindex():
    header = 'L.p.;Metoda selekcji;Operator Krzyżowania;Parametry operatora krzyżowania;Operator Mutacji;Parametry operatora mutacji'
    algo = 0
    f = open(os.path.dirname(__file__) + '/results/ga_index.csv', 'w')
    f.write(header + '\n')
    for selection_method in selection_methods:
        for crossover_method in crossover_methods:
            for mutation_method in mutation_methods:
                algo += 1
                f.write('{};{};{};{};{};{}\n'.format(algo,
                                                 selection_method['name'],
                                                 crossover_method['class'].__name__,
                                                 crossover_method['params'],
                                                 mutation_method['class'].__name__,
                                                 mutation_method['params']))
    f.close()


def run(test_functions, population, scope):
    header = 'Algo;Best afer 50 epoch;Best after 100 epoch;Best;Best in epoch;GA Combination'
    for testfunction in test_functions:
        test_function = testfunction['class'](**testfunction['params'])
        algo = 0
        for selectionmethod in selection_methods:
            selection_method = selectionmethod['func']
            for crossover_method in crossover_methods:
                crossover = crossover_method['class']()
                for mutation_method in mutation_methods:
                    algo += 1
                    # Offset if chunk set (idea to run calculation on multiple hosts)
                    if algo not in scope:
                        continue
                    # Verbose
                    print('\nCalculating {} of {}'.format(algo, testfunction['class'].__name__), end='')
                    # Create directory and result file and save calculation output
                    os.makedirs('{}/results_rerun/{}'.format(path, testfunction['class'].__name__),
                                exist_ok=True)
                    if not os.path.isfile('{}/results_rerun/{}/result_{}.csv'.format(path,
                                                                               testfunction['class'].__name__,
                                                                               algo)):
                        f = open('{}/results_rerun/{}/result_{}.csv'.format(path,
                                                                      testfunction['class'].__name__,
                                                                      algo), 'w')
                        f.write(header + '\n')
                    else:
                        with open('{}/results_rerun/{}/result_{}.csv'.format(path,
                                                                      testfunction['class'].__name__,
                                                                      algo), 'r') as f:
                            if len(f.readlines()) > 100:
                                # Verbose
                                print(' Hooray! This one is already done!', end='')
                                continue
                        f = open('{}/results_rerun/{}/result_{}.csv'.format(path,
                                                                      testfunction['class'].__name__,
                                                                      algo), 'a')
                    # Preparation
                    best50, best100, best, best_epoch = None, None, None, None
                    mutation = mutation_method['class']()
                    newpop = population.copy()
                    # Magic loop which runs GA
                    for i in range(1, 101):
                        # Verbose
                        print('.', end='')
                        sys.stdout.flush()
                        newpop = repair_population(newpop)
                        Y = test_function.calculate(newpop)
                        newpop, Y = repair_population(newpop, Y)
                        if best is None or Y.max() > best:
                            best = Y.max()
                            best_epoch = i
                        if i == 50:
                            best50 = Y.max()
                        elif i == 100:
                            best100 = Y.max()
                        pick = selection_method(newpop, Y, amount=100)
                        newpop = crossover.crossover(pick, evaluation_function=test_function.calculate,
                                                     **crossover_method['params'])
                        newpop = mutation.mutate(newpop, evaluation_function=test_function.calculate,
                                                 **mutation_method['params'])
                    # Save calculation result
                    f.write('{};{};{};{};{};{}_{}_{}_{}_{}\n'.format(algo,
                                                                   best50.astype(str),
                                                                   best100.astype(str),
                                                                   best.astype(str),
                                                                   best_epoch,
                                                                   selectionmethod['name'],
                                                                   crossover_method['class'].__name__,
                                                                   crossover_method['params'],
                                                                   mutation_method['class'].__name__,
                                                                   mutation_method['params']))
                    f.close()


if len(sys.argv) > 1:
    if sys.argv[1] == '1':
        scope = Rastrigin_to_re_run
        func = [{'class': Rastrigin, 'params': {'negative': True}}]
    elif sys.argv[1] == '2':
        scope = Michalewicz_to_re_run
        func = [{'class': Michalewicz, 'params': {'negative': True}}]
    elif sys.argv[1] == '3':
        scope = BukinF6_to_re_run
        func = [{'class': BukinF6, 'params': {'negative': True}}]
    elif sys.argv[1] == '4':
        scope = Easom_to_re_run
        func = [{'class': Easom, 'params': {'negative': True}}]
    elif sys.argv[1] == '5':
        scope = Wolfe_to_re_run
        func = test_functions_3d
        population = population_3d
    run(func, population, scope)
else:
    print('Usage re-run.py [func_no]')
