# router_functional.py

import random
import statistics


class FunctionalRouter:
    def __init__(self, experts):
        self.experts = experts
        self.history = []
        self.history_limit = 50

    def route(self, token):
        """
        Functional routing:
        1. Prefer underused experts
        2. Maintain balance between complementary pairs
        3. Avoid deterministic repetition
        """

        # calculate mean load
        loads = [e.activation_count for e in self.experts]
        mean_load = statistics.mean(loads)

        # prefer experts below mean load
        candidates = [e for e in self.experts if e.activation_count <= mean_load]

        if not candidates:
            candidates = self.experts

        expert = random.choice(candidates)

        # Optional: activate complementary pair with small probability
        if random.random() < 0.1:
            pair = self.experts[expert.pair_id]
            pair.activate()
            self._remember(pair.id)
            return pair

        expert.activate()
        self._remember(expert.id)
        return expert

    def _remember(self, expert_id):
        self.history.append(expert_id)
        if len(self.history) > self.history_limit:
            self.history.pop(0)
