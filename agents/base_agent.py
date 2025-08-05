import json
import requests
from typing import Dict, Any, List
from config import Config

class BaseAgent:
    def __init__(self, model: str = None):
        self.api_key = Config.OPENROUTER_API_KEY
        self.base_url = Config.OPENROUTER_BASE_URL
        self.model = model or Config.ANALYSIS_MODEL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": Config.SITE_URL,
            "X-Title": Config.SITE_NAME,
            "Content-Type": "application/json"
        }
    
    async def call_llm(self, messages: List[Dict[str, str]], temperature: float = 0.7) -> str:
        """Make a call to the OpenRouter API"""
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Error calling LLM: {e}")
            return ""
    
    def parse_json_response(self, response: str) -> Dict[str, Any]:
        """Parse JSON response from LLM"""
        try:
            # Try to extract JSON from the response
            if "```json" in response:
                json_str = response.split("```json")[1].split("```")[0].strip()
            elif "```" in response:
                json_str = response.split("```")[1].strip()
            else:
                json_str = response.strip()
            
            return json.loads(json_str)
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            return {} 