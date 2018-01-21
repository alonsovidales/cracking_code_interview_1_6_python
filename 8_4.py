# Write a method to compute all permutations of a string

def str_perms(s, perms=None):
    if perms is None:
        perms = set()
    if s in perms:
        return perms

    perms.add(s)

    list_str = list(s)
    for i in xrange(len(list_str)):
        for j in xrange(len(list_str)):
            aux = list_str[i]
            list_str[i] = list_str[j]
            list_str[j] = aux
            perms |= str_perms(''.join(list_str), perms)


    return perms

perms = str_perms('hello')
for s in perms:
    print s
