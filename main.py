"""One-line office joke entry for the make.fun bounty
'Make the AI Judge Laugh: Office Jokes'.

The joke:

    Our team building exercise was trust falls. HR caught nobody,
    but Legal caught everything on camera.

Why it lands: a trust fall is supposed to prove your colleagues will
catch you, so HR catching nobody is the first failure of the exercise.
The turn is Legal — the one department nobody wants involved — catching
everything, but only on camera. The team gets neither the trust nor the
safety the exercise promises; instead they get evidence. HR drops the
ball and Legal keeps the footage, which is exactly how a corporate
team-building day feels: nobody has your back, but somebody has it
on record.

Writes a single one-line joke about office life to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

JOKE = "Our team building exercise was trust falls. HR caught nobody, but Legal caught everything on camera."


def main() -> None:
    # The bounty gate: the entry must be a single line of 1-199 chars,
    # so the joke is asserted inside that range before it is written.
    assert 1 <= len(JOKE) <= 199
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
