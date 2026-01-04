from lcm_client import call_lcm
from concepts import EmailConcept

def rewrite_email(email_text: str, concept: EmailConcept, critique: dict, data) -> str:
    prompt = f"""
Rewrite the email to better match the concept.

Concept:
Intent: {concept.intent}
Tone: {concept.tone}
Emotional angle: {concept.emotional_angle}
Structure: {concept.structure}

Critique issues:
{critique.get("issues", [])}

Improvements to apply:
{critique.get("improvements", [])}

Constraints:
- Max {data["max_words"]} words
- Must include CTA
- Output ONLY the final email body text

Original email:
{email_text}
"""
    return call_lcm(prompt)
