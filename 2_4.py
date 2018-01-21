"""
You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1's digit is at the head of
the list. Write a function that adds the two numbers and returns the sum as a linked
list.
EXAMPLE
Input: (3 -> 1 -> 5), (5 -> 9 -> 2)
Output: 8 -> 0 -> 8
"""

class LinkedList(object):
    def __init__(self, length):
        self._lists = [None] * length

    class Node(object):
        def __init__(self, value):
            self.next = None
            self.v = value

    def append(self, l_id, v):
        if self._lists[l_id] is None:
            self._lists[l_id] = self.Node(v)
            return

        prev = self._lists[l_id]
        curr = self._lists[l_id].next
        while curr is not None:
            prev = curr
            curr = curr.next

        prev.next = self.Node(v)

        return prev.next

    def sum_all(self):
        poniters = []
        for l in self._lists:
            poniters.append(l)

        result = LinkedList(1)
        all_none = False
        carry = 0
        while not all_none:
            all_none = True
            new_v = carry
            for l in xrange(len(poniters)):
                if poniters[l] is not None:
                    all_none = False
                    new_v += poniters[l].v
                    poniters[l] = poniters[l].next

            carry = new_v / 10
            new_v %= 10
            if not all_none or new_v != 0:
                result.append(0, new_v)

        return result

    def __str__(self):
        vals = []
        for l in self._lists:
            curr = l
            while curr is not None:
                vals.append(curr.v)
                curr = curr.next
            vals.append("-")

        return ' '.join(map(str, vals))


l = LinkedList(2)
l.append(0, 3)
l.append(0, 1)
l.append(0, 5)
l.append(1, 5)
l.append(1, 9)
l.append(1, 2)

print l
print l.sum_all()
