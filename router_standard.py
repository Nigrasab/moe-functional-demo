# router_standard.py

import random


class StandardRouter:
    def __init__(self, experts):
        self.experts = experts
        self.epsilon = 1e-6  # small value to avoid zero probability

    def route(self, token):
        """
        Popularity-based routing (positive feedback).

        Probability of selecting an expert grows with its activation count.
        This simulates real softmax-based MoE collapse behaviour.
        """

        weights = []
        for e in self.experts:
            weights.append(e.activation_count + self.epsilon)

        total = sum(weights)
        r = random.random() * total

        cumulative = 0
        for expert, w in zip(self.experts, weights):
            cumulative += w
            if cumulative >= r:
                expert.activate()
                return expert

        # fallback
        expert = self.experts[-1]
        expert.activate()
        return expert