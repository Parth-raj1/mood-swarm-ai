# mood_swarm.py
# Created by Parth (2025) – original author. Not for commercial use.

import numpy as np
import time
import random
import matplotlib.pyplot as plt

# Define possible agent strategies
tones = ['friendly', 'clinical', 'cold']
response_types = ['supportive', 'reflective', 'motivational']
delays = [0, 1, 2, 3, 4]

# Generate agent
def create_agent():
    return {
        'tone': random.choice(tones),
        'response_type': random.choice(response_types),
        'delay': random.choice(delays)
    }

# Mutate agent with some randomness
def mutate(agent):
    new_agent = agent.copy()
    if np.random.rand() < 0.3:
        new_agent['tone'] = random.choice(tones)
    if np.random.rand() < 0.3:
        new_agent['response_type'] = random.choice(response_types)
    if np.random.rand() < 0.3:
        new_agent['delay'] = random.choice(delays)
    return new_agent

# Fitness function with slight randomness
def fitness_func(agent):
    tone_score = {'friendly': 1, 'clinical': 0.5, 'cold': -1}
    response_score = {'supportive': 2, 'reflective': 1, 'motivational': 1.5}
    delay_penalty = max(0, agent['delay'] - 2) * -0.2
    noise = np.random.normal(0, 0.1)
    score = tone_score[agent['tone']] + response_score[agent['response_type']] + delay_penalty + noise
    return score

# Swarm evolution setup
num_generations = 20
num_agents = 10
top_k = 3
best_fitness_per_gen = []

print("🚀 Launching mood-optimization swarm with mutation and noise...\n")

previous_top_agents = []

for gen in range(num_generations):
    agents = []
    for i in range(num_agents):
        if previous_top_agents and i < top_k:
            agent = mutate(previous_top_agents[i])  # carry + mutate
        else:
            agent = create_agent()
        agent['fitness'] = fitness_func(agent)
        agents.append(agent)

    agents.sort(key=lambda a: a['fitness'], reverse=True)
    best_fitness_per_gen.append(agents[0]['fitness'])
    previous_top_agents = agents[:top_k]

    print(f"✅ Generation {gen+1}: Best fitness {agents[0]['fitness']:.2f} | Strategy: Tone={agents[0]['tone']}, Type={agents[0]['response_type']}, Delay={agents[0]['delay']}s")

# Plot fitness trend
plt.plot(best_fitness_per_gen, marker='o')
plt.title("Best Agent Fitness Over Generations (with Mutation & Noise)")
plt.xlabel("Generation")
plt.ylabel("Mood Impact Score")
plt.grid(True)
plt.show()
