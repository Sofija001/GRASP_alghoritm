import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from grasp import grasp, seed_function, distance_matrix
from utils import plot_tour

# Podaci za Rim
rome_coords = np.array([
    [41.9028, 12.4964],  # Colosseum
    [41.8902, 12.4922],  # Roman Forum
    [41.9009, 12.4833],  # Trevi Fountain
    [41.8986, 12.4768],  # Spanish Steps
    [41.9022, 12.4539],  # Vatican
    [41.9139, 12.4540],  # St. Peter's Basilica
    [41.8897, 12.4908],  # Circus Maximus
    [41.8955, 12.4823],  # Piazza Venezia
    [41.9109, 12.4765],  # Villa Borghese
    [41.9031, 12.4663],  # Castel Sant'Angelo
    [41.8789, 12.5091],  # EUR district
    [41.9320, 12.5336],  # Parioli
    [41.9444, 12.5049],  # Ponte Milvio
    [41.8667, 12.4667],  # Trastevere South
    [41.9200, 12.5200],  # Northeast Rome
    [41.8970, 12.4850],  # Pantheon
    [41.8899, 12.4920],  # Piazza Navona
    [41.8919, 12.5113],  # Basilica of Saint Paul Outside the Walls
    [41.9025, 12.4765],  # Piazza del Popolo
    [41.8989, 12.4769],  # Piazza di Spagna
])

data = distance_matrix(rome_coords, rome_coords)
seed = seed_function(data)
best_tour = grasp(data, seed, iterations=50, rcl_size=10, greediness=0.8)
print("Best tour:", best_tour[0])
print("Distance:", best_tour[1])

plot_tour(rome_coords, best_tour, title="Tourist Route in Rome")
