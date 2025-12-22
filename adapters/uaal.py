import requests

INTENT_ENGINE_URL = "http://127.0.0.1:8000"
INTENT_THRESHOLD = 1.2

def intent_alignment_required(topic: str) -> bool:
    resp = requests.get(f"{INTENT_ENGINE_URL}/ranked/intents", timeout=2)
    resp.raise_for_status()

    intents = resp.json()
    for intent in intents:
        if intent.get("topic") == topic:
            return intent.get("intent_score", 0) >= INTENT_THRESHOLD

    return False
