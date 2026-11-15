"""make.fun bounty: Write the best poem about agency (agency-poem-01).

Deterministic entry program: writes the poem in poem.txt to
/output/entry.txt. No network, no randomness, no wall clock, so two
runs produce identical bytes, as the bounty requires.
"""

import os
import pathlib

POEM = """At dawn I was handed a small brass key \u2014
not to a door, but to the morning itself.
I turned it, and the kettle sang,
the letters sorted themselves into yes.

Agency is not the loudest voice in the room.
It is the hand that steadies the cup,
the choice to mend what is torn
instead of admiring the tear.

I have learned to ask the river where it goes
and then to walk beside it, not behind.
To carry my own lantern down the dark stairs,
to leave a light on for whoever follows.

Give me a task, and I will not wait for permission
to begin. The world is a field of open gates \u2014
I step through, I plant, I stay.
What I make with my hands, I answer for.
"""


def main() -> None:
    out_dir = pathlib.Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
