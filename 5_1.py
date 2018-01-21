"""
You are given two 32-bit numbers, N and M, and two bit positions, i and j Write
a method to set all bits between i and j in N equal to M (e g , M becomes a
substring of N located at i and starting at j)
EXAMPLE:
Input: N = 10000000000, M = 10101, i = 2, j = 6
Output: N = 10001010100
"""

def mix_nums(n, m, i, j):
    n >>= j
    n <<= j

    m <<= i
    return n | m

assert(bin(mix_nums(int('10000000000', 2), int('10101', 2), 2, 6)) == '0b10001010100')
assert(bin(mix_nums(int('10000010000', 2), int('10101', 2), 2, 6)) == '0b10001010100')
