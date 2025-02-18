import random
import json

class ReinforcementLearning:
    def __init__(self, memory_file):
        self.memory_file = memory_file
        self.q_table = self.load_memory()
    
    def load_memory(self):
        """Loads Q-learning memory from a JSON file."""
        try:
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_memory(self):
        """Saves Q-learning memory to a JSON file."""
        with open(self.memory_file, 'w') as f:
            json.dump(self.q_table, f, indent=4)
    
    def choose_action(self, state, actions, exploration_rate=0.1):
        """Selects an action using epsilon-greedy policy."""
        if random.random() < exploration_rate:
            return random.choice(actions)
        
        state_key = str(state)
        if state_key not in self.q_table:
            self.q_table[state_key] = {action: 0 for action in actions}
            return random.choice(actions)
        
        return max(self.q_table[state_key], key=self.q_table[state_key].get)
    
    def update_q_value(self, state, action, reward, next_state, learning_rate=0.1, discount_factor=0.9):
        """Updates Q-values based on agent experience."""
        state_key = str(state)
        next_state_key = str(next_state)
        
        if state_key not in self.q_table:
            self.q_table[state_key] = {action: 0}
        
        if next_state_key not in self.q_table:
            self.q_table[next_state_key] = {action: 0}
        
        old_value = self.q_table[state_key].get(action, 0)
        future_value = max(self.q_table[next_state_key].values(), default=0)
        new_value = old_value + learning_rate * (reward + discount_factor * future_value - old_value)
        self.q_table[state_key][action] = new_value
        
        self.save_memory()
    
    def think(self):
        """Placeholder for future decision-making logic."""
        return "Analyzing past experiences for optimal decision-making..."
