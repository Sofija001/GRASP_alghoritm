import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from brute_force import brute_force_emergency

def main():
    cost_matrix = np.array([
        [0, 10, 14, 10],
        [10, 0, 10, 14],
        [14, 10, 0, 10],
        [10, 14, 10, 0]
    ])

    reliability_penalty = [2, 2, 2, 2]

    route, cost = brute_force_emergency(cost_matrix, reliability_penalty)
    print("Test BF2")
    print("Cost matrix:\n", cost_matrix)
    print("Penalties:", reliability_penalty)
    print("Best route:", route)
    print("Best cost:", cost)

if __name__ == "__main__":
    main()
