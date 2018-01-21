# You have two very large binary trees: T1, with millions of nodes, and T2,
# with hun- dreds of nodes Create an algorithm to decide if T2 is a subtree of
# T1

class Node(object):
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

class TreeHandler(object):
    def _check_same(self, t1, t2):
        if t1.v != t2.v:
            return False

        if t1.l is not None and t2.l is not None:
            if not self._check_same(t1.l, t2.l):
                return False
        elif t2.l is not None:
            return False

        if t1.l is not None and t2.l is not None:
            if not self._check_same(t1.l, t2.l):
                return False
        elif t2.l is not None:
            return False

        return True

    def is_subtree(self, t1, t2):
        return (
                self._check_same(t1, t2) or
                (t1.l is not None and self.is_subtree(t1.l, t2)) or
                (t1.r is not None and self.is_subtree(t1.r, t2))
               )
