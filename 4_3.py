# Given a sorted (increasing order) array, write an algorithm to create a
# binary tree with minimal height
# 1, 4, 5, 6, 8, 9

class BTree(object):
    class Node(object):
        def __init__(self, v, l=None, r=None):
            self.v = v
            self.l = l
            self.r = r

    def __init__(self):
        self._root = None
        
    def addArr(self, arr):
        self.add(arr[len(arr)/2])
        if len(arr) > 2:
            self.addArr(arr[:len(arr)/2])
            self.addArr(arr[len(arr)/2+1:])
        else:
            for e in arr:
                self.add(e)

    def add(self, v):
        n = self.Node(v)
        if self._root is None:
            self._root = n
            return
        else:
            p = self._root
            while True:
                if p.v > v:
                    if p.r is None:
                        p.r = n
                        return
                    else:
                        p = p.r
                else:
                    if p.l is None:
                        p.l = n
                        return
                    else:
                        p = p.l



bt = BTree()
bt.addArr((1, 4, 5, 6, 8, 9))
