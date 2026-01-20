from fastapi import FastAPI
from pydantic import BaseModel
from app import run_agents

app = FastAPI(title="Agent Orchestration API")

class RequestBody(BaseModel):
    topic: str

@app.post("/run-agents")
def run_agent_api(request: RequestBody):
    return run_agents(request.topic)
