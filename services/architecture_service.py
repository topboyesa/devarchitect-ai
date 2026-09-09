from fastapi import FastAPI
from pydantic import BaseModel

from agents.architecture_agent import ArchitectureAgent


app = FastAPI(
    title="DevArchitect AI - Architecture Agent"
)


class ProjectRequest(BaseModel):
    idea: str


agent = ArchitectureAgent()


@app.get("/")
def home():

    return {
        "status": "online",
        "agent": agent.name
    }


@app.post("/design")
def design_architecture(request: ProjectRequest):

    result = agent.design(request.idea)

    return result