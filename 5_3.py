# Given an integer, print the next smallest and next largest number that have
# the same number of 1 bits in their binary representation

def get_next_small_largets(n):
    # 101 -> 110 - 11
    # 111 -> 1110 - 111
    # 1110 -> 11100 - 1101
    min_str = list(bin(n)[2:])
    max_str = min_str[::-1]
    searching = True
    found = False
    for i, v in enumerate(max_str):
        if searching and v == '1':
            searching = False
            max_str[i] = '0'
        elif not searching and v == '0':
            max_str[i] = '1'
            found = True
            break

    if not searching and not found:
        max_str.append('1')

    searching = True
    for i, v in enumerate(min_str):
        if searching and v == '0':
            min_str[i-1] = '0'
            min_str[i] = '1'
            break

    return int(''.join(min_str), 2), int(''.join(max_str[::-1]), 2)

min_n, max_n = get_next_small_largets(int('101', 2))
print '101',  int('101', 2), min_n, max_n, bin(min_n), bin(max_n)

min_n, max_n = get_next_small_largets(int('111', 2))
print '111', int('111', 2), min_n, max_n, bin(min_n), bin(max_n)

min_n, max_n = get_next_small_largets(int('1110', 2))
print '1110', int('1110', 2), min_n, max_n, bin(min_n), bin(max_n)
