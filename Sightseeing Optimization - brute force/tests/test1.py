import sys, os
import numpy as np
from scipy.spatial import distance_matrix

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bruteforce import brute_force_tsp

rome_coords = np.array([
    [41.9028, 12.4964],  # Colosseum
    [41.8902, 12.4922],  # Roman Forum
    [41.9009, 12.4833],  # Trevi Fountain
    [41.8986, 12.4768],  # Spanish Steps
    [41.9022, 12.4539],  # Vatican
    [41.8897, 12.4908],  # Circus Maximus
    [41.8955, 12.4823],  # Piazza Venezia
    [41.9031, 12.4663],  # Castel Sant'Angelo
])

data = distance_matrix(rome_coords, rome_coords)

solution = brute_force_tsp(data)

print("ROME – Brute Force")
print("Route:", solution[0])
print("Distance:", solution[1])
