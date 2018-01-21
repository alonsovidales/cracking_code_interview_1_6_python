# Implement the "paint  ll" function that one might see on many image editing
# pro- grams That is, given a screen (represented by a 2 dimensional array of
# Colors), a point, and a new color,  ll in the surrounding area until you hit
# a border of that col- or'

def paint_fill(m, x, y, new_color, original_color=None, xi=None, yi=None):
    if xi is None: 
        original_color = m[y][x]
        xi = x
        yi = y

    if yi >= len(m) or xi >= len(m[0]) or xi < 0 or yi < 0:
        return

    if m[yi][xi] == original_color:
        m[yi][xi] = new_color
        paint_fill(m, x, y, new_color, original_color, xi+1, yi)
        paint_fill(m, x, y, new_color, original_color, xi-1, yi)
        paint_fill(m, x, y, new_color, original_color, xi, yi+1)
        paint_fill(m, x, y, new_color, original_color, xi, yi-1)

aux = (
    [12, 12, 12, 12, 12, 12, 12],
    [12,  1,  2,  2,  2,  2,  1],
    [12,  2,  2, 12, 12,  1, 12],
    [12,  2, 12, 12, 12,  1, 12],
    [ 1, 12, 12, 12, 12, 12,  2],
    [12,  1, 12, 12, 12, 12, 12],
    [12,  1,  1,  2,  2,  1,  1],
    [12, 12, 12, 12, 12, 12, 12],
    [12, 12, 12, 12, 12, 12, 12],
    [12, 12, 12, 12, 12, 12, 12],
    [12, 12, 12, 12, 12, 12, 12],
)

paint_fill(aux, 4, 2, 5)

for l in aux:
    print l
