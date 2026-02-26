from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Tone(str, Enum):
    """Supported speech tone options."""

    FORMAL = "formal"
    INFORMAL = "informal"
    INSPIRATIONAL = "inspirational"


class Length(str, Enum):
    """Supported speech length options."""

    SHORT = "short"
    MEDIUM = "medium"
    LONG = "long"


@dataclass(frozen=True)
class Audience:
    """Audience profile used to tailor generated content."""

    description: str
    time_of_day: str = "day"
    context: str = ""

    def __post_init__(self) -> None:
        if not self.description.strip():
            raise ValueError("Audience description cannot be empty.")
