"""
Imagine a robot sitting on the upper left hand corner of an NxN grid The robot
can only move in two directions: right and down How many possible paths are
there for the robot?
FOLLOW UP
Imagine certain squares are "o  limits", such that the robot can not step on
them Design an algorithm to get all possible paths for the robot
"""
class Board(object):
    def __init__(self, n):
        self._n = n

    def moves(self, x=0, y=0, total=None):
        if x > self._n or y > self._n: # Check here if this is off limits
            return

        if total is None:
            total = [0]
        total[0] += 1
        self.moves(x+1, y, total)
        self.moves(x, y+1, total)

        return total[0]

br = Board(2)
print br.moves()
br = Board(4)
print br.moves()
br = Board(8)
print br.moves()
