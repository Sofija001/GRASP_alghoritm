import sys, os
import numpy as np
from scipy.spatial import distance_matrix

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bruteforce import brute_force_tsp

london_coords = np.array([
    [51.5007, -0.1246],  # Big Ben
    [51.5033, -0.1195],  # London Eye
    [51.5081, -0.0759],  # Tower of London
    [51.5094, -0.0760],  # Tower Bridge
    [51.5076, -0.1280],  # Buckingham Palace
    [51.5155, -0.0922],  # St Paul's Cathedral
    [51.5128, -0.0918],  # Millennium Bridge
    [51.5202, -0.0983],  # Barbican
])

data = distance_matrix(london_coords, london_coords)

solution = brute_force_tsp(data)

print("LONDON – Brute Force")
print("Route:", solution[0])
print("Distance:", solution[1])
