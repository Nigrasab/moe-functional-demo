# simulation.py

from experts import create_experts
from router_standard import StandardRouter
from router_functional import FunctionalRouter
from metrics import (
    compute_std,
    compute_entropy,
    effective_expert_count,
    gini_coefficient,
    top_k_share,
)


def run_simulation(router_class, steps=20000):
    experts = create_experts(64)
    router = router_class(experts)

    for i in range(steps):
        router.route(i)

    return {
        "std_dev": compute_std(experts),
        "entropy": compute_entropy(experts),
        "effective_experts": effective_expert_count(experts),
        "gini": gini_coefficient(experts),
        "top4_share": top_k_share(experts, 4),
    }


def main():
    print("Running Standard Router...")
    standard_metrics = run_simulation(StandardRouter)
    print("Standard:", standard_metrics)

    print("\nRunning Functional Router...")
    functional_metrics = run_simulation(FunctionalRouter)
    print("Functional:", functional_metrics)


if __name__ == "__main__":
    main()