MAX_NUM_CHARS = 256 # I made this up

def unique_str(s):
    if len(s) > MAX_NUM_CHARS:
        return false

    return len(set(s)) == len(s)

def no_additional_structure(s):
    prev = None
    for c in sorted(s): # We are allocating a new string here, but well, is the same type of datastructure
        if c == prev:
            return False
        prev = c

    return True

assert(unique_str('asdfg'))
assert(not unique_str('aasdfg'))
assert(not unique_str('asdffg'))

assert(no_additional_structure('asdfg'))
assert(not no_additional_structure('asdffg'))
