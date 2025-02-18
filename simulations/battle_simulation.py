from models.cot_reasoning import CoTReasoning
from models.reinforcement_learning import ReinforcementLearning
import random

class BattleSimulation:
    def __init__(self, memory_file):
        self.cot = CoTReasoning()
        self.rl = ReinforcementLearning(memory_file)
    
    def simulate_battle(self, attacker, defender):
        """Simulates a battle scenario using CoT reasoning and reinforcement learning."""
        state = {"attacker": attacker, "defender": defender}
        actions = ["charge", "flank", "defend", "retreat"]
        chosen_action = self.rl.choose_action(state, actions)
        
        cot_analysis = self.cot.analyze_battle(f"Attacker: {attacker}, Defender: {defender}, Action: {chosen_action}")
        
        battle_outcome = "Victory" if random.random() > 0.5 else "Defeat"
        reward = 1 if battle_outcome == "Victory" else -1
        
        self.rl.update_q_value(state, chosen_action, reward, state)
        
        return {
            "action": chosen_action,
            "analysis": cot_analysis,
            "outcome": battle_outcome
        }
