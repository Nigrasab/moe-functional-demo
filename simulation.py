# simulation.py

from experts import create_experts
from router_standard import StandardRouter
from router_functional import FunctionalRouter
from metrics import compute_std, compute_entropy, collapse_ratio


def run_simulation(router_class, steps=100000):
    experts = create_experts(64)
    router = router_class(experts)

    for i in range(steps):
        token = i  # dummy token
        router.route(token)

    std = compute_std(experts)
    entropy = compute_entropy(experts)
    collapse = collapse_ratio(experts)

    return {
        "std_dev": std,
        "entropy": entropy,
        "collapse_ratio": collapse
    }


if __name__ == "__main__":
    print("Running Standard Router...")
    standard_metrics = run_simulation(StandardRouter)
    print("Standard:", standard_metrics)

    print("\nRunning Functional Router...")
    functional_metrics = run_simulation(FunctionalRouter)
    print("Functional:", functional_metrics)
