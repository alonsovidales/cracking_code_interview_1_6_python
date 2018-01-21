# Given a matrix in which each row and each column is sorted, write a method to
# find an element in it
# 17:59

def search_marix(mx, n):
    lo = 0
    hi = len(mx)-1

    while abs(hi-lo) > 1:
        m = (hi-lo)/2+lo
        if mx[m][0] < n:
            lo = m
        else:
            hi = m

    if mx[hi][0] > n:
        row = lo
    else:
        row = hi

    print row
    lo = 0
    hi = len(mx[row])-1
    while hi-lo > 1:
        m = (hi-lo)/2+lo
        if mx[row][m] == n:
            return row, m
        if mx[row][m] > n:
            hi = m
        else:
            lo = m

    if mx[row][hi] == n:
        return row, hi
    if mx[row][lo] == n:
        return row, lo
    print "Nonde:", mx[row]
    return None

print search_marix((
    (1, 2, 3, 5),
    (5, 7, 11, 13),
    (6, 8, 14, 18),
    (9, 10, 17, 22),
), 8)
print search_marix((
    (1, 2, 3, 5),
    (5, 7, 11, 13),
    (6, 8, 14, 18),
    (9, 10, 17, 22),
), 100)
print search_marix((
    (1, 2, 3, 5),
    (5, 7, 11, 13),
    (6, 8, 14, 18),
    (9, 10, 17, 22),
), 14)
