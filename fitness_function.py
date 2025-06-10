# fitness_function.py
# Computes fitness score based on emotional feedback and response quality

import numpy as np

def compute_valence_arousal_score(feedback):
    """
    Converts emotional feedback into a (valence, arousal) score.
    Higher valence = more positive emotion.
    Higher arousal = more energetic/intense response.
    """
    valence = feedback.get('valence', 0.0)  # Range: [-1.0, +1.0]
    arousal = feedback.get('arousal', 0.0)  # Range: [-1.0, +1.0]

    # Normalize to [0, 1]
    v_score = (valence + 1) / 2
    a_score = (arousal + 1) / 2
    return v_score, a_score

def compute_response_alignment(agent_response, expected_tone):
    """
    Measures how well agent's tone aligns with the target emotional state.
    """
    if agent_response['tone'] == expected_tone:
        return 1.0
    else:
        return 0.5  # Partial penalty for mismatch

def calculate_fitness(feedback, agent_response, expected_tone):
    """
    Final fitness = blend of:
    - valence-arousal positivity
    - tone alignment
    - response delay penalty (faster is better)
    """
    valence_score, arousal_score = compute_valence_arousal_score(feedback)
    alignment_score = compute_response_alignment(agent_response, expected_tone)
    
    delay_penalty = 1.0 - min(agent_response.get("delay", 0.5), 1.0)  # Lower delay is better

    # Weighted average of the components
    fitness = (
        0.4 * valence_score +
        0.3 * arousal_score +
        0.2 * alignment_score +
        0.1 * delay_penalty
    )
    return round(fitness, 3)

# Example usage
if __name__ == "__main__":
    feedback = {"valence": 0.6, "arousal": 0.2}
    agent_response = {"tone": "supportive", "delay": 0.3}
    expected_tone = "supportive"

    fitness_score = calculate_fitness(feedback, agent_response, expected_tone)
    print(f"Agent Fitness: {fitness_score}")
