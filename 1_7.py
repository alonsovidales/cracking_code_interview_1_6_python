# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column is set to 0.

# O(n*m)
def set_zeroes(m):
    cols_rows_to_zero = (set(), set())

    for y, row in enumerate(m):
        for x, v in enumerate(row):
            if v == 0:
                cols_rows_to_zero[0].add(y)
                cols_rows_to_zero[1].add(x)

    for y in xrange(len(m)):
        for x in xrange(len(row)):
            if y in cols_rows_to_zero[0] or x in cols_rows_to_zero[1]:
                m[y][x] = 0

    return m

result = set_zeroes([
        [1, 2, 3, 4, 5, 1],
        [1, 2, 3, 0, 5, 3],
        [1, 2, 3, 4, 5, 3],
        [1, 0, 3, 4, 5, 0],
        [1, 2, 3, 4, 5, 0],
])

for l in result:
    print l
