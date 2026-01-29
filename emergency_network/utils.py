import numpy as np
import matplotlib.pyplot as plt

def communication_cost(cost_matrix, config, reliability_penalty):
    total_cost = 0
    visited = set()

    for i in range(len(config[0]) - 1):
        a = config[0][i] - 1
        b = config[0][i + 1] - 1
        total_cost += cost_matrix[a, b]

        if a not in visited:
            total_cost += reliability_penalty[a]
            visited.add(a)

    return total_cost


def build_distance_matrix(coordinates):
    n = coordinates.shape[0]
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i, j] = np.linalg.norm(coordinates[i] - coordinates[j])
    return matrix


def plot_communication_network(coords, config, reliability_penalty):
    tour = config[0]
    start_node = tour[0] - 1 

    plt.figure(figsize=(9, 9))

    sizes = 300 + (reliability_penalty - np.min(reliability_penalty)) / (
        np.ptp(reliability_penalty) + 1e-6
    ) * 700

    scatter = plt.scatter(
        coords[:, 0],
        coords[:, 1],
        s=sizes,
        c=reliability_penalty,
        cmap="Reds",
        vmin=np.min(reliability_penalty),
        vmax=np.max(reliability_penalty),
        edgecolors="black",
        zorder=3
    )

    for i, (x, y) in enumerate(coords):
        plt.text(x + 1, y + 1, f"{i+1}", fontsize=10, weight="bold")

    for i in range(len(tour) - 1):
        a = tour[i] - 1
        b = tour[i + 1] - 1
        plt.plot(
            [coords[a][0], coords[b][0]],
            [coords[a][1], coords[b][1]],
            color="black",
            linewidth=2,
            alpha=0.8,
            zorder=2
        )

    plt.scatter(
        coords[start_node][0],
        coords[start_node][1],
        s=sizes[start_node] + 400,
        facecolors="none",
        edgecolors="blue",
        linewidths=2.5,
        label="Start node",
        zorder=4
    )

    plt.colorbar(scatter, label="Reliability penalty")

    plt.title("Emergency Communication Network – Optimal Configuration", fontsize=14)
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

