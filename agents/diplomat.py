from agents.base_agent import BaseAgent
import random

class Diplomat(BaseAgent):
    def __init__(self, name, faction, memory_file):
        super().__init__(name, "Diplomat", memory_file)
        self.faction = faction
        self.memory.setdefault("negotiations", 0)
        self.memory.setdefault("alliances_formed", 0)
        self.memory.setdefault("betrayals", 0)

    def negotiate(self, other_faction):
        """Attempts to negotiate an alliance or trade deal."""
        success_chance = random.uniform(0.3, 0.8)
        outcome = "Alliance Formed" if random.random() < success_chance else "Negotiation Failed"
        
        self.memory["negotiations"] += 1
        if outcome == "Alliance Formed":
            self.memory["alliances_formed"] += 1
            self.update_memory("last_negotiation", {
                "faction": other_faction,
                "outcome": "Alliance Formed"
            })
        else:
            self.update_memory("last_negotiation", {
                "faction": other_faction,
                "outcome": "Failed"
            })
        
        return f"{self.name} negotiated with {other_faction}. Result: {outcome}."
    
    def betray(self, ally_faction):
        """Decides to betray an ally for strategic gain."""
        self.memory["betrayals"] += 1
        self.update_memory("last_betrayal", {
            "faction": ally_faction,
            "outcome": "Betrayed"
        })
        
        return f"{self.name} has betrayed {ally_faction}!"
    
    def think(self):
        """Diplomat's AI logic to decide next move."""
        return "Analyzing diplomatic relations..."
