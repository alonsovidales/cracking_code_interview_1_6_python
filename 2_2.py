# Implement an algorithm to find the nth to last element of a singly linked list

class LinkedList(object):
    def __init__(self):
        self._list = None

    class Node(object):
        def __init__(self, value):
            self.next = None
            self.v = value

    def append(self, v):
        if self._list is None:
            self._list = self.Node(v)
            return

        prev = self._list
        curr = self._list.next
        while curr is not None:
            prev = curr
            curr = curr.next

        prev.next = self.Node(v)

    # O(n)
    def nth_end(self, n):
        p1 = self._list
        p2 = self._list
        dist = 0
        while p2 is not None:
            if dist >= n+1:
                p1 = p1.next

            dist += 1
            p2 = p2.next

        if dist < n:
            return None

        return p1.v

    def __str__(self):
        vals = []
        curr = self._list
        while curr is not None:
            vals.append(curr.v)
            curr = curr.next

        return ' '.join(map(str, vals))


l = LinkedList()
l.append(2)
l.append(3)
l.append(2)
l.append(4)
l.append(7)
l.append(2)
l.append(7)
print l.nth_end(0)
print l.nth_end(3)
print l.nth_end(4)
