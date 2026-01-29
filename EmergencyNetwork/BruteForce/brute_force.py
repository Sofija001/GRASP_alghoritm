import itertools
import numpy as np

def brute_force_emergency(cost_matrix, reliability_penalty):
    n = len(cost_matrix)
    nodes = list(range(n))

    best_cost = float("inf")
    best_route = None

    for perm in itertools.permutations(nodes):
        cost = 0

        for i in range(n - 1):
            cost += cost_matrix[perm[i]][perm[i+1]]
            cost += reliability_penalty[perm[i]]

        cost += cost_matrix[perm[-1]][perm[0]]
        cost += reliability_penalty[perm[-1]]

        if cost < best_cost:
            best_cost = cost
            best_route = perm

    return best_route, best_cost


