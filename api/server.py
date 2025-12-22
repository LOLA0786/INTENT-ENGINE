from fastapi import FastAPI, Query
from datetime import datetime, timezone
import uuid

from engine.scoring import compute_intent_score
from engine.explain import explain_intent

api = FastAPI()
INTENTS = {}

@api.get("/health")
def health():
    return {"status": "ok"}

@api.post("/inject-intent")
def inject_intent(payload: dict):
    intent_id = str(uuid.uuid4())
    payload["id"] = intent_id
    payload["created_at"] = datetime.now(timezone.utc)
    INTENTS[intent_id] = payload
    return {"id": intent_id}

@api.get("/ranked/intents")
def ranked_intents():
    ranked = []
    for intent in INTENTS.values():
        score = compute_intent_score(intent)
        ranked.append({**intent, "intent_score": score})

    ranked.sort(key=lambda x: x["intent_score"], reverse=True)
    return ranked

@api.get("/why-this")
def why_this(intent_id: str = Query(...)):
    intent = INTENTS.get(intent_id)
    if not intent:
        return {"error": "intent not found"}

    score = compute_intent_score(intent)
    explanation = explain_intent(intent, score)

    return {
        "intent_id": intent_id,
        "intent_score": score,
        "explanation": explanation
    }
