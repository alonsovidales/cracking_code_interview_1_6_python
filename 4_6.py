# Design an algorithm and write code to  nd the  rst common ancestor of two
# nodes in a binary tree Avoid storing additional nodes in a data structure
# NOTE: This is not necessarily a binary search tree

# 19:03

class BTreeNode(object):
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

    def _find_common_ancestor(self, n1, n2, ancestor):
        if self.v == n1 or self.v == n2:
            return True

        if self.l is not None:
            found_l = self.l._find_common_ancestor(n1, n2, ancestor)
        else:
            found_l = False

        if self.r is not None:
            found_r = self.r._find_common_ancestor(n1, n2, ancestor)
        else:
            found_r = False

        if found_l and found_r and ancestor[0] is None:
            ancestor[0] = self.v

        return found_l or found_r

    def find_common_ancestor(self, n1, n2):
        ancestor = [None]
        self._find_common_ancestor(n1, n2, ancestor)

        return ancestor[0]


bt = BTreeNode(9,
        BTreeNode(5,
            BTreeNode(3),
            BTreeNode(8)),
        BTreeNode(10,
            BTreeNode(7),
            BTreeNode(12)))

print bt.find_common_ancestor(3, 10)
print bt.find_common_ancestor(3, 8)
print bt.find_common_ancestor(3, 5)
print bt.find_common_ancestor(3, 122)
