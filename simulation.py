# router_standard.py

import random


class StandardRouter:
    def __init__(self, experts):
        self.experts = experts

        # collapse bias configuration
        self.bias_probability = 0.7
        self.biased_group_size = 8

    def route(self, token):
        """
        Simulated collapse scenario.

        70% of tokens go to first 8 experts.
        30% distributed among remaining experts.

        This mimics expert dominance typical for real MoE collapse.
        """

        biased_group = self.experts[:self.biased_group_size]
        other_group = self.experts[self.biased_group_size:]

        if random.random() < self.bias_probability:
            expert = random.choice(biased_group)
        else:
            expert = random.choice(other_group)

        expert.activate()
        return expert
