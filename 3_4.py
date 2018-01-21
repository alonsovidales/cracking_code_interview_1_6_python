class TowerStack(object):
    class Disk(object):
        def __init__(self, size, next_disk):
            self.size = size
            self.next = next_disk

    def __init__(self):
        self._stack = None
        self._size = 0

    def __str__(self):
        result = []
        p = self._stack
        while p is not None:
            result.append(p.size)
            p = p.next

        return ', '.join(map(str, result))

    def push(self, size):
        if self._stack is not None and size > self._stack.size:
            return False

        self._stack = self.Disk(size, self._stack)
        self._size += 1

        return True

    def pop(self):
        if self._stack is None:
            return None

        node = self._stack
        self._stack = self._stack.next
        self._size -= 1

        return node.size

    def __len__(self):
        return self._size

class Hanoi(object):
    def __init__(self, sizes):
        self._towers = (TowerStack(), TowerStack(), TowerStack())
        for s in sizes:
            if not self._towers[0].push(s):
                raise Exception('The sizes are not properly ordered')

    def __str__(self):
        return '|'.join(map(str, self._towers))

    def move_to_right(self, known_positions=None, found=None):
        if known_positions is None:
            found = [False]
            known_positions = set()
        if found[0] or str(self) in known_positions:
            return
        known_positions.add(str(self))
        print str(self)
        if sum(map(len, self._towers[:len(self._towers)-1])) == 0:
            found[0] = True
            return

        for i in xrange(len(self._towers)):
            disk = self._towers[i].pop()
            if disk is not None:
                for j in xrange(len(self._towers)):
                    if i != j and self._towers[j].push(disk):
                        self.move_to_right(known_positions, found)
                        self._towers[j].pop()

                self._towers[i].push(disk)

hn = Hanoi((5, 4, 3, 2, 1))
hn.move_to_right()
