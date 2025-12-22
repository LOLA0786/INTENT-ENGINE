from math import exp
from datetime import datetime, timezone

MOMENTUM_MAP = {
    "surging": 1.3,
    "rising": 1.1,
    "steady": 0.9
}

def recency_decay(created_at, half_life_hours=24):
    hours = (datetime.now(timezone.utc) - created_at).total_seconds() / 3600
    return exp(-hours / half_life_hours)

def compute_intent_score(intent: dict) -> float:
    momentum = MOMENTUM_MAP.get(intent.get("momentum"), 1.0)
    confidence = intent.get("confidence", 0.0)

    authenticity = intent.get("authenticity", {}).get("human_source_pct", 0) / 100
    streak_days = intent.get("streak_days", 0)
    streak_boost = 1 + min(streak_days / 14, 0.3)

    created_at = intent.get("created_at")
    if not created_at:
        return 0.0

    decay = recency_decay(created_at)

    score = momentum * confidence * authenticity * streak_boost * decay
    return round(score, 3)
