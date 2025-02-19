class OllamaWrapper:
    """Connects Deepseek R1 to AI decision-making."""
    
    def __init__(self, model_name="deepseek-r1-1.5b"):
        self.model_name = model_name
    
    def query(self, prompt):
        """Sends a query to the AI model and returns the response."""
        return f"[Ollama AI Response] {prompt}"
