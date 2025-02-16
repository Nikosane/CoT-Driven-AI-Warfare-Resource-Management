from agents.base_agent import BaseAgent
import random

class General(BaseAgent):
    def __init__(self, name, faction, memory_file):
        super().__init__(name, "General", memory_file)
        self.faction = faction
        self.memory.setdefault("battles_fought", 0)
        self.memory.setdefault("victories", 0)
        self.memory.setdefault("defeats", 0)

    def plan_attack(self, enemy_faction):
        """Simulates an attack plan using Chain of Thought reasoning."""
        strategy = random.choice(["Blitzkrieg", "Defensive", "Guerilla", "Naval Invasion"])
        success_chance = random.uniform(0.4, 0.9)  # Dynamic probability
        result = "Victory" if random.random() < success_chance else "Defeat"
        
        self.memory["battles_fought"] += 1
        if result == "Victory":
            self.memory["victories"] += 1
        else:
            self.memory["defeats"] += 1
        
        self.update_memory("last_battle", {
            "enemy": enemy_faction,
            "strategy": strategy,
            "result": result
        })
        
        return f"{self.name} planned a {strategy} attack on {enemy_faction}. Result: {result}."

    def think(self):
        """General's AI logic to decide next move."""
        return "Analyzing battle scenarios..."
