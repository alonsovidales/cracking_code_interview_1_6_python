# How would you design a stack which, in addition to push and pop, also has a function
# min which returns the minimum element? Push, pop and min should all operate in
# O(1) time.

class MinStack(object):
    class Node(object):
        def __init__(self, v, nex, min_v):
            self.v = v
            self.nex = nex
            self.curr_min = min_v

    def __init__(self):
        self._stack = None
        self._min_v = float('inf')

    def push(self, v):
        self._stack = self.Node(v, self._stack, self._min_v)
        if v < self._min_v:
            self._min_v = v

    def min(self):
        if self._stack is None:
            return None
        return min(self._stack.curr_min, self._stack.v)

    def pop(self):
        n = self._stack
        self._stack = self._stack.nex

        return n.v

ms = MinStack()
ms.push(4)
print "Push:", 4, ms.min()
ms.push(3)
print "Push:", 3, ms.min()
ms.push(4)
print "Push:", 4, ms.min()
ms.push(5)
print "Push:", 5, ms.min()
ms.push(6)
print "Push:", 6, ms.min()
ms.push(2)
print "Push:", 2, ms.min()
ms.push(3)
print "Push:", 3, ms.min()
ms.push(1)
print "Push:", 1, ms.min()
ms.push(9)
print "Push:", 9, ms.min()
ms.push(2)
print "Push:", 2, ms.min()
ms.push(1123)
print "Push:", 1123, ms.min()

print "Pop:", ms.pop()
print "Min:", ms.min()
print "Pop:", ms.pop()
print "Min:", ms.min()
print "Pop:", ms.pop()
print "Min:", ms.min()
print "Pop:", ms.pop()
print "Min:", ms.min()
print "Pop:", ms.pop()
print "Min:", ms.min()
print "Pop:", ms.pop()
print "Min:", ms.min()
print "Pop:", ms.pop()
print "Min:", ms.min()
print "Pop:", ms.pop()
print "Min:", ms.min()
print "Pop:", ms.pop()
print "Min:", ms.min()
print "Pop:", ms.pop()
print "Min:", ms.min()
print "Pop:", ms.pop()
print "Min:", ms.min()
