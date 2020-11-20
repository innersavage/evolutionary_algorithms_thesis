from test_functions.test_functions import *
from selection_methods.selection_methods import *
import numpy as np

test_functions = [rastrigin_func, bukin_f6_func, wolfe_func, easom_func, michalewicz_func]
selection_methods = [roulette_selection, ranking_selection_linear, ranking_selection_nonlinear, tournament_selection]

X1 = np.random.random_sample((100, 1)) * 200 - 100
X2 = np.random.random_sample((100, 1)) * 200 - 100
population = [X1, X2]

Y = rastrigin_func(population)
print('----------------------------------------------------------')

temp = []

for func in selection_methods:
    for crossover in [PointCrossover]:
        crossover = crossover()
        newpop = population.copy()
        for i in range(100):
            Y = rastrigin_func(newpop)
            newpop, Y = repair_population(newpop, Y)
            pick = func(newpop, Y, amount=99)
            temp.append(pick.copy())
            newpop = crossover.crossover(pick)
        idx = np.argmax(Y)
        print(Y[idx].real, newpop[0][idx], newpop[1][idx], crossover, func)


# for func in selection_methods:
#     for crossover in crossover_methods:
#         newpop = population.copy()
#         for i in range(100):
#             Y = rastrigin_func(newpop)
#             newpop, Y = invalid_values_cleanup(newpop, Y)
#             pick = func(newpop, Y, amount=99)
#             temp.append(pick.copy())
#             newpop = crossover(pick)
#         idx = np.argmax(Y)
#         print(Y[idx].real, newpop[0][idx], newpop[1][idx], crossover, func)

