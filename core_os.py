"""
Core OS simulation module.
Includes basic file system simulation, process management, and environment variables.
"""

from cache import Cache
from ai_integration import AIIntegration

class SimulatedOS:
    def __init__(self):
        self.filesystem = {}
        self.processes = []
        self.env_vars = {}
        self.cache = Cache()
        self.ai = AIIntegration()
        self.memory = []

    def run(self):
        while True:
            command = input("sim-os> ")
            if command in ("exit", "quit"):
                print("")
                break
            else:
                user_input = command.strip()
                # Prepend instruction to act like Linux terminal with specific formatting and memory
                prompt = f"I want you to act as a linux terminal. (DON'T USE MARKDOWN) I will type commands and you will reply with what the terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. when i need to tell you something in english, i will do so by putting text inside curly brackets like this: {{}}. my command {user_input}"
                
                response = self.ai.get_ai_response_with_memory(prompt, self.memory)
                if response:
                    print(f"{response}")
                    self.cache.set(prompt, response)
                    self.memory.append({"role": "user", "content": prompt})
                    self.memory.append({"role": "assistant", "content": response})
                else:
                        print("Failed to get AI response.")
