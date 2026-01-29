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
        [2, 0],
        [4, 0],
        [6, 0],
        [8, 0],
        [10, 0]
    ])
    cost_matrix = build_distance_matrix(coords)
    reliability_penalty = [1, 2, 1, 2, 1, 2]

    best_config = grasp_emergency_network(cost_matrix, reliability_penalty, iterations=12)
    print("Test3 - Best config:", best_config)
    plot_communication_network(coords, best_config, reliability_penalty)


if __name__ == "__main__":
    main()
