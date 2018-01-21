# Implement a function to check if a tree is balanced For the purposes of this
# question, a balanced tree is de ned to be a tree such that no two leaf nodes
# di er in distance from the root by more than one

class BinTree(object):
    class Node(object):
        def __init__(self, v, l=None, r=None):
            self.v = v
            self.l = l
            self.r = r

    def __init__(self):
        self._root = None

    def append(self, v):
        n = self.Node(v)
        if self._root is not None:
            aux = self._root
            while True:
                if v > aux.v:
                    if aux.r is not None:
                        aux = aux.r
                    else:
                        aux.r = n
                        return
                elif v < aux.v:
                    if aux.l is not None:
                        aux = aux.l
                    else:
                        aux.l = n
                        return
                else:
                    return
        else:
            self._root = n

    def _get_deeps(self, node, deeps, curr_deep):
        if node.l is None and node.r is None:
            deeps.append(curr_deep)

        if node.l is not None:
            self._get_deeps(node.l, deeps, curr_deep+1)
        if node.r is not None:
            self._get_deeps(node.r, deeps, curr_deep+1)

        return deeps

    def is_balanced(self, root=None, deeps=None):
        deeps = self._get_deeps(self._root, [], 0)

        return max(deeps)-min(deeps) <= 1



bt = BinTree()
bt.append(4)
bt.append(3)
bt.append(2)
bt.append(1)
bt.append(6)

print bt.is_balanced()

bt = BinTree()
bt.append(4)
bt.append(3)
bt.append(2)
bt.append(6)
bt.append(5)

print bt.is_balanced()
