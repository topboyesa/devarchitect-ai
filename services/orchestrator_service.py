from fastapi import FastAPI
from pydantic import BaseModel
from agents.orchestrator_agent import OrchestratorAgent
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="DevArchitect AI - Orchestrator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
def analyze_project(request: ProjectRequest):
    result = agent.analyze(request.idea)
    return result