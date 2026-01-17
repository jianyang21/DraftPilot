from __future__ import annotations

from typing import Any, Dict, Optional

from planner import plan_concept
from renderer import render_email
from critic import critique_email
from rewriter import rewrite_email


def run_pipeline(intent: str, context: Optional[str] = None) -> Dict[str, Any]:
    """
    Production-safe pipeline entry.
    Returns a dict with concept, draft, critique, and final email.

    intent: what the outreach is for (example: "internship outreach")
    context: optional extra context to help the agent (example: resume summary, job link)
    """

    # Base config. You can tune defaults here.
    data: Dict[str, Any] = {
        "goal": intent,
        "audience": "technical recruiter",
        "tone": "professional",
        "key_points": [
            "AI engineering intern experience",
            "Python + ML projects",
            "Fast learner and hands-on builder",
        ],
        "max_words": 120,
    }

    # If you want context to influence generation, pass it through the data object.
    if context:
        data["context"] = context

    concept = plan_concept(data)
    email_draft = render_email(concept, data)
    review = critique_email(email_draft, concept)

    final_email = email_draft
    alignment_score = 0

    try:
        alignment_score = int(review.get("alignment_score", 0))
    except Exception:
        alignment_score = 0

    if alignment_score < 8:
        final_email = rewrite_email(email_draft, concept, review, data)

    return {
        "concept": concept,
        "draft": email_draft,
        "critique": review,
        "final": final_email,
    }


def run() -> None:
    """
    Local CLI-style run for quick testing.
    """
    result = run_pipeline(
        intent="internship outreach",
        context=None,  # put resume summary or job link here if you want
    )

    print("\nCONCEPT:\n", result["concept"])
    print("\nDRAFT EMAIL:\n", result["draft"])
    print("\nCRITIQUE:\n", result["critique"])
    print("\nFINAL EMAIL:\n", result["final"])


if __name__ == "__main__":
    run()
