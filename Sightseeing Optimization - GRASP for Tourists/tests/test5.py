import sys, os
import numpy as np
from matplotlib import pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grasp import grasp, seed_function, distance_matrix
from utils import plot_tour

tokyo_coords = np.array([
    [35.6586, 139.7454],  # Tokyo Tower
    [35.6764, 139.6993],  # Imperial Palace
    [35.7100, 139.8107],  # Asakusa Senso-ji
    [35.6895, 139.6917],  # Shinjuku
    [35.6938, 139.7034],  # Shibuya Crossing
    [35.6930, 139.7037],  # Hachiko Statue
    [35.6702, 139.7023],  # Meiji Shrine
    [35.6639, 139.7302],  # Harajuku
    [35.6329, 139.8804],  # Odaiba
    [35.7106, 139.7978],  # Tokyo Skytree
    [35.6852, 139.7528],  # Ginza
    [35.6581, 139.7516],  # Roppongi Hills
    [35.6320, 139.8810],  # Palette Town
    [35.6931, 139.7036],  # Dogenzaka
    [35.6998, 139.7745],  # Ueno Park
    [35.7013, 139.7740],  # Ameyoko Market
    [35.6840, 139.7520],  # Tokyo Station area
    [35.6610, 139.7310],  # Yoyogi Park
    [35.6595, 139.7005],  # Ebisu Garden Place
    [35.6739, 139.7100],  # Shinjuku Gyoen National Garden
])

data = distance_matrix(tokyo_coords, tokyo_coords)
seed = seed_function(data)
best_tour = grasp(data, seed, iterations=10, rcl_size=3, greediness=0.7)

print("Best tour:", best_tour[0])
print("Distance:", best_tour[1])

plot_tour(tokyo_coords, best_tour, title="Tourist Route in Tokyo")
