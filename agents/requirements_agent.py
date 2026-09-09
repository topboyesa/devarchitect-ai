import os
from dotenv import load_dotenv
from google import genai


# Load variables from .env
load_dotenv()


class RequirementsAgent:
    """
    AI-powered Requirements Agent.

    Analyzes software ideas and generates
    detailed project requirements.
    """

    def __init__(self):
        self.name = "Requirements Agent"

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found. Check your .env file."
            )

        self.client = genai.Client(api_key=api_key)

    def analyze(self, idea: str):

        prompt = f"""
You are a senior software requirements engineer.

Analyze the following software project idea:

"{idea}"

Provide a detailed analysis with these sections:

1. Project Summary
2. Problem Being Solved
3. Target Users
4. Functional Requirements
5. Non-Functional Requirements
6. MVP Features
7. Nice-to-Have Features
8. User Stories
9. Assumptions

Make the response practical and specific.

Return the answer in clean Markdown format.
"""

        response = self.client.models.generate_content(
         model="gemini-3.6-flash",
         contents=prompt
         )

        return {
            "agent": self.name,
            "idea": idea,
            "status": "success",
            "analysis": response.text
        }