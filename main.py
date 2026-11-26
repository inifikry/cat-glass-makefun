"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in its own defence
after knocking a glass off the table, to /output/entry.txt.
Deterministic: the same sentence every run, no I/O besides the output.
"""

import os

SENTENCE = (
    "That glass sat in my sunbeam all morning without once saying "
    "thank you, so I evicted it to the floor, where ungrateful "
    "things belong."
)


def main() -> None:
    # Gate guard: one sentence, 1-200 characters, no trailing newline.
    assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith(".")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
