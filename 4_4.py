# Given a binary search tree, design an algorithm which creates a linked list
# of all the nodes at each depth (i e , if you have a tree with depth D, you'll
# have D linked lists)

class SuperLinkedlist(object):
    class Node(object):
        def __init__(self, v, nex=None):
            self.v = v
            self.next = nex

        def __str__(self):
            r = []
            p = self
            while p != None:
                r.append(str(p.v))
                p = p.next

            return ', '.join(r)

    def __init__(self):
        self._lists = []

    def convert_tree(self, t, deep=0):
        if t is None:
            return

        n = self.Node(t.v)
        if len(self._lists) < deep+1:
            self._lists.append(n)
        else:
            n.next = self._lists[deep]
            self._lists[deep] = n

        self.convert_tree(t.l, deep+1)
        self.convert_tree(t.r, deep+1)

    def __str__(self):
        r = []
        for l in self._lists:
            r.append(str(l))

        return '\n'.join(r)

class BTreeNode(object):
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

bt = BTreeNode(9,
        BTreeNode(5,
            BTreeNode(3),
            BTreeNode(8)),
        BTreeNode(10,
            BTreeNode(7),
            BTreeNode(12)))

sl = SuperLinkedlist()
sl.convert_tree(bt)

print sl
