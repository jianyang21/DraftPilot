import json
from lcm_client import call_lcm
from concepts import EmailConcept  # your dataclass file name should be concepts.py

def plan_concept(data) -> EmailConcept:
    prompt = f"""
Return ONLY valid JSON with these keys:
intent, audience, tone, emotional_angle, structure

Rules:
- intent: short phrase
- audience: who this email is for
- tone: one word
- emotional_angle: short phrase
- structure: a single string using this format:
  "opener | context | value | cta"

Context:
Goal: {data["goal"]}
Audience: {data["audience"]}
Tone: {data["tone"]}
"""

    raw = call_lcm(prompt)

    # Clean common markdown wrappers
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1].strip()
        if raw.startswith("json"):
            raw = raw[4:].strip()

    obj = json.loads(raw)

    return EmailConcept(
        intent=obj["intent"],
        audience=obj["audience"],
        tone=obj["tone"],
        emotional_angle=obj["emotional_angle"],
        structure=obj["structure"]
    )
