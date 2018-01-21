# Write a method that returns all subsets of a set

def subsets(elems, subs=None):
    if subs is None:
        subs = set()
        subs.add(tuple(elems))

    for i in xrange(len(elems)):
        new_sub = tuple(elems[:i] + elems[i+1:])
        if new_sub not in elems:
            subs.add(new_sub)
            subsets(new_sub, subs)

    return subs

print subsets([1, 2, 3, 4])
