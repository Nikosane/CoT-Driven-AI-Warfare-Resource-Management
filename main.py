from simulations.battle_simulation import BattleSimulation
from simulations.diplomacy_simulation import DiplomacySimulation
from simulations.economy_simulation import EconomySimulation
from utils.game_state import GameState
from utils.ollama_wrapper import OllamaWrapper
from utils.logging import log_message

def main():
    log_message("info", "Starting CoT-Driven AI Warfare & Resource Management Simulation")
    
    game_state = GameState()
    state = game_state.load_state()
    
    battle_sim = BattleSimulation()
    diplomacy_sim = DiplomacySimulation()
    economy_sim = EconomySimulation("data/agent_memory.json")
    ollama = OllamaWrapper()
    
    # Example: Simulating a battle round
    battle_result = battle_sim.simulate_battle("Faction A", "Faction B")
    log_message("info", f"Battle Result: {battle_result}")
    
    # Example: Simulating diplomacy
    diplomacy_result = diplomacy_sim.negotiate("Faction A", "Faction B")
    log_message("info", f"Diplomacy Outcome: {diplomacy_result}")
    
    # Example: Simulating economy
    economy_result = economy_sim.manage_resources("Faction A", "Stable Economy")
    log_message("info", f"Economic Decision: {economy_result}")
    
    # Save game state
    state["last_event"] = "Simulation cycle completed"
    game_state.save_state(state)
    log_message("info", "Game state saved successfully")
    
if __name__ == "__main__":
    main()
