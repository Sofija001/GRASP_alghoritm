import random
import copy
from utils import communication_cost

def initial_configuration(cost_matrix, reliability_penalty):
    config = [[], float("inf")]
    nodes = random.sample(
        list(range(1, cost_matrix.shape[0] + 1)),
        cost_matrix.shape[0]
    )
    nodes.append(nodes[0])  # povratak na start
    config[0] = nodes
    config[1] = communication_cost(cost_matrix, config, reliability_penalty)
    return config


def restricted_candidate_list_emergency(cost_matrix, reliability_penalty, greediness):
    config = [[], float("inf")]
    sequence = [random.randint(1, cost_matrix.shape[0])]

    while len(sequence) < cost_matrix.shape[0]:
        current = sequence[-1] - 1
        candidates = []

        for node in range(1, cost_matrix.shape[0] + 1):
            if node not in sequence:
                cost = cost_matrix[current, node - 1] + reliability_penalty[node - 1]
                candidates.append((node, cost))

        candidates.sort(key=lambda x: x[1])

        if random.random() > greediness:
            next_node = candidates[0][0]
        else:
            rcl_size = max(2, int(greediness * len(candidates)))
            next_node = random.choice(candidates[:rcl_size])[0]

        sequence.append(next_node)

    sequence.append(sequence[0])
    config[0] = sequence
    config[1] = communication_cost(cost_matrix, config, reliability_penalty)
    return config


def local_search_2_opt_emergency(cost_matrix, config, reliability_penalty):
    best = copy.deepcopy(config)
    improved = True

    while improved:
        improved = False
        for i in range(1, len(best[0]) - 2):
            for j in range(i + 1, len(best[0]) - 1):
                candidate = copy.deepcopy(best)
                #candidate[0][i:j] = reversed(candidate[0][i:j])
                candidate[0][i:j] = list(reversed(candidate[0][i:j]))
                candidate[1] = communication_cost(cost_matrix, candidate, reliability_penalty)

                if candidate[1] < best[1]:
                    best = copy.deepcopy(candidate)
                    improved = True
    return best


def grasp_emergency_network(cost_matrix, reliability_penalty, iterations=30):
    best_solution = initial_configuration(cost_matrix, reliability_penalty)
    no_improvement = 0

    for it in range(iterations):
        greediness = 0.9 - (it / iterations)

        candidate = restricted_candidate_list_emergency(cost_matrix, reliability_penalty, greediness)
        candidate = local_search_2_opt_emergency(cost_matrix, candidate, reliability_penalty)

        if candidate[1] < best_solution[1]:
            best_solution = copy.deepcopy(candidate)
            no_improvement = 0
        else:
            no_improvement += 1

        print(
            f"Iteration {it+1}: Candidate = {candidate[1]:.2f}, Best = {best_solution[1]:.2f}"
        )

        if no_improvement >= 15:
            print("Stopping early: no improvement in last 15 iterations.")
            break

    return best_solution
