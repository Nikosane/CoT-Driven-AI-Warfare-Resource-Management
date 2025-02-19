import json

class GameState:
    """Handles saving and loading game progress."""
    
    def __init__(self, file_path="data/game_state.json"):
        self.file_path = file_path
    
    def save_state(self, state):
        with open(self.file_path, "w") as f:
            json.dump(state, f, indent=4)
    
    def load_state(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
