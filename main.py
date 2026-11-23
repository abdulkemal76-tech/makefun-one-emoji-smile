"""One Emoji, One Smile — make.fun bounty entry.

Writes exactly one emoji to /output/entry.txt: the hugging face.
A smiling face with open arms: warm at first glance, specific and
goofy rather than the default smiley, universal, and friendly from
a stranger — a virtual hug, not flirtation or an in-joke.
"""

EMOJI = "\U0001F917"  # 🤗 Hugging Face


import os


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Self-check: the file must hold exactly one emoji and nothing else.
    with open("/output/entry.txt", encoding="utf-8") as f:
        content = f.read()
    assert content == EMOJI, f"entry.txt must be exactly one emoji, got {content!r}"


if __name__ == "__main__":
    main()
