import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grasp import grasp_emergency_network
from utils import build_distance_matrix
from utils import plot_communication_network
import numpy as np

def main():
    coords = np.array([
        [0, 0],
        [0, 10],
        [10, 10],
        [10, 0]
    ])
    cost_matrix = build_distance_matrix(coords)
    reliability_penalty = [5, 2, 4, 3]

    best_config = grasp_emergency_network(cost_matrix, reliability_penalty, iterations=10)
    print("Test1 - Best config:", best_config)
    plot_communication_network(coords, best_config, reliability_penalty)


if __name__ == "__main__":
    main()
