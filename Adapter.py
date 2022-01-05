import math


class RoundPeg:
    """
    RoundPeg(s) are compatible with RoundHole(s)
    """
    def __init__(self, radius: float):
        self._radius = radius

    def getRadius(self) -> float:
        return self._radius


class RoundHole:
    """
    RoundHole(s) are compatible with RoundPeg(s)
    """
    def __init__(self, radius: float):
        self._radius = radius

    def getRadius(self) -> float:
        return self._radius

    def fits(self, peg: RoundPeg) -> bool:
        return self.getRadius() >= peg.getRadius()


class SquarePeg:
    """
    SquarePeg(s) are not compatible with RoundHole(s).
    But we need to integrate them into our program.
    """
    def __init__(self, width: float):
        self._width = width

    def getWidth(self) -> float:
        return self._width


class SquarePegAdapter:
    """
    The Adapter Adapter allows fitting square pegs into round holes.
    """

    def __init__(self, squarePeg: SquarePeg):
        self.squarePeg = squarePeg

    def getRadius(self) -> float:
        return self.squarePeg.getWidth() * math.sqrt(2) / 2


if __name__ == "__main__":
    hole = RoundHole(5)

    # Round fits round, no surprise.
    rpeg = RoundPeg(5)
    if hole.fits(rpeg):
        print("Round peg r5 fits round hole r5!")

    smallSqPeg = SquarePeg(2)
    largeSqPeg = SquarePeg(20)
    # hole.fits(smallSqPeg)  # Won't work!

    # Adapter solves the problem.
    smallSqPegAdapter = SquarePegAdapter(smallSqPeg)
    largeSqPegAdapter = SquarePegAdapter(largeSqPeg)
    if hole.fits(smallSqPegAdapter):
        print("Square peg w2 fits round hole r5!")
    if not hole.fits(largeSqPegAdapter):
        print("Square peg w20 does not fit into round hole r5!")
