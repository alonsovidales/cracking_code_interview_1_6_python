def remove_duplicate_bo_buffer(s):
    i = 0
    while i < len(s):
        j = i+1
        while j < len(s):
            if s[i] == s[j]:
                s = s[:j] + s[j+1:] # Yep, we are allocating a brand new string here, but we can't mutate the string in python
            else:
                j += 1

        i += 1

    return s

assert(remove_duplicate_bo_buffer('asdaasd') == 'asd')
assert(remove_duplicate_bo_buffer('asd') ==  'asd')
assert(remove_duplicate_bo_buffer('') == '')
assert(remove_duplicate_bo_buffer('aaa') == 'a')
assert(remove_duplicate_bo_buffer('a') == 'a')
