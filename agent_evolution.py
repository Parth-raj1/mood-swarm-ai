# agent_evolution.py
# Evolves agents based on emotional feedback + swarm knowledge sharing

import random
import copy

class Agent:
    def __init__(self, tone, response_type, delay):
        self.tone = tone
        self.response_type = response_type
        self.delay = delay
        self.fitness = 0.0

    def mutate_based_on(self, feedback):
        """
        Mutate strategy based on valence/arousal feedback.
        Encourages more empathetic tones or faster responses.
        """
        valence = feedback.get('valence', 0.0)
        arousal = feedback.get('arousal', 0.0)

        if valence < 0:
            self.tone = random.choice(['supportive', 'reflective'])  # more empathy
        if arousal < -0.3:
            self.delay = max(0.0, self.delay - 0.1)  # respond faster under stress

        if random.random() < 0.2:
            self.response_type = random.choice(['supportive', 'motivational', 'reflective'])

    def share_strategies(self, knowledge_pool):
        """
        Share and absorb strategies from the swarm's knowledge pool.
        """
        if not knowledge_pool:
            return

        shared = random.choice(knowledge_pool)
        # Partial adoption of better strategies
        if shared.fitness > self.fitness:
            if random.random() < 0.5:
                self.tone = shared.tone
            if random.random() < 0.5:
                self.response_type = shared.response_type
            if random.random() < 0.5:
                self.delay = (self.delay + shared.delay) / 2

def evolve_agents(swarm, environment_feedback):
    """
    Mutates all agents and updates based on emotional feedback & peer strategies.
    """
    knowledge_pool = copy.deepcopy(swarm)  # Snapshot for peer learning
    for agent in swarm:
        agent.mutate_based_on(environment_feedback)
        agent.share_strategies(knowledge_pool)
