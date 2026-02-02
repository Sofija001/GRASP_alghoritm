import sys, os
import numpy as np
from matplotlib import pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grasp import grasp, seed_function, distance_matrix
from utils import plot_tour

nyc_coords = np.array([
    [40.7484, -73.9857],  # Empire State
    [40.6892, -74.0445],  # Statue of Liberty
    [40.7580, -73.9855],  # Times Square
    [40.7061, -74.0087],  # Wall Street
    [40.7829, -73.9654],  # Central Park
    [40.7615, -73.9777],  # Rockefeller Center
    [40.7527, -73.9772],  # Grand Central Terminal
    [40.7587, -73.9787],  # Broadway Theatre
    [40.7308, -73.9973],  # Washington Square Park
    [40.7127, -74.0134],  # One World Trade Center
    [40.7295, -73.9965],  # NYU
    [40.7411, -73.9897],  # Flatiron Building
    [40.7505, -73.9934],  # Madison Square Garden
    [40.8075, -73.9626],  # Columbia University
    [40.7489, -73.9680],  # Chrysler Building
    [40.7359, -74.0036],  # SoHo
    [40.7520, -73.9810],  # Bryant Park
    [40.7122, -74.0150],  # Battery Park
    [40.7589, -73.9851],  # Radio City Music Hall
    [40.7410, -73.9897],  # Madison Ave
])

data = distance_matrix(nyc_coords, nyc_coords)
seed = seed_function(data)
best_tour = grasp(data, seed, iterations=10, rcl_size=3, greediness=0.5)

print("Best tour:", best_tour[0])
print("Distance:", best_tour[1])

plot_tour(nyc_coords, best_tour, title="Tourist Route in New York")
