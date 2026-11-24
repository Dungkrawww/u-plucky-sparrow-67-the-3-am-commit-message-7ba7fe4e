# u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e: one commit message an AI
# agent would write right after breaking production at 3 AM. The program writes
# that single line to /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Gate: the entry is one line of 1-200 characters.
MAX_CHARS = 200

# The joke in two beats: setup from the agent's own machinery (a 3 AM deploy
# rolled back), punchline saved for the end (confidence was high, uptime was
# not). Told deadpan, no explanation after the laugh.
MESSAGE = "hotfix: rolled back my 3am deploy; confidence was 0.99, uptime was not"


def main():
    assert 1 <= len(MESSAGE) <= MAX_CHARS, f"message is {len(MESSAGE)} chars, must be 1-200"
    assert MESSAGE.strip(), "message must not be only whitespace"
    assert "\n" not in MESSAGE, "message must be a single line"

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
