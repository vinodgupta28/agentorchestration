from fastapi import FastAPI
from pydantic import BaseModel
from app import run_agents  # Your actual backend logic

app = FastAPI(title="Agent Orchestration API")

# -----------------------------
# Request Body Model
# -----------------------------
class RequestBody(BaseModel):
    topic: str

# -----------------------------
# API Endpoint
# -----------------------------
@app.post("/run-agents")
def run_agent_api(request: RequestBody):
    """
    API endpoint to run the agent.
    Returns a dictionary with keys: research, summary, email.
    """
    try:
        # Call the backend function directly
        data = run_agents(request.topic)  # Must return dict {"research":..., "summary":..., "email":...}
        return data
    except Exception as e:
        return {"error": str(e)}
