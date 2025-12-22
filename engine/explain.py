def explain_intent(intent: dict, score: float):
    return [
        {"signal": "momentum", "value": intent.get("momentum")},
        {"signal": "confidence", "value": intent.get("confidence")},
        {
            "signal": "human_authenticity",
            "value": intent.get("authenticity", {}).get("human_source_pct")
        },
        {"signal": "streak_days", "value": intent.get("streak_days", 0)},
        {"signal": "final_score", "value": score}
    ]
