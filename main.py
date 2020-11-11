from test_functions import *
from selection_methods import *
import numpy as np

test_functions = [rastrigin_func, bukin_f6_func, wolfe_func, easom_func, michalewicz_func]
selection_methods = [roulette_selection, ranking_selection_linear, ranking_selection_nonlinear, tournament_selection]


X1 = np.random.rand(10, 1)
X2 = np.random.rand(10, 1)
population = [X1, X2]

Y = rastrigin_func(population)

pick = tournament_selection(population, Y, amount=10, p=0.7)
print(pick)
pick = ranking_selection_nonlinear(population, Y, amount=10)
print(pick)
pick = ranking_selection_linear(population, Y, amount=10)
print(pick)
pick = roulette_selection(population, Y, amount=10)
print(pick)