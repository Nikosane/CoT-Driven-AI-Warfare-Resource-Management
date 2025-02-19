from models.cot_reasoning import CoTReasoning
from models.reinforcement_learning import ReinforcementLearning
import random

class EconomySimulation:
    def __init__(self, memory_file):
        self.cot = CoTReasoning()
        self.rl = ReinforcementLearning(memory_file)
    
    def manage_resources(self, faction, economy_context):
        """Simulates economic decision-making using CoT reasoning and reinforcement learning."""
        state = {"faction": faction, "economy_context": economy_context}
        actions = ["increase trade", "impose sanctions", "invest in military", "stockpile resources"]
        chosen_action = self.rl.choose_action(state, actions)
        
        cot_analysis = self.cot.evaluate_economy(f"Faction: {faction}, Context: {economy_context}, Action: {chosen_action}")
        
        outcome = "Profitable" if random.random() > 0.5 else "Loss"
        reward = 1 if outcome == "Profitable" else -1
        
        self.rl.update_q_value(state, chosen_action, reward, state)
        
        return {
            "action": chosen_action,
            "analysis": cot_analysis,
            "outcome": outcome
        }
