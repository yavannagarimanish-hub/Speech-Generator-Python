import textwrap

def generate_speech(topic, audience, tone, length):
    """Generate a neutral, non-political speech skeleton."""
    tone_phrases = {
        "formal": {
            "greeting": f"Good {audience.get('time_of_day', 'day')},",
            "closing": "Thank you for your time and attention.",
            "connector": "Moreover",
            "hope": "I sincerely hope"
        },
        "informal": {
            "greeting": "Hey everyone,",
            "closing": "Thanks a lot for listening.",
            "connector": "On top of that",
            "hope": "I really hope"
        },
        "inspirational": {
            "greeting": "Friends and colleagues,",
            "closing": "Let us move forward with confidence.",
            "connector": "Most importantly",
            "hope": "I truly believe"
        }
    }

    style = tone_phrases.get(tone, tone_phrases["formal"])

    audience_desc = audience.get("description", "all of you")
    context = audience.get("context", "")

    intro = (
        f"{style['greeting']} {audience_desc}.\n\n"
        f"Today, I want to talk with you about {topic}."
        + (f" In particular, we’ll focus on {context}." if context else "")
    )

    body_points = [
        f"First, we need to understand why {topic} matters to us today.",
        f"Second, we should look at some practical steps we can take to engage with {topic} more effectively.",
        f"Finally, we must consider how our choices around {topic} will shape our work, our learning, and our everyday lives."
    ]

    elaboration = [
        f"When we look closely at {topic}, we see that it affects our habits, our goals, and the way we collaborate.",
        f"{style['connector']}, small, consistent actions often lead to meaningful improvements over time.",
        f"{style['hope']} that each of us can leave here with at least one concrete idea we’re ready to put into practice."
    ]

    conclusion = (
        f"In closing, remember that {topic} is not just an abstract idea—it is something we live out in the way we plan, "
        f"the way we communicate, and the way we support one another.\n\n"
        f"{style['closing']}"
    )

    # Adjust length by number of body paragraphs
    if length == "short":
        body = "\n\n".join(body_points[:1] + elaboration[:1])
    elif length == "medium":
        body = "\n\n".join(body_points[:2] + elaboration[:2])
    else:  # long
        body = "\n\n".join(body_points + elaboration)

    speech = f"{intro}\n\n{body}\n\n{conclusion}"
    return textwrap.fill(speech, width=80)

def ask_input():
    topic = input("Enter a (non-political) topic (e.g., 'time management', 'teamwork'): ").strip()
    audience_desc = input("Describe your audience (e.g., 'students', 'colleagues'): ").strip() or "everyone"
    time_of_day = input("Time of day (morning/afternoon/evening, optional): ").strip() or "day"
    context = input("Optional context (e.g., 'our next project', 'this semester'): ").strip()

    print("\nTone options: formal / informal / inspirational")
    tone = input("Choose tone: ").strip().lower() or "formal"
    if tone not in {"formal", "informal", "inspirational"}:
        tone = "formal"

    print("\nLength options: short / medium / long")
    length = input("Choose length: ").strip().lower() or "medium"
    if length not in {"short", "medium", "long"}:
        length = "medium"

    audience = {
        "description": audience_desc,
        "time_of_day": time_of_day,
        "context": context
    }

    return topic, audience, tone, length

def main():
    print("=== Neutral Speech Generator (Python) ===")
    print("Note: For non-political topics only.\n")

    topic, audience, tone, length = ask_input()
    speech = generate_speech(topic, audience, tone, length)

    print("\n--- Generated Speech ---\n")
    print(speech)
    print("\n------------------------\n")

if __name__ == "__main__":
    main()
