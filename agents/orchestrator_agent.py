import httpx


class OrchestratorAgent:
    """
    Coordinates all DevArchitect AI agents.
    """

    def __init__(self):
        self.name = "Orchestrator Agent"

        self.requirements_url = "http://127.0.0.1:8000/analyze"
        self.architecture_url = "http://127.0.0.1:8001/analyze"
        self.security_url = "http://127.0.0.1:8002/analyze"

    async def analyze(self, idea: str):

        async with httpx.AsyncClient(timeout=120.0) as client:

            # Requirements Agent
            requirements_response = await client.post(
                self.requirements_url,
                json={"idea": idea}
            )

            # Architecture Agent
            architecture_response = await client.post(
                self.architecture_url,
                json={"idea": idea}
            )

            # Security Agent
            security_response = await client.post(
                self.security_url,
                json={"idea": idea}
            )

        return {
            "agent": self.name,
            "project_idea": idea,

            "requirements_analysis": requirements_response.json(),

            "architecture_analysis": architecture_response.json(),

            "security_analysis": security_response.json()
        }