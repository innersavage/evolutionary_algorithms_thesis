import unittest

from test_functions import *
from selection_methods import *
from crossover_operators import *


class TestAll(unittest.TestCase):
    test_functions = [rastrigin_func, bukin_f6_func, wolfe_func, easom_func, michalewicz_func]
    selection_methods = [roulette_selection, ranking_selection_linear, ranking_selection_nonlinear,
                         tournament_selection]
    crossover_methods = [{'class': PointCrossover, 'params': {}},
                         {'class': KPointCrossover, 'params': {'k': 2}},
                         {'class': ShuffleCrossover, 'params': {}},
                         {'class': AverageCrossover, 'params': {}},
                         {'class': BlendCrossoverAlphaBeta, 'params': {'alpha': 0.7, 'beta': 0.5}},
                         {'class': DiscreteCrossover, 'params': {}},
                         {'class': HighlyDisruptiveCrossover, 'params': {}},
                         {'class': ReducedSurrogateCrossover, 'params': {}},
                         {'class': BlendCrossoverAlpha, 'params': {'alpha': 0.7}},
                         {'class': FlatCrossover, 'params': {}},
                         {'class': IntermediateCrossover, 'params': {}},
                         {'class': UniformCrossover, 'params': {'p': 0.7}}]

    def setUp(self):
        X1 = np.random.random_sample((100, 1)) * 200 - 100
        X2 = np.random.random_sample((100, 1)) * 200 - 100
        self.population = [X1, X2]

    def test_all_combinations(self):
        for func in self.selection_methods:
            print('Testing selection method: {}'.format(func))
            for crossover_method in self.crossover_methods:
                print('Testing crossover_method method: {}'.format(crossover_method))
                crossover = crossover_method['class']()
                newpop = self.population.copy()
                for i in range(10):
                    Y = rastrigin_func(newpop)
                    newpop, Y = repair_population(newpop, Y)
                    pick = func(newpop, Y, amount=100)
                    self.assertTrue(isinstance(pick, list))
                    for element in pick:
                        self.assertTrue(isinstance(element, list))
                    newpop = crossover.crossover(pick, **crossover_method['params'])
                    self.assertTrue(isinstance(newpop, list))
                    for element in newpop:
                        self.assertTrue(isinstance(element, np.ndarray))

    def test_elitistcrossover_all_combinations(self):
        elitist = ElitistCrossover()
        for func in self.selection_methods:
            print('Testing selection method: {}'.format(func))
            for crossover_method in self.crossover_methods:
                print('Testing crossover_method method: {}'.format(crossover_method))
                crossover = crossover_method['class']()
                newpop = self.population.copy()
                for i in range(10):
                    Y = rastrigin_func(newpop)
                    newpop, Y = repair_population(newpop, Y)
                    pick = func(newpop, Y, amount=100)
                    self.assertTrue(isinstance(pick, list))
                    for element in pick:
                        self.assertTrue(isinstance(element, list))
                    newpop = elitist.crossover(pick, crossover_function=crossover.crossover,
                                               evaluation_function=rastrigin_func, **crossover_method['params'])
                    self.assertTrue(isinstance(newpop, list))
                    for element in newpop:
                        self.assertTrue(isinstance(element, np.ndarray))


if __name__ == '__main__':
    unittest.main()
