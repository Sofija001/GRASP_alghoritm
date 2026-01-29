import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from brute_force import brute_force_emergency

def main():
    cost_matrix = np.array([
        [0, 8, 15, 20, 6],
        [8, 0, 10, 14, 7],
        [15, 10, 0, 9, 12],
        [20, 14, 9, 0, 11],
        [6, 7, 12, 11, 0]
    ])

    reliability_penalty = [3, 5, 2, 4, 6]

    route, cost = brute_force_emergency(cost_matrix, reliability_penalty)
    print("Test BF4")
    print("Cost matrix:\n", cost_matrix)
    print("Penalties:", reliability_penalty)
    print("Best route:", route)
    print("Best cost:", cost)

if __name__ == "__main__":
    main()
