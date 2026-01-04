from planner import plan_concept
from renderer import render_email
from critic import critique_email
from rewriter import rewrite_email

def run():
    data = {
        "goal": "internship outreach",
        "audience": "technical recruiter",
        "tone": "professional",
        "key_points": [
            "AI engineering intern experience",
            "Python + ML projects",
            "Fast learner and hands-on builder"
        ],
        "max_words": 120
    }

    concept = plan_concept(data)
    print("\nCONCEPT:\n", concept)

    email = render_email(concept, data)
    print("\nDRAFT EMAIL:\n", email)

    review = critique_email(email, concept)
    print("\nCRITIQUE:\n", review)

    if review.get("alignment_score", 0) < 8:
        email = rewrite_email(email, concept, review, data)
        print("\nREWRITTEN EMAIL:\n", email)

if __name__ == "__main__":
    run()
