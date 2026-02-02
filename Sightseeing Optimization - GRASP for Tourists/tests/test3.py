import sys, os
import numpy as np
from matplotlib import pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grasp import grasp, seed_function, distance_matrix
from utils import plot_tour

london_coords = np.array([
    [51.5007, -0.1246],  # Big Ben
    [51.5033, -0.1195],  # London Eye
    [51.5155, -0.0922],  # St Paul's Cathedral
    [51.5081, -0.0759],  # Tower of London
    [51.5076, -0.1280],  # Buckingham Palace
    [51.5094, -0.0760],  # Tower Bridge
    [51.5014, -0.1419],  # Victoria and Albert Museum
    [51.5194, -0.1270],  # British Museum
    [51.5035, -0.1196],  # Westminster Abbey
    [51.5070, -0.1280],  # Trafalgar Square
    [51.5100, -0.1340],  # National Gallery
    [51.5128, -0.0918],  # Sky Garden
    [51.5045, -0.0865],  # HMS Belfast
    [51.5142, -0.1175],  # Covent Garden
    [51.5008, -0.1246],  # Parliament
    [51.5194, -0.1240],  # Bloomsbury
    [51.5111, -0.1190],  # Soho
    [51.5080, -0.1281],  # Charing Cross
    [51.5074, -0.1278],  # City center
    [51.5125, -0.1270],  # Leicester Square
])

data = distance_matrix(london_coords, london_coords)
seed = seed_function(data)
best_tour = grasp(data, seed, iterations=50, rcl_size=3, greediness=0.7)

print("Best tour:", best_tour[0])
print("Distance:", best_tour[1])

plot_tour(london_coords, best_tour, title="Tourist Route in London")
