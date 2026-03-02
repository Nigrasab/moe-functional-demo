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


def effective_expert_count(experts):
    """
    Perplexity-style measure:
    2^entropy
    Maximum = number of experts
    """

    entropy = compute_entropy(experts)
    return 2 ** entropy


def gini_coefficient(experts):
    """
    Measures inequality.
    0 = perfect equality
    1 = maximal inequality
    """

    loads = sorted(compute_distribution(experts))
    n = len(loads)
    total = sum(loads)

    if total == 0:
        return 0

    cumulative = 0
    for i, load in enumerate(loads, 1):
        cumulative += i * load

    gini = (2 * cumulative) / (n * total) - (n + 1) / n
    return gini


def top_k_share(experts, k=4):
    """
    Fraction of total load carried by top-k experts.
    """

    loads = sorted(compute_distribution(experts), reverse=True)
    total = sum(loads)

    if total == 0:
        return 0

    return sum(loads[:k]) / total