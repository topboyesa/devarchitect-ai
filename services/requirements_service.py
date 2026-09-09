from fastapi import FastAPI
from pydantic import BaseModel

from agents.requirements_agent import RequirementsAgent


app = FastAPI(
    title="DevArchitect AI - Requirements Agent"
)


class ProjectRequest(BaseModel):
    idea: str


agent = RequirementsAgent()


@app.get("/")
def home():
    return {
        "status": "online",
        "agent": agent.name
    }


@app.post("/analyze")
def analyze_project(request: ProjectRequest):
    try:
        result = agent.analyze(request.idea)
        return result

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }