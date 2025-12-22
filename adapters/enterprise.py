from adapters.base import SignalAdapter
from datetime import datetime, timezone

class EnterpriseAdapter(SignalAdapter):

    def fetch_signals(self):
        # Example: tickets, searches, approvals, escalations
        return [
            {
                "source": "enterprise",
                "topic": "AI governance",
                "momentum": "steady",
                "confidence": 0.9,
                "authenticity": {"human_source_pct": 95},
                "streak_days": 12,
                "created_at": datetime.now(timezone.utc)
            }
        ]
