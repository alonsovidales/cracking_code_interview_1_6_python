# Write a method to decide if two strings are anagrams or not.

# The one below can have collisions use a defaultdict in order to count chars
def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    sx1 = 0
    sx2 = 0
    for i in xrange(len(s1)):
        sx1 ^= ord(s1[i])
        sx2 ^= ord(s2[i])

    if sx1 ^ sx2 != 0:
        return False

assert(anagrams('asd', 'sda'))
assert(not anagrams('ad', 'sda'))
assert(anagrams('d', 'd'))
assert(anagrams('', ''))
assert(not anagrams('asdasd', 'asdsdak'))
