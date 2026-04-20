from typing import Dict, Any, List

# ----------------------------------------
# Business Logic Layer (Reusable Core)
# ----------------------------------------

def get_recent_balls(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extracts the most recent ball events from match data.

    Fully decoupled from API layer for reuse in:
    - Django backend
    - Live match feeds
    - AI summarization modules
    """

    balls: List[Dict[str, Any]] = payload["balls"]
    limit: int = payload.get("limit", 6)

    # Sort balls by delivery sequence (float-based over.ball)
    sorted_balls = sorted(balls, key=lambda x: x["ball"])

    recent = sorted_balls[-limit:]

    processed = []

    for b in recent:
        processed.append({
            "ball": b["ball"],
            "runs": b["runs_off_bat"],
            "extras": b.get("extras", 0),
            "extra_type": b.get("extra_type"),
            "wicket": b.get("wicket", False),
            "total": b["runs_off_bat"] + b.get("extras", 0)
        })

    return {
        "match_id": payload["match_id"],
        "innings": payload["innings"],
        "limit": limit,
        "recent_balls": processed
    }
