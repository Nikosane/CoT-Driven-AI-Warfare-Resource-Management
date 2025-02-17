import ollama

class CoTReasoning:
    def __init__(self, model="deepseek-r1-1.5b"):
        self.model = model
    
    def generate_reasoning(self, prompt):
        """Generates a Chain of Thought reasoning response from the AI model."""
        response = ollama.chat(model=self.model, messages=[
            {"role": "system", "content": "You are an advanced AI specializing in strategic reasoning."},
            {"role": "user", "content": prompt}
        ])
        return response.get("message", {}).get("content", "No response generated.")

    def analyze_battle(self, situation):
        """Analyzes a battle scenario using CoT reasoning."""
        prompt = f"Analyze this battle scenario and suggest an optimal strategy: {situation}"
        return self.generate_reasoning(prompt)

    def assess_diplomacy(self, negotiation):
        """Evaluates a diplomatic situation and suggests an approach."""
        prompt = f"Evaluate this diplomatic scenario and provide a strategic response: {negotiation}"
        return self.generate_reasoning(prompt)

    def optimize_economy(self, economic_state):
        """Suggests an optimal economic strategy based on current conditions."""
        prompt = f"Given this economic state, suggest an optimal resource allocation: {economic_state}"
        return self.generate_reasoning(prompt)
