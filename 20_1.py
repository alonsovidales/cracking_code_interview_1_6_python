# Write a function that adds two numbers You should not use + or any arithmetic
# operators

def add(a, b):
    ba = bin(a)[2:][::-1]
    bb = bin(b)[2:][::-1]

    carr = 0
    new_num = []
    for i in xrange(max(len(ba), len(bb))):
        if i < len(ba) and i < len(bb):
            total = int(ba[i]) + int(bb[i]) + carr
        elif i < len(ba):
            total = int(ba[i]) + carr
        else:
            total = int(bb[i]) + carr

        new_num.append(total % 2)
        carr = total / 2

    if carr == 1:
        new_num.append(1)

    return int(''.join(map(str, new_num[::-1])), 2)

assert(add(4, 5) == 9)
assert(add(10, 5) == 15)
assert(add(20, 22) == 42)
