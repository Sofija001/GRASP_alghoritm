import copy
import pandas as pd
import numpy as np
from scipy.spatial import distance
from scipy.spatial import distance_matrix
import random

def eucledian_distance(x, y):
    return distance.euclidean(x, y)

def calc_distance(data, city_tour):
    distance = 0
    for k in range(0, len(city_tour[0])-1):
        distance = distance + data[city_tour[0][k], city_tour[0][k+1]]
    return distance

def seed_function(data):
    seed = [[], float("inf")]
    sequence = random.sample(range(data.shape[0]), data.shape[0])
    sequence.append(sequence[0])
    seed[0] = sequence
    seed[1] = calc_distance(data, seed)
    return seed

def ranking(data, city=0):
    rank = np.zeros((data.shape[0], 2)) 
    for i in range(0, rank.shape[0]):
        rank[i,0] = data[i,city]
        rank[i,1] = i
    rank = rank[rank[:,0].argsort()]
    return rank

def restricted_candidate_list(data, greedines=0.5):
    seed = [[], float("inf")]
    sequence = []
    sequence.append(random.sample(list(range(0,data.shape[0])), 1)[0])
    
    for i in range(0, data.shape[0]):
        rand = random.uniform(0.0, 1.0)

        if(rand > greedines and len(sequence) <  data.shape[0]):
            ranked_cities = ranking(data, city=sequence[-1])

            for row in ranked_cities:
                candidate = int(row[1])
                if candidate not in sequence:
                    sequence.append(candidate)
                    break


        elif(rand <= greedines and len(sequence) < data.shape[0]):
            next_city = random.sample(list(range(0,data.shape[0])), 1)[0]
            while next_city in sequence:
                next_city = int(random.sample(list(range(0,data.shape[0])), 1)[0])
            sequence.append(next_city)

    sequence.append(sequence[0])
    seed[0] = sequence
    seed[1] = calc_distance(data, seed)
    return seed

def local_search_2_opt_simple(data, city_tour):

    best = copy.deepcopy(city_tour)

    for i in range(1, len(best[0]) - 2):
        for j in range(i+1, len(best[0]) - 1):

            candidate = copy.deepcopy(best)

            candidate[0][i:j+1] = list(reversed(candidate[0][i:j+1]))
            candidate[0][-1] = candidate[0][0]
            candidate[1] = calc_distance(data, candidate)

            if candidate[1] < best[1]:
                best = copy.deepcopy(candidate)

    return best

def grasp(data, initial_tour, iterations=50, rcl_size=10, greediness=0.8):

    best_solution = copy.deepcopy(initial_tour)

    for it in range(1, iterations+1):
        rcl_candidates = [restricted_candidate_list(data, greediness) for _ in range(rcl_size)]
        
        candidate = random.choice(rcl_candidates)
        
        improved_candidate = local_search_2_opt_simple(data, candidate)
        
        if improved_candidate[1] < best_solution[1]:
            best_solution = copy.deepcopy(improved_candidate)
        
        print(f"Iteration {it} -> Distance: {best_solution[1]:.2f}")

    print("Best Solution:", best_solution)
    return best_solution




