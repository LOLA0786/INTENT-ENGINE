from engine.scoring import compute_intent_score
from datetime import datetime, timezone

def test_high_intent_scores_high():
    intent = {
        "momentum": "surging",
        "confidence": 0.95,
        "authenticity": {"human_source_pct": 90},
        "streak_days": 10,
        "created_at": datetime.now(timezone.utc)
    }

    score = compute_intent_score(intent)
    assert score > 1.0
