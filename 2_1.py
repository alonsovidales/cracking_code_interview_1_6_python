# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

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
    def remove_duplicates(self):
        vals = set()
        
        prev = None
        curr = self._list
        while curr is not None:
            if curr.v in vals:
                prev.next = curr.next
                curr = curr.next
            else:
                vals.add(curr.v)
                prev = curr
                curr = curr.next

    # O(n^2)
    def remove_duplicates_no_buff(self):
        curr_1 = self._list
        while curr_1 is not None:
            prev = curr_1
            curr_2 = curr_1.next
            while curr_2 is not None:
                if curr_1.v == curr_2.v:
                    prev.next = curr_2.next
                    curr_2 = curr_2.next
                else:
                    prev = curr_2
                    curr_2 = curr_2.next

            curr_1 = curr_1.next

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
l.remove_duplicates()
print l

l = LinkedList()
l.append(2)
l.append(3)
l.append(2)
l.append(4)
l.append(7)
l.append(2)
l.append(7)
l.remove_duplicates_no_buff()
print l

l = LinkedList()
l.remove_duplicates_no_buff()
print l
