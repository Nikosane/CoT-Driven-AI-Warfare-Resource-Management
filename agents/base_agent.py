import json
import os

class BaseAgent:
    def __init__(self, name, role, memory_file):
        self.name = name
        self.role = role
        self.memory_file = memory_file
        self.memory = self.load_memory()
    
    def load_memory(self):
        """Loads agent memory from a JSON file."""
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as file:
                return json.load(file)
        return {}
    
    def save_memory(self):
        """Saves agent memory to a JSON file."""
        with open(self.memory_file, 'w') as file:
            json.dump(self.memory, file, indent=4)
    
    def update_memory(self, key, value):
        """Updates agent memory and saves it."""
        self.memory[key] = value
        self.save_memory()
    
    def think(self):
        """Placeholder for agent decision-making logic."""
        raise NotImplementedError("Each agent must implement its own 'think' method.")
