import numpy as np
import random
import math


def repair_population(population, evaluation_values=None):
    inf = np.array([np.inf])
    inf_minus = np.array([-np.inf])
    if evaluation_values is not None:
        evaluation_values[evaluation_values == inf] = np.nextafter(inf, 0)
        evaluation_values[evaluation_values == inf_minus] = np.nextafter(inf_minus, 0)
        idx = np.array([i if type(i) == np.bool_ else i[0] for i in np.isnan(evaluation_values)])
        new_population = []
        for i in population:
            i[i == inf] = np.nextafter(inf, 0)
            new_population.append(i[~idx])
        return new_population, evaluation_values[~idx]
    else:
        for i in population:
            i[i == inf] = np.nextafter(inf, 0)
            i[i == inf_minus] = np.nextafter(inf_minus, 0)
        return population


def roulette_spin(roulette_wheel):
    spin = random.SystemRandom().uniform(0, 100)
    for i, j in enumerate(roulette_wheel):
        if spin < j:
            return i


def roulette_selection(population, evaluation_values, amount=10):
    if not all([True if len(evaluation_values) == len(chromosomes) else False for chromosomes in population]):
        raise Exception
    sum_of_all = np.sum(evaluation_values)
    if sum_of_all in [np.float64('inf'), np.float64('-inf')]:
        sum_of_all = np.nextafter(sum_of_all, 0)
    # Below the edge case if sum_of_all equals zero
    if sum_of_all == 0:
        sum_of_all = 1
    probability = [i / sum_of_all for i in evaluation_values]
    roulette_wheel = [sum(probability[0:i]) * 100 for i in range(1, len(probability) + 1)]
    parent_population = [[] for i in range(len(population))]
    for i in range(amount):
        pick = roulette_spin(roulette_wheel)
        for j, chromosomes in enumerate(parent_population):
            chromosomes.append(population[j][pick])
    return parent_population


def ranking_selection(population, evaluation_values, amount=10, function=None, **kwargs):
    if not all([True if len(evaluation_values) == len(chromosomes) else False for chromosomes in population]):
        raise Exception
    ranking = evaluation_values.tolist()
    ranking.sort()
    parent_population = [[] for i in range(len(population))]
    i, j = len(ranking), 0
    last_index = (np.array(-1),)
    while len(parent_population[0]) < amount:
        f = function(i, len(ranking), **kwargs)
        i -= 1
        next_index = np.where(evaluation_values == ranking[i])
        j = j + 1 if (last_index[0].tolist() == next_index[0].tolist()) else 0
        last_index = next_index
        index = next_index[0][j]
        for k in range(math.ceil(f)):
            for l, chromosomes in enumerate(parent_population):
                chromosomes.append(population[l][index])
        if i == 0:
            i, j = len(ranking), 0
    return parent_population


def linear_function(i, K, SP=2):
    f = 2 - SP + (2 * (SP - 1) * i - 1) / (K - 1)
    return f


def ranking_selection_linear(population, evaluation_values, amount=10, **kwargs):
    return ranking_selection(population, evaluation_values, amount, function=linear_function, SP=2, **kwargs)


def nonlinear_function_X(K, SP=2):
    poly = [SP - K]
    for i in range(K-1):
        poly.append(SP)
    p = np.poly1d(poly)
    return p.r[0].real


def nonlinear_function(i, K, SP=2):
    X = nonlinear_function_X(K, SP)
    f = (K * pow(X, i - 1)) / sum([pow(X, j) for j in range(K)])
    return f


def ranking_selection_nonlinear(population, evaluation_values, amount=10, **kwargs):
    return ranking_selection(population, evaluation_values, amount, function=nonlinear_function, SP=2, **kwargs)


def tournament_selection(population, evaluation_values, amount=10, p=1, how_many_in_grp=4):
    if not all([True if len(evaluation_values) == len(chromosomes) else False for chromosomes in population]):
        raise Exception
    parent_population = [[] for i in range(len(population))]
    while len(parent_population[0]) < amount:
        group = []
        while len(group) < how_many_in_grp:
            pick = random.SystemRandom().randint(0, len(evaluation_values) - 1)
            if [pick, evaluation_values[pick]] not in group:
                group.append([pick, evaluation_values[pick]])
        group.sort(key=lambda a: a[1])
        probability = [sum([p * pow(1 - p, i) for i in range(how_many_in_grp)][i:how_many_in_grp])
                       for i in range(how_many_in_grp - 1, -1, -1)]
        pick = random.SystemRandom().uniform(0, 1)
        for i, j in enumerate(probability):
            if pick < j:
                for k, chromosomes in enumerate(parent_population):
                    chromosomes.append(population[k][group[i][0]])
                break
    return parent_population

