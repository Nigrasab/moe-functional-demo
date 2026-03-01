# metrics.py

import math
import statistics


def compute_distribution(experts):
    return [e.activation_count for e in experts]


def compute_std(experts):
    loads = compute_distribution(experts)
    return statistics.stdev(loads)


def compute_entropy(experts):
    loads = compute_distribution(experts)
    total = sum(loads)

    if total == 0:
        return 0

    entropy = 0
    for load in loads:
        if load > 0:
            p = load / total
            entropy -= p * math.log(p, 2)

    return entropy


def collapse_ratio(experts, threshold_ratio=0.8):
    """
    Measures how many experts carry 80% of load.
    Lower is worse (collapse).
    """
    loads = sorted(compute_distribution(experts), reverse=True)
    total = sum(loads)

    cumulative = 0
    count = 0

    for load in loads:
        cumulative += load
        count += 1
        if cumulative >= threshold_ratio * total:
            break

    return count / len(loads)
