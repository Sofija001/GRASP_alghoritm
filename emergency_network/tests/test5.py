import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grasp import grasp_emergency_network
from utils import build_distance_matrix
from utils import plot_communication_network
import numpy as np

def main():
    np.random.seed(2026)
    coords = np.random.rand(13, 2) * 100
    cost_matrix = build_distance_matrix(coords)
    reliability_penalty = np.random.randint(5, 25, size=13)

    best_config = grasp_emergency_network(cost_matrix, reliability_penalty, iterations=35)
    print("\nTest Big2 - Best config:", best_config)
    plot_communication_network(coords, best_config, reliability_penalty)


if __name__ == "__main__":
    main()
