import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from brute_force import brute_force_emergency

def main():
    np.random.seed(1)

    cost_matrix = np.random.randint(5, 30, size=(6, 6))
    np.fill_diagonal(cost_matrix, 0)

    reliability_penalty = np.random.randint(1, 10, size=6)

    route, cost = brute_force_emergency(cost_matrix, reliability_penalty)
    print("Test BF5")
    print("Cost matrix:\n", cost_matrix)
    print("Penalties:", reliability_penalty)
    print("Best route:", route)
    print("Best cost:", cost)

if __name__ == "__main__":
    main()
