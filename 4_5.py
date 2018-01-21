# Write an algorithm to find the 'next' node (i e , in-order successor) of a
# given node in a binary search tree where each node has a link to its parent

class BTreeNode(object):
    def __init__(self, v, l=None, r=None, p=None):
        self.v = v
        self.l = l
        self.r = r
        self.p = p

        if l is not None:
            l.p = self
        if r is not None:
            r.p = self

    def _get_next(self):
        if self.l is not None:
            return self.l._get_next()

        return self.v

    def get_next(self):
        if self.r:
            return self.r._get_next()

        return None

node_5 = BTreeNode(5,
        BTreeNode(3),
        BTreeNode(8))
bt = BTreeNode(9,
        node_5,
        BTreeNode(10,
            BTreeNode(11),
            BTreeNode(12)))

print bt.get_next()
print node_5.get_next()
