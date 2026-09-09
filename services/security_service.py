from fastapi import FastAPI
from pydantic import BaseModel

from agents.security_agent import SecurityAgent


app = FastAPI(
    title="DevArchitect AI - Security Agent"
)


class ProjectRequest(BaseModel):
    idea: str


agent = SecurityAgent()


@app.get("/")
def home():

    return {
        "status": "online",
        "agent": agent.name
    }


@app.post("/analyze-security")
def analyze_security(request: ProjectRequest):

    result = agent.analyze_security(request.idea)

    return result