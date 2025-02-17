from agents.base_agent import BaseAgent
import random

class Economist(BaseAgent):
    def __init__(self, name, faction, memory_file):
        super().__init__(name, "Economist", memory_file)
        self.faction = faction
        self.memory.setdefault("trade_deals", 0)
        self.memory.setdefault("economic_growth", 1.0)
        self.memory.setdefault("resource_allocations", {})
    
    def manage_resources(self):
        """Allocates resources efficiently for war and economy."""
        allocation = {
            "military": random.uniform(0.3, 0.7),
            "research": random.uniform(0.1, 0.4),
            "diplomacy": random.uniform(0.1, 0.3)
        }
        self.memory["resource_allocations"] = allocation
        self.update_memory("last_allocation", allocation)
        return f"{self.name} allocated resources: {allocation}"
    
    def negotiate_trade(self, partner_faction):
        """Attempts to secure a trade deal with another faction."""
        success_chance = random.uniform(0.4, 0.9)
        outcome = "Trade Successful" if random.random() < success_chance else "Trade Failed"
        
        if outcome == "Trade Successful":
            self.memory["trade_deals"] += 1
            self.memory["economic_growth"] *= random.uniform(1.02, 1.1)
        
        self.update_memory("last_trade", {
            "partner": partner_faction,
            "outcome": outcome
        })
        
        return f"{self.name} negotiated trade with {partner_faction}. Result: {outcome}."
    
    def think(self):
        """Economist's AI logic to decide next move."""
        return "Analyzing economic opportunities..."
