# Imagine you have a square matrix, where each cell is filled with either black
# or white Design an algorithm to find the maximum subsquare such that all four
# borders are filled with black pixels

# b b b w w b w b
# b w b w w b b b
# b b b b w b w b
# b b b w w w w b
# b w b w w b w b

class SquareProcessor(object):
    def __init__(self, square):
        self._s = square

    def find_max_subsquare(self, x=0, y=0, w=0, l=0, max_sqr=None):
        if y+l >= len(self._s) or x+w >= len(self._s[0]):
            return

        if max_sqr is None:
            max_sqr = [0, 0, 0, 0]

        if w + l > max_sqr[2] + max_sqr[3]:
            valid = True
            for xi in xrange(x, x+w):
                if self._s[y][xi] != 'b' or self._s[y+l][xi] != 'b':
                    valid = False
                    break

            for yi in xrange(y, y+l):
                if self._s[yi][x] != 'b' or self._s[yi][x+w] != 'b':
                    valid = False
                    break

            if valid:
                max_sqr[0] = x
                max_sqr[1] = y
                max_sqr[2] = w
                max_sqr[3] = l

        self.find_max_subsquare(x, y, w+1, l, max_sqr)
        self.find_max_subsquare(x, y, w, l+1, max_sqr)
        self.find_max_subsquare(x+1, y, w, l, max_sqr)
        self.find_max_subsquare(x, y+1, w, l, max_sqr)

        return max_sqr

sp = SquareProcessor((
    ('b', 'b', 'b', 'w', 'w', 'b', 'w', 'b'),
    ('b', 'w', 'b', 'w', 'w', 'b', 'b', 'b'),
    ('b', 'b', 'b', 'b', 'w', 'b', 'w', 'b'),
    ('b', 'b', 'b', 'w', 'w', 'w', 'w', 'b'),
    ('b', 'w', 'b', 'w', 'w', 'b', 'w', 'b'),
))

print sp.find_max_subsquare() 
