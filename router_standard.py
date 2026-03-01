# router_standard.py

import random


class StandardRouter:
    def __init__(self, experts):
        self.experts = experts

    def route(self, token):
        """
        Standard routing:
        Random weighted selection (uniform for MVP)
        """
        expert = random.choice(self.experts)
        expert.activate()
        return expert
