import ollama
from tools import ToolSuite

class JarvisOrchestrator:
    def __init__(self):
        self.tools = ToolSuite()
        self.local_model = "llama3:8b"

    def process_command(self, text):
        # 1. Intent Routing via Ollama (Llama 3 8B)
        # We ask Ollama to return a JSON list of tasks
        prompt = f"Break this request into JSON sub-tasks: '{text}'. Tools: spotify, obs, web_search, vision, system."
        response = ollama.generate(model=self.local_model, prompt=prompt)
        
        # 2. Parallel Execution
        # (Simplified logic)
        if "spotify" in text.lower():
            self.tools.spotify_skip()
        if "browser" in text.lower():
            self.tools.open_browser()
            
        return "Tasks executed."
