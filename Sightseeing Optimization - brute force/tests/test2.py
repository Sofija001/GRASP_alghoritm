import sys, os
import numpy as np
from scipy.spatial import distance_matrix

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bruteforce import brute_force_tsp

paris_coords = np.array([
    [48.8584, 2.2945],  # Eiffel Tower
    [48.8529, 2.3499],  # Notre-Dame
    [48.8606, 2.3376],  # Louvre
    [48.8867, 2.3431],  # Sacré-Cœur
    [48.8738, 2.2950],  # Arc de Triomphe
    [48.8649, 2.3499],  # Palais Garnier
    [48.8570, 2.3522],  # Sainte-Chapelle
    [48.8610, 2.3358],  # Tuileries Garden
    [48.8462, 2.3371],  # Pantheon
])

data = distance_matrix(paris_coords, paris_coords)

solution = brute_force_tsp(data)

print("PARIS – Brute Force")
print("Route:", solution[0])
print("Distance:", solution[1])
