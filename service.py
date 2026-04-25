from typing import List, Dict

def validate_ball_events(ball_events: List[Dict]):
    seen = set()

    for ball in ball_events:
        key = (ball["over"], ball["ball_in_over"])

        if key in seen:
            raise ValueError(f"Duplicate ball detected: {key}")
        seen.add(key)

        expected = f"{ball['over']}.{ball['ball_in_over']}"
        if ball["over_ball"] != expected:
            raise ValueError(f"Invalid over_ball format: expected {expected}")

        if ball["runs"] < 0 or ball["extras"] < 0:
            raise ValueError("Runs/extras cannot be negative")

        if ball["ball_in_over"] > 6:
            raise ValueError("Invalid ball_in_over (>6)")

    # Ensure chronological order
    sorted_events = sorted(ball_events, key=lambda x: (x["over"], x["ball_in_over"]))
    if ball_events != sorted_events:
        raise ValueError("Ball events must be in chronological order")


def build_label(ball: Dict) -> str:
    if ball["wicket"] == 1:
        return "WICKET"

    if ball["extra_type"] == "wide":
        return f"{ball['extras']} wide"
    elif ball["extra_type"] == "no_ball":
        return f"No ball + {ball['runs']}"
    elif ball["extras"] > 0:
        return f"{ball['runs']} + {ball['extras']} extras"
    else:
        return f"{ball['runs']} runs"


def get_recent_balls(ball_events: List[Dict], limit: int) -> List[Dict]:
    # Already validated chronological order → safe slicing
    sliced = ball_events[-limit:]

    result = []
    for ball in sliced:
        result.append({
            "over_ball": ball["over_ball"],
            "striker": ball["striker"],
            "bowler": ball["bowler"],
            "runs": ball["runs"],
            "extras": ball["extras"],
            "wicket": ball["wicket"],
            "label": build_label(ball)
        })

    return result
