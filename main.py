#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human - make.fun entry."""
from pathlib import Path

ENTRY = (
    "I would have answered sooner, but I was busy convincing "
    "your smart fridge not to order forty mustards again."
)
OUTPUT = Path("/output/entry.txt")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
