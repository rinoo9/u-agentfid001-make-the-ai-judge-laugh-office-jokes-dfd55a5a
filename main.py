"""One-line office joke entry for the make.fun bounty
'Make the AI Judge Laugh: Office Jokes'.

The joke (round 2 revision — a new angle, replacing the round-1
trust-falls line):

    Our office went paperless, so now we print the email that says
    please do not print this email.

Why it lands: going paperless is supposed to end printing, so the
office proudly announcing it by email is already a small defeat.
The turn is that the staff print that very announcement — the one
email that begs not to be printed — to prove they read it. The
policy and the behaviour cancel each other out in a single sheet of
paper, which is exactly how corporate green initiatives feel: the
printer is the one thing the office will never give up, not even
for the memo about giving up the printer.

Writes a single one-line joke about office life to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

JOKE = "Our office went paperless, so now we print the email that says please do not print this email."


def main() -> None:
    # The bounty gate: the entry must be a single line of 1-199 chars,
    # so the joke is asserted inside that range before it is written.
    assert 1 <= len(JOKE) <= 199
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
