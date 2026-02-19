import os
from openai import OpenAI

class LLMInterface:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

    def generate_tasks(self, goal):
        prompt = f"""
        Break down the following goal into structured actionable tasks.
        Return as a numbered list.

        Goal:
        {goal}
        """

        response = self.client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[
                {"role": "system", "content": "You are a professional project planning assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content
