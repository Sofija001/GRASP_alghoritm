import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grasp import grasp_emergency_network
from utils import build_distance_matrix
from utils import plot_communication_network
import numpy as np

def main():
    np.random.seed(2026)

    coords = np.random.rand(25, 2) * 100
    cost_matrix = build_distance_matrix(coords)

    reliability_penalty = np.random.randint(5, 40, size=25)

    best_config = grasp_emergency_network(cost_matrix, reliability_penalty, iterations=60)

    print("\nTest 25 Nodes - Best config:", best_config)
    plot_communication_network(coords, best_config, reliability_penalty)


if __name__ == "__main__":
    main()
