# Implement an algorithm to print all valid (e g , properly opened and closed)
# combi- nations of n-pairs of parentheses
# EXAMPLE:
# input: 3 (e g , 3 pairs of parentheses)
# output: ()()(), ()(()), (())(), ((()))

class Balancer(object):
    def _valid(self, parents):
        opens = 0
        for c in parents:
            if c == '(':
                opens += 1
            else:
                opens -= 1
                if opens < 0:
                    return False

        return opens == 0

    def _get_perms(self, perm, known=None, valids=None):
        if known is None:
            valids = set()
            known = set()
        if perm in known:
            return known

        if self._valid(perm):
            valids.add(perm)
        known.add(perm)

        for i in xrange(len(perm)-1):
            perm_list = list(perm)
            a = perm_list[i]
            perm_list[i] = perm_list[i+1]
            perm_list[i+1] = perm_list[i]
            self._get_perms(''.join(perm_list), known, valids)

        return valids


    def get_balanced(self, p):
        init_str = ''
        for i in xrange(p):
            init_str += '()'

        return self._get_perms(init_str)


bc = Balancer()
result = bc.get_balanced(3)
for r in result:
    print r
