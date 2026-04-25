from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import RecentBallsRequest
from services import validate_ball_events, get_recent_balls

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Recent Balls API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recent-balls")
def recent_balls(request: RecentBallsRequest):

    if not request.innings_id:
        raise HTTPException(status_code=400, detail="Missing innings_id")

    if request.limit is None:
        raise HTTPException(status_code=400, detail="Missing limit")

    if request.limit < 1 or request.limit > 12:
        raise HTTPException(status_code=400, detail="Limit must be between 1 and 12")

    if not request.ball_events:
        raise HTTPException(status_code=400, detail="ball_events cannot be empty")

    try:
        validate_ball_events(request.ball_events)
        result = get_recent_balls(request.ball_events, request.limit)

        return {
            "innings_id": request.innings_id,
            "recent_balls": result
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
