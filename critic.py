import json
from lcm_client import call_lcm
from concepts import EmailConcept

def critique_email(email_text: str, concept: EmailConcept) -> dict:
    prompt = f"""
Evaluate this email against the concept.

Concept:
- Intent: {concept.intent}
- Emotional angle: {concept.emotional_angle}
- Structure: {concept.structure}

Email:
{email_text}

Return ONLY valid JSON with:
alignment_score (0-10), issues (array), improvements (array)
"""
    raw = call_lcm(prompt)

    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1].strip()
        if raw.startswith("json"):
            raw = raw[4:].strip()

    return json.loads(raw)
