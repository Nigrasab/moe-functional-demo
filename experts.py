# experts.py

import random


class Expert:
    def __init__(self, expert_id, pair_id=None):
        self.id = expert_id
        self.pair_id = pair_id

        self.activation_count = 0
        self.integrity = 1.0  # starts healthy

    def activate(self):
        self.activation_count += 1
        self._update_integrity()

    def _update_integrity(self):
        """
        Integrity drops if expert is either:
        - Overused
        - Never used
        """
        # simple heuristic: deviation from mean load
        # will be updated globally in metrics
        pass

    def __repr__(self):
        return f"Expert(id={self.id}, pair={self.pair_id}, activations={self.activation_count})"


def create_experts(num_experts=64):
    experts = []

    for i in range(num_experts):
        experts.append(Expert(i))

    # assign complementary pairs
    # simple pairing: (0-1), (2-3), ...
    for i in range(0, num_experts, 2):
        experts[i].pair_id = i + 1
        experts[i + 1].pair_id = i

    return experts
