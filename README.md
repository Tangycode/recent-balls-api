# recent-balls-api
The Recent Balls API returns the most recent ball events from a cricket match in a structured format for live dashboard and frontend use. It is integration-ready, fully payload-driven, and designed to work within the Khel AI MVP system without relying on any hardcoded or demo data.

Features
Returns latest N balls (configurable limit)
Accepts live ball-by-ball payload
Chronological sorting of deliveries
Frontend-ready JSON output
Stateless and scalable design
Logic separated from route layer
Endpoint

POST /recent-balls

Request
{
  "match_id": "match_001",
  "innings": 1,
  "limit": 6,
  "balls": [
    {
      "ball": 12.1,
      "runs_off_bat": 1,
      "extras": 0,
      "extra_type": null,
      "wicket": false
    }
  ]
}
Response
{
  "status": "success",
  "data": {
    "match_id": "match_001",
    "innings": 1,
    "limit": 6,
    "recent_balls": [
      {
        "ball": 12.1,
        "runs": 1,
        "extras": 0,
        "extra_type": null,
        "wicket": false,
        "total": 1
      }
    ]
  }
}

Key Improvement
Moved from static/demo data → fully payload-driven, stateless API with clean service-layer architecture for integration into Khel AI MVP.
