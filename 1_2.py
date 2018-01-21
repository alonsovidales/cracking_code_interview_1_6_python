def reverse_str(s):
    list_str = map(ord, s) # We can't modify the string char by char
    for i in xrange((len(list_str)-1)/2):
        list_str[i] ^= list_str[len(s)-i-2]
        list_str[len(s)-i-2] ^= list_str[i]
        list_str[i] ^= list_str[len(s)-i-2]

    return ''.join(map(chr, list_str))

assert(reverse_str("\n") == "\n")
assert(reverse_str("sadc\n") == "cdas\n")
assert(reverse_str("sapdc\n") == "cdpas\n")
