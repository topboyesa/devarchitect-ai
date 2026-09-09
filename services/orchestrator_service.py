from fastapi import FastAPI
from pydantic import BaseModel

from agents.orchestrator_agent import OrchestratorAgent


app = FastAPI(
    title="DevArchitect AI - Orchestrator",
    description="Coordinates multiple AI software engineering agents"
)


class ProjectRequest(BaseModel):
    idea: str


agent = OrchestratorAgent()


@app.get("/")
def home():
    return {
        "status": "online",
        "agent": agent.name
    }


@app.post("/analyze")
async def analyze_project(request: ProjectRequest):

    result = await agent.analyze(request.idea)

    return result