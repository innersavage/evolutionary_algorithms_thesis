import unittest

from test_functions import *
from selection_methods import *
from crossover_operators import *
from mutation_operators import *


class TestAll(unittest.TestCase):
    test_functions = [rastrigin_func, bukin_f6_func, wolfe_func, easom_func, michalewicz_func]
    selection_methods = [roulette_selection, ranking_selection_linear, ranking_selection_nonlinear,
                         tournament_selection]
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
                        {'class': BitFlipMutation, 'params': {'p': 0.5}}]

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
                for mutation_method in self.mutation_methods:
                    print('Testing mutation_method method: {}'.format(mutation_method))
                    mutation = mutation_method['class']()
                    newpop = self.population.copy()
                    for i in range(10):
                        Y = rastrigin_func(newpop)
                        newpop, Y = repair_population(newpop, Y)
                        pick = func(newpop, Y, amount=100)
                        self.assertTrue(isinstance(pick, list))
                        for element in pick:
                            self.assertTrue(isinstance(element, list))
                        newpop = crossover.crossover(pick, evaluation_function=rastrigin_func, **crossover_method['params'])
                        self.assertTrue(isinstance(newpop, list))
                        newpop = mutation.mutate(newpop, **mutation_method['params'])
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
                for mutation_method in self.mutation_methods:
                    print('Testing mutation_method method: {}'.format(mutation_method))
                    mutation = mutation_method['class']()
                    newpop = self.population.copy()
                    for i in range(10):
                        Y = rastrigin_func(newpop)
                        newpop, Y = repair_population(newpop, Y)
                        pick = func(newpop, Y, amount=100)
                        self.assertTrue(isinstance(pick, list))
                        for element in pick:
                            self.assertTrue(isinstance(element, list))
                        newpop = elitist.crossover(pick, crossover_operator=crossover,
                                                   evaluation_function=rastrigin_func, **crossover_method['params'])
                        self.assertTrue(isinstance(newpop, list))
                        newpop = mutation.mutate(newpop, **mutation_method['params'])
                        self.assertTrue(isinstance(newpop, list))
                        for element in newpop:
                            self.assertTrue(isinstance(element, np.ndarray))


if __name__ == '__main__':
    unittest.main()
