from __future__ import annotations

import textwrap
from typing import Dict

from .models import Audience, Length, Tone


_TONE_PHRASES: Dict[Tone, Dict[str, str]] = {
    Tone.FORMAL: {
        "greeting": "Good {time_of_day},",
        "closing": "Thank you for your time and attention.",
        "connector": "Moreover",
        "hope": "I sincerely hope",
    },
    Tone.INFORMAL: {
        "greeting": "Hey everyone,",
        "closing": "Thanks a lot for listening.",
        "connector": "On top of that",
        "hope": "I really hope",
    },
    Tone.INSPIRATIONAL: {
        "greeting": "Friends and colleagues,",
        "closing": "Let us move forward with confidence.",
        "connector": "Most importantly",
        "hope": "I truly believe",
    },
}


class SpeechGenerator:
    """Deterministically generates a neutral speech skeleton."""

    def __init__(self, wrap_width: int = 80) -> None:
        if wrap_width < 40:
            raise ValueError("Wrap width must be at least 40 characters.")
        self._wrap_width = wrap_width

    def generate(
        self,
        topic: str,
        audience: Audience,
        tone: Tone = Tone.FORMAL,
        length: Length = Length.MEDIUM,
    ) -> str:
        clean_topic = topic.strip()
        if not clean_topic:
            raise ValueError("Topic cannot be empty.")

        style = _TONE_PHRASES[tone]
        greeting = style["greeting"].format(time_of_day=audience.time_of_day)

        intro = (
            f"{greeting} {audience.description}.\n\n"
            f"Today, I want to talk with you about {clean_topic}."
            + (f" In particular, we’ll focus on {audience.context}." if audience.context else "")
        )

        body_points = [
            f"First, we need to understand why {clean_topic} matters to us today.",
            f"Second, we should look at practical steps we can take to engage with {clean_topic} more effectively.",
            f"Finally, we must consider how our choices around {clean_topic} will shape our work, learning, and daily lives.",
        ]

        elaboration = [
            f"When we look closely at {clean_topic}, we see that it affects our habits, goals, and collaboration.",
            f"{style['connector']}, small, consistent actions often lead to meaningful improvements over time.",
            f"{style['hope']} that each of us can leave here with at least one concrete idea we’re ready to put into practice.",
        ]

        conclusion = (
            f"In closing, remember that {clean_topic} is not just an abstract idea—it is something we live out in how we plan, "
            f"communicate, and support one another.\n\n"
            f"{style['closing']}"
        )

        body = self._build_body(length=length, body_points=body_points, elaboration=elaboration)
        speech = f"{intro}\n\n{body}\n\n{conclusion}"
        return textwrap.fill(speech, width=self._wrap_width)

    @staticmethod
    def _build_body(length: Length, body_points: list[str], elaboration: list[str]) -> str:
        if length == Length.SHORT:
            paragraphs = body_points[:1] + elaboration[:1]
        elif length == Length.MEDIUM:
            paragraphs = body_points[:2] + elaboration[:2]
        else:
            paragraphs = body_points + elaboration

        return "\n\n".join(paragraphs)
