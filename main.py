"""One-line office joke entry for the make.fun bounty
'Make the AI Judge Laugh: Office Jokes'.

Writes a single one-line joke about office life to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

JOKE = "Our team building exercise was trust falls. HR caught nobody, but Legal caught everything on camera."


def main() -> None:
    assert 1 <= len(JOKE) <= 199
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
