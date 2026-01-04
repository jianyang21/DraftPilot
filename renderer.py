from lcm_client import call_lcm
from concepts import EmailConcept

def render_email(concept: EmailConcept, data) -> str:
    prompt = f"""
Write an email using this concept.

Intent: {concept.intent}
Audience: {concept.audience}
Tone: {concept.tone}
Emotional angle: {concept.emotional_angle}
Structure: {concept.structure}

Constraints:
- Max {data["max_words"]} words
- Must include a clear CTA
- No markdown fences
- Output ONLY the email body text

Key points to include:
{data.get("key_points", [])}
"""
    return call_lcm(prompt)
