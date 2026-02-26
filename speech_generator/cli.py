from __future__ import annotations

import argparse

from .generator import SpeechGenerator
from .models import Audience, Length, Tone


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a neutral, non-political speech skeleton."
    )
    parser.add_argument("--topic", help="Speech topic.")
    parser.add_argument("--audience", default="everyone", help="Audience description.")
    parser.add_argument("--time-of-day", default="day", help="Greeting context (e.g., morning).")
    parser.add_argument("--context", default="", help="Optional audience context.")
    parser.add_argument(
        "--tone",
        choices=[tone.value for tone in Tone],
        default=Tone.FORMAL.value,
        help="Speech tone.",
    )
    parser.add_argument(
        "--length",
        choices=[length.value for length in Length],
        default=Length.MEDIUM.value,
        help="Speech length.",
    )
    return parser.parse_args()


def _prompt_if_missing(value: str | None, prompt: str, fallback: str | None = None) -> str:
    if value:
        return value.strip()
    entered = input(prompt).strip()
    if entered:
        return entered
    if fallback is not None:
        return fallback
    raise ValueError("A required value was not provided.")


def run() -> int:
    args = _parse_args()

    print("=== Neutral Speech Generator (Python) ===")
    print("Note: For non-political topics only.\n")

    topic = _prompt_if_missing(args.topic, "Enter a topic: ")
    audience_description = _prompt_if_missing(
        args.audience, "Describe your audience: ", fallback="everyone"
    )

    audience = Audience(
        description=audience_description,
        time_of_day=args.time_of_day.strip() or "day",
        context=args.context.strip(),
    )

    generator = SpeechGenerator()
    speech = generator.generate(
        topic=topic,
        audience=audience,
        tone=Tone(args.tone),
        length=Length(args.length),
    )

    print("\n--- Generated Speech ---\n")
    print(speech)
    print("\n------------------------")
    return 0
