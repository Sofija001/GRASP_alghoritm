import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grasp import grasp_emergency_network
from utils import build_distance_matrix
from utils import plot_communication_network
import numpy as np

def main():
    np.random.seed(123)  

    coords = np.random.rand(12, 2) * 100
    cost_matrix = build_distance_matrix(coords)

    reliability_penalty = np.random.randint(5, 30, size=12)

    best_config = grasp_emergency_network(cost_matrix, reliability_penalty, iterations=30)

    print("\nTest Big - Best config:", best_config)
    plot_communication_network(coords, best_config, reliability_penalty)


if __name__ == "__main__":
    main()
