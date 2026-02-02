import sys, os
import numpy as np
from matplotlib import pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grasp import grasp, seed_function, distance_matrix
from utils import plot_tour

paris_coords = np.array([
    [48.8584, 2.2945],   # Eiffel Tower
    [48.8529, 2.3499],   # Notre-Dame
    [48.8606, 2.3376],   # Louvre
    [48.8867, 2.3431],   # Sacré-Cœur
    [48.8738, 2.2950],   # Arc de Triomphe
    [48.8649, 2.3499],   # Palais Garnier
    [48.8570, 2.3522],   # Sainte-Chapelle
    [48.8530, 2.3497],   # Pont Neuf
    [48.8625, 2.2875],   # Trocadéro
    [48.8480, 2.3550],   # Panthéon
    [48.8730, 2.2955],   # Champs-Élysées
    [48.8640, 2.3180],   # Place de la Concorde
    [48.8635, 2.3200],   # Jardin des Tuileries
    [48.8732, 2.3030],   # Palais de Tokyo
    [48.8795, 2.3670],   # Montmartre Museum
    [48.8600, 2.3260],   # Orsay Museum
    [48.8700, 2.3600],   # Centre Pompidou
    [48.8575, 2.2955],   # Musée Rodin
    [48.8535, 2.3490],   # Sainte-Chapelle (dup)
    [48.8566, 2.3522],   # City center
])

data = distance_matrix(paris_coords, paris_coords)
seed = seed_function(data)
best_tour = grasp(data, seed, iterations=50, rcl_size=10, greediness=0.8)

print("Best tour:", best_tour[0])
print("Distance:", best_tour[1])

plot_tour(paris_coords, best_tour, title="Tourist Route in Paris")
