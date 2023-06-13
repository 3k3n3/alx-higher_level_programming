#!/usr/bin/python3
"""My int class."""


class MyInt(int):
    """Rebel, does the opposite."""

    """Overides __eq__ & __ne__ method inherited from int."""

    def __eq__(self, x):
        """Inverts Equal."""
        return super().__ne__(x)

    def __ne__(self, x):
        """Inverts not equal."""
        return super().__eq__(x)
