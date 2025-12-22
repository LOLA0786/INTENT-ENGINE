from adapters.base import SignalAdapter
from datetime import datetime, timezone

class SocialAdapter(SignalAdapter):

    def fetch_signals(self):
        # Placeholder: later this pulls from SocialGraph
        return [
            {
                "source": "social",
                "topic": "AI governance",
                "momentum": "rising",
                "confidence": 0.8,
                "authenticity": {"human_source_pct": 85},
                "streak_days": 5,
                "created_at": datetime.now(timezone.utc)
            }
        ]
