from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from recent_balls_service import get_recent_balls

app = FastAPI()

# -----------------------------
# Request Schema (Payload-based)
# -----------------------------

class BallEvent(BaseModel):
    ball: float
    runs_off_bat: int
    extras: int = 0
    extra_type: Optional[str] = None
    wicket: bool = False

class RecentBallsInput(BaseModel):
    match_id: str
    innings: int
    balls: List[BallEvent]
    limit: int = 6  # default: last over worth of balls

# -----------------------------
# API Route Layer
# -----------------------------

@app.post("/recent-balls")
def recent_balls(input_data: RecentBallsInput):
    """
    Returns most recent ball events for live match tracking.
    Fully integration-ready (no hardcoded sample data).
    """
    try:
        result = get_recent_balls(input_data.dict())
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
