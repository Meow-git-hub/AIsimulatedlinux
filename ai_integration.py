"""
AI integration module using text.pollinations.ai for random seed and content generation.
"""

import requests
import random
import urllib.parse

class AIIntegration:
    def __init__(self):
        self.api_base_url = "https://text.pollinations.ai/prompt/"

    def get_ai_response(self, user_input):
        # Generate a random seed number
        seed = random.randint(1000, 9999)
        # URL encode the user input for HTTPS request
        encoded_prompt = urllib.parse.quote(user_input)
        # Construct URL with seed as a query parameter
        url = f"{self.api_base_url}{encoded_prompt}?seed={seed}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip()
            else:
                print(f"AI API returned status code {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching AI data: {e}")
            return None

    def get_ai_response_with_memory(self, prompt, memory):
        # Combine memory and prompt into a single conversation string
        conversation = ""
        for entry in memory:
            role = entry.get("role", "")
            content = entry.get("content", "")
            conversation += f"{role}: {content}\n"
        conversation += f"user: {prompt}"

        # Generate a random seed number
        seed = random.randint(1000, 9999)
        # URL encode the conversation for HTTPS request
        encoded_conversation = urllib.parse.quote(conversation)
        # Construct URL with seed as a query parameter
        url = f"{self.api_base_url}{encoded_conversation}?seed={seed}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip()
            else:
                print(f"AI API returned status code {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching AI data: {e}")
            return None
