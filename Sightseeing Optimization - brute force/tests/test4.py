import sys, os
import numpy as np
from scipy.spatial import distance_matrix

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bruteforce import brute_force_tsp

tokyo_coords = np.array([
    [35.6586, 139.7454],  # Tokyo Tower
    [35.6764, 139.6993],  # Imperial Palace
    [35.7100, 139.8107],  # Asakusa
    [35.6895, 139.6917],  # Shinjuku
    [35.6938, 139.7034],  # Shibuya
    [35.6702, 139.7023],  # Meiji Shrine
    [35.6998, 139.7745],  # Ueno Park
    [35.7106, 139.7978],  # Tokyo Skytree
    [35.6852, 139.7528],  # Ginza
])

data = distance_matrix(tokyo_coords, tokyo_coords)

solution = brute_force_tsp(data)

print("TOKYO – Brute Force")
print("Route:", solution[0])
print("Distance:", solution[1])
