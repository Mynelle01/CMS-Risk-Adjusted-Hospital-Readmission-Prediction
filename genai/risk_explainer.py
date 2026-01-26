def generate_risk_explanation(risk_score, top_features):
    """
    GenAI-assisted explanation prototype.
    This function simulates how an LLM would generate explanations based on model outputs.
    """

    explanation = (
        f"The patient has an estimated {risk_score:.0%} risk of 30-day readmission."
        f"This risk is primarily driven by {', '.join(top_features)}."
        "These factors suggest higher clinical complexity and prior utilization."
    )

    return explanation