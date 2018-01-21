# Implement a MyQueue class which implements a queue using two stacks.

class MyQueue(object):
    def __init__(self):
        self._arrs = ([], [])

    def enqueue(self, v):
        self._arrs[0].append(v)

    def dequeue(self):
        if len(self._arrs[1]) == 0:
            while len(self._arrs[0]) > 0:
                self._arrs[1].append(self._arrs[0].pop())

        return self._arrs[1].pop()

mq = MyQueue()
mq.enqueue(1)
mq.enqueue(2)
mq.enqueue(3)
print mq.dequeue()
mq.enqueue(4)
mq.enqueue(5)
mq.enqueue(6)
print mq.dequeue()
mq.enqueue(7)
mq.enqueue(8)
mq.enqueue(9)
print mq.dequeue()
mq.enqueue(10)
mq.enqueue(11)

print mq.dequeue()
print mq.dequeue()
print mq.dequeue()
print mq.dequeue()
print mq.dequeue()
