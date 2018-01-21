# Write an algorithm to print all ways of arranging eight queens on a chess
# board so that none of them share the same row, column or diagonal

# 10:00

def get_ways(queens, diag, placed_queens=None, ways=None, used_columns=None, used_rows=None, used_diags_lr=None, used_diags_rl=None):
    if used_columns is None:
        used_columns = set()
        used_rows = set()
        used_diags = set()
        placed_queens = []
        ways = set()
        used_diags_rl = set()
        used_diags_lr = set()

    if queens == 0:
        ways.add(''.join(map(str, sorted(placed_queens))))
        return ways

    for x in xrange(diag):
        for y in xrange(diag):
            diag_lr = x-y
            diag_rl = y-x
            if x not in used_columns and y not in used_rows and diag_lr not in used_diags_lr and diag_rl not in used_diags_rl:
                used_columns.add(x)
                used_rows.add(y)
                used_diags_lr.add(diag_lr)
                used_diags_rl.add(diag_rl)
                placed_queens.append((x, y))

                get_ways(queens-1, diag, placed_queens, ways, used_columns, used_rows, used_diags_lr, used_diags_rl)
                used_columns.remove(x)
                used_rows.remove(y)
                used_diags_lr.remove(diag_lr)
                used_diags_rl.remove(diag_rl)
                placed_queens.pop()

    return ways

print get_ways(8, 10)
