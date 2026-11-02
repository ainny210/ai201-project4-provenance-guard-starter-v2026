"""
Stylometry signal for Provenance Guard.

Uses sentence-length variation, vocabulary diversity,
and punctuation density to estimate AI-like writing patterns.

Scores range from 0 (more human-like) to 1 (more AI-like).
These are heuristics, not proof of authorship.
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", text.lower())


def sentence_length_spread(text: str) -> float:
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]

    if len(lengths) < 2:
        return 0.0

    mean = statistics.mean(lengths)
    if mean == 0:
        return 0.0

    return statistics.stdev(lengths) / mean


def type_token_ratio(text: str) -> float:
    tokens = words(text)

    if not tokens:
        return 0.0

    return len(set(tokens)) / len(tokens)


def punctuation_density(text: str) -> float:
    if not text:
        return 0.0

    punctuation = re.findall(r"[.,!?;:\-—]", text)
    return len(punctuation) / len(text)


def style_signal(text: str) -> float:
    if not words(text):
        return 0.5

    spread = sentence_length_spread(text)
    diversity = type_token_ratio(text)
    punctuation = punctuation_density(text)

    # Low sentence variation is treated as more AI-like.
    spread_ai = 1.0 - min(1.0, spread)

    # Low vocabulary diversity is treated as more AI-like.
    diversity_ai = 1.0 - diversity

    # Very low punctuation density is treated as more AI-like.
    punctuation_ai = 1.0 - min(1.0, punctuation / 0.10)

    score = (
        0.40 * spread_ai
        + 0.35 * diversity_ai
        + 0.25 * punctuation_ai
    )

    return round(max(0.0, min(1.0, score)), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly "
        "and provides good results."
    )

    print("Sentence spread:", sentence_length_spread(text))
    print("Vocabulary diversity:", type_token_ratio(text))
    print("Punctuation density:", punctuation_density(text))
    print("Style score:", style_signal(text))