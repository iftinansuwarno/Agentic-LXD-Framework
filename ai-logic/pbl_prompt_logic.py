class PBLPromptLibrary:
    """
    Library ini mengotomatisasi pembuatan prompt berdasarkan fase PBL
    sesuai dengan riset: 'Transforming Digital Literacy through ChatGPT-Assisted PBL'
    """
    
    def __init__(self, topic):
        self.topic = topic

    def get_phase_prompt(self, phase):
        prompts = {
            "orientation": f"I am studying {self.topic}. Can you explain which modern lifestyle factors contribute most to this issue in simple terms? [Goal: Activate curiosity]",
            "investigation": f"Explain the process of filtration in the glomerulus and how high blood pressure can permanently damage this structure for my research on {self.topic}. [Goal: Research Assistant]",
            "development": f"Our team wants to create a health campaign about {self.topic}. Provide 3 creative ideas that combine social media with physical activity. [Goal: Brainstorming Partner]",
            "reflection": "Identify one piece of information you just provided that might be a 'hallucination' or requires further academic verification. [Goal: Critical Evaluation]"
        }
        return prompts.get(phase, "Phase not found.")

# Simulasi Penggunaan
research = PBLPromptLibrary("Disorders of the Excretory System")
print("--- AI INTERACTION CYCLE (RESEARCH LOGIC) ---")
print(f"Phase 1 (Orientation): {research.get_phase_prompt('orientation')}")
print(f"Phase 3 (Development): {research.get_phase_prompt('development')}")
