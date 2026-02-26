import unittest

from speech_generator.generator import SpeechGenerator
from speech_generator.models import Audience, Length, Tone


class TestSpeechGenerator(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = SpeechGenerator(wrap_width=80)
        self.audience = Audience(description="engineering team", time_of_day="morning")

    def test_generate_includes_topic_and_audience(self) -> None:
        speech = self.generator.generate(
            topic="time management",
            audience=self.audience,
            tone=Tone.FORMAL,
            length=Length.SHORT,
        )
        self.assertIn("time management", speech)
        self.assertIn("engineering team", speech)

    def test_empty_topic_raises(self) -> None:
        with self.assertRaises(ValueError):
            self.generator.generate(topic=" ", audience=self.audience)

    def test_long_is_longer_than_short(self) -> None:
        short_speech = self.generator.generate(
            topic="teamwork", audience=self.audience, length=Length.SHORT
        )
        long_speech = self.generator.generate(
            topic="teamwork", audience=self.audience, length=Length.LONG
        )
        self.assertGreater(len(long_speech), len(short_speech))


if __name__ == "__main__":
    unittest.main()
