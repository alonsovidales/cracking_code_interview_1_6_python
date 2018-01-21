# Design an algorithm to figure out if someone has won in a game of tic-tac-toe

def who_won(board):
    total_d_x = 0
    total_d_o = 0
    for i in xrange(len(board)):
        if board[i][i] == 'o':
            total_d_o += 1
        if board[i][i] == 'x':
            total_d_x += 1
        total_h_x = 0
        total_h_o = 0
        total_v_x = 0
        total_v_o = 0
        for j in xrange(len(board)):
            if board[i][j] == 'o':
                total_h_o += 1
            elif board[i][j] == 'x':
                total_h_x += 1

            if board[j][i] == 'o':
                total_v_o += 1
            elif board[j][i] == 'x':
                total_v_x += 1

        if total_h_x == 3 or total_v_x == 3 or total_d_x == 3:
            return 'x'

        if total_h_o == 3 or total_v_o == 3 or total_d_o == 3:
            return 'o'

    return None

assert(who_won((
    ('x', 'o', 'x'),
    ('o', 'x', 'o'),
    (' ', ' ', 'x'),
)) == 'x')

assert(who_won((
    ('x', 'x', 'x'),
    ('o', ' ', 'o'),
    (' ', ' ', 'x'),
)) == 'x')

assert(who_won((
    ('o', 'x', 'x'),
    ('o', ' ', 'o'),
    ('o', ' ', 'x'),
)) == 'o')
