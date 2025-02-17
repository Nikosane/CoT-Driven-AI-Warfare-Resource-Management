from agents.base_agent import BaseAgent
import random

class Spy(BaseAgent):
    def __init__(self, name, faction, memory_file):
        super().__init__(name, "Spy", memory_file)
        self.faction = faction
        self.memory.setdefault("missions", 0)
        self.memory.setdefault("successful_missions", 0)
        self.memory.setdefault("failed_missions", 0)
    
    def infiltrate(self, target_faction):
        """Attempts to infiltrate an enemy faction and gather intelligence."""
        success_chance = random.uniform(0.4, 0.9)
        outcome = "Success" if random.random() < success_chance else "Failure"
        
        self.memory["missions"] += 1
        if outcome == "Success":
            self.memory["successful_missions"] += 1
        else:
            self.memory["failed_missions"] += 1
        
        self.update_memory("last_infiltration", {
            "target": target_faction,
            "outcome": outcome
        })
        
        return f"{self.name} attempted to infiltrate {target_faction}. Result: {outcome}."
    
    def sabotage(self, target_faction):
        """Performs sabotage on an enemy faction."""
        success_chance = random.uniform(0.3, 0.7)
        outcome = "Sabotage Successful" if random.random() < success_chance else "Sabotage Failed"
        
        self.memory["missions"] += 1
        if outcome == "Sabotage Successful":
            self.memory["successful_missions"] += 1
        else:
            self.memory["failed_missions"] += 1
        
        self.update_memory("last_sabotage", {
            "target": target_faction,
            "outcome": outcome
        })
        
        return f"{self.name} sabotaged {target_faction}. Result: {outcome}."
    
    def think(self):
        """Spy's AI logic to decide next move."""
        return "Analyzing espionage opportunities..."
