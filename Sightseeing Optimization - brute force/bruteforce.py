import itertools
import copy

def brute_force_tsp(data):
    
    n = data.shape[0]
    cities = list(range(n))

    best_tour = None
    best_distance = float("inf")

    for perm in itertools.permutations(cities[1:]):
        tour = [0] + list(perm) + [0]

        distance = 0
        for i in range(len(tour) - 1):
            distance += data[tour[i], tour[i + 1]]

        if distance < best_distance:
            best_distance = distance
            best_tour = tour

    return [best_tour, best_distance]
