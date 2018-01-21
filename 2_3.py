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

        return prev.next

    # O(1)
    def remove(self, node):
        assert node.next is not None
        node.v = node.next.v
        node.next = node.next.next

    def __str__(self):
        vals = []
        curr = self._list
        while curr is not None:
            vals.append(curr.v)
            curr = curr.next

        return ' '.join(map(str, vals))


l = LinkedList()
l.append(2)
to_remove = l.append(3)
l.append(2)
l.append(4)
l.append(7)
l.append(2)
l.append(7)

l.remove(to_remove)
print l
