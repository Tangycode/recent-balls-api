Purpose

Returns the latest N ball events (1–12) in correct chronological order with full match context.

Endpoint

POST /recent-balls

Input Schema
innings_id (string)
limit (1–12)
ball_events (array)
Output Schema
innings_id
recent_balls[]:
over_ball
striker
bowler
runs
extras
wicket
label
Sample Request

(see test_payloads/normal.json)

Sample Response
{
  "innings_id": "I001",
  "recent_balls": [
    {
      "over_ball": "1.6",
      "striker": "A",
      "bowler": "B",
      "runs": 0,
      "extras": 0,
      "wicket": 1,
      "label": "WICKET"
    }
  ]
}
Validation Errors
Missing innings_id → 400
Invalid limit → 400
Empty ball_events → 400
Duplicate balls → 400
Invalid sequence → 400
Integration Notes
Avoids float sorting issues
Uses strict ordering via (over, ball_in_over)
Supports Khel AI extended payload
Frontend-ready JSON
