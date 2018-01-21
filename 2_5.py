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

    def make_a_loop(self, node):
        curr = self._list
        while curr.next is not None:
            curr = curr.next

        curr.next = node

    def get_first_circle(self):
        curr = self._list
        known_nodes = set()
        while curr.next is not None:
            if curr in known_nodes:
                return curr
            known_nodes.add(curr)
            curr = curr.next
        

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
node = l.append(4)
l.append(7)
l.append(2)
l.append(7)

l.make_a_loop(node)

print l.get_first_circle().v
