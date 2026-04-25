from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class BallEvent(BaseModel):
    over: int = Field(..., ge=0)
    ball_in_over: int = Field(..., ge=1, le=6)
    over_ball: str
    striker: str
    bowler: str
    runs: int = Field(..., ge=0)
    extras: int = Field(..., ge=0)
    extra_type: Optional[str] = None  # wide, no_ball, bye, leg_bye
    wicket: int = Field(..., ge=0, le=1)

class RecentBallsRequest(BaseModel):
    innings_id: str
    limit: int
    ball_events: List[BallEvent]

    # Optional Khel AI extensions
    match: Optional[Dict] = None
    teams: Optional[Dict] = None
    players: Optional[Dict] = None
