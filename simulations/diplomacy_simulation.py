from models.cot_reasoning import CoTReasoning
from models.reinforcement_learning import ReinforcementLearning
import random

class DiplomacySimulation:
    def __init__(self, memory_file):
        self.cot = CoTReasoning()
        self.rl = ReinforcementLearning(memory_file)
    
    def negotiate(self, faction1, faction2, context):
        """Simulates a diplomatic negotiation using CoT reasoning and reinforcement learning."""
        state = {"faction1": faction1, "faction2": faction2, "context": context}
        actions = ["form alliance", "betray", "declare neutrality", "demand tribute"]
        chosen_action = self.rl.choose_action(state, actions)
        
        cot_analysis = self.cot.assess_diplomacy(f"Faction 1: {faction1}, Faction 2: {faction2}, Context: {context}, Action: {chosen_action}")
        
        outcome = "Success" if random.random() > 0.5 else "Failure"
        reward = 1 if outcome == "Success" else -1
        
        self.rl.update_q_value(state, chosen_action, reward, state)
        
        return {
            "action": chosen_action,
            "analysis": cot_analysis,
            "outcome": outcome
        }
