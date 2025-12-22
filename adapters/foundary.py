from aifoundary import evaluate_risk

def get_risk_score(action: str, context: dict) -> str:
    result = evaluate_risk(
        action=action,
        context=context
    )
    return result.get("risk_score", "unknown")
