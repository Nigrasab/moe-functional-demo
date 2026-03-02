# router_standard.py

import random


class StandardRouter:
    def __init__(self, experts, alpha=1.2):
        """
        alpha controls strength of positive feedback:

        alpha = 0   -> uniform routing
        alpha = 1   -> linear preference
        alpha > 1   -> strong collapse tendency
        """

        self.experts = experts
        self.alpha = alpha
        self.epsilon = 1e-6

    def route(self, token):
        weights = []

        for e in self.experts:
            weight = (e.activation_count + 1) ** self.alpha
            weights.append(weight + self.epsilon)

        total = sum(weights)
        r = random.random() * total

        cumulative = 0
        for expert, w in zip(self.experts, weights):
            cumulative += w
            if cumulative >= r:
                expert.activate()
                return expert

        expert = self.experts[-1]
        expert.activate()
        return expert